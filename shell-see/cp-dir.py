import os

# 获取源文件路径
source_file = input("Enter the source file path: ")

# 获取目标文件路径
target_file = input("Enter the target file path: ")

# 运行 cp 命令
os.system(f"cp {source_file} {target_file}")



