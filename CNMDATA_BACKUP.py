"""
任务名称
name: CNMDATA_DATA
定时规则
cron: 0 0 0 * * *
"""

import os
import zipfile
import shutil
from datetime import datetime


def compress_and_clean_pull_directory():
    """
    压缩./Pull目录下的所有文件（除了last_success.json），然后删除原文件
    """
    pull_dir = "./Pull"
    exclude_file = "last_success.json"

    # 检查Pull目录是否存在
    if not os.path.exists(pull_dir):
        print(f"错误：目录 {pull_dir} 不存在")
        return False

    # 获取当前时间作为压缩文件名的一部分
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"pull_backup_{timestamp}.zip"
    zip_path = os.path.join(pull_dir, zip_filename)

    # 获取需要压缩的文件列表
    files_to_compress = []
    dirs_to_compress = []

    try:
        for item in os.listdir(pull_dir):
            item_path = os.path.join(pull_dir, item)

            # 跳过要排除的文件
            if item == exclude_file:
                continue

            # 跳过所有zip文件
            if item.lower().endswith('.zip'):
                continue

            if os.path.isfile(item_path):
                files_to_compress.append(item)
            elif os.path.isdir(item_path):
                dirs_to_compress.append(item)

        # 检查是否有文件需要压缩
        if not files_to_compress and not dirs_to_compress:
            print("没有找到需要压缩的文件或目录")
            return True

        print(f"开始压缩文件到: {zip_filename}")
        print(f"将要压缩的文件: {files_to_compress}")
        print(f"将要压缩的目录: {dirs_to_compress}")

        # 创建压缩文件
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 压缩文件
            for file_name in files_to_compress:
                file_path = os.path.join(pull_dir, file_name)
                zipf.write(file_path, file_name)
                print(f"已添加文件: {file_name}")

            # 压缩目录
            for dir_name in dirs_to_compress:
                dir_path = os.path.join(pull_dir, dir_name)
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # 计算相对于Pull目录的路径
                        arcname = os.path.relpath(file_path, pull_dir)
                        zipf.write(file_path, arcname)
                        print(f"已添加文件: {arcname}")

        print(f"压缩完成: {zip_filename}")

        # 删除原文件和目录
        print("开始删除原文件...")
        for file_name in files_to_compress:
            file_path = os.path.join(pull_dir, file_name)
            try:
                os.remove(file_path)
                print(f"已删除文件: {file_name}")
            except Exception as e:
                print(f"删除文件 {file_name} 时出错: {e}")

        for dir_name in dirs_to_compress:
            dir_path = os.path.join(pull_dir, dir_name)
            try:
                shutil.rmtree(dir_path)
                print(f"已删除目录: {dir_name}")
            except Exception as e:
                print(f"删除目录 {dir_name} 时出错: {e}")

        print("操作完成！")
        return True

    except Exception as e:
        print(f"操作过程中发生错误: {e}")
        return False


def main():
    """主函数"""
    print("=" * 50)
    print("Pull目录文件压缩打包工具")
    print("=" * 50)

    # 显示当前工作目录
    print(f"当前工作目录: {os.getcwd()}")

    # 执行压缩和清理操作
    success = compress_and_clean_pull_directory()

    if success:
        print("\n所有操作已成功完成！")
    else:
        print("\n操作过程中出现错误，请检查日志信息")


if __name__ == "__main__":
    main()