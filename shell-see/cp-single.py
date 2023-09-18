import os

# 获取源文件路径
source_path = input("Enter the source folder path: ")

# 获取目标文件路径
target_path = input("Enter the target folder path: ")

# 遍历源文件夹中的所有文件
for root, dirs, files in os.walk(source_path):
    for file in files:
        # 获取源文件和目标文件路径
        source_file = os.path.join(root, file)
        target_file = os.path.join(target_path, file)
        # 运行 cp 命令
        os.system(f"cp {source_file} {target_file}")
