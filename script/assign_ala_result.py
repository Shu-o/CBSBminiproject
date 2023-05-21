#!/usr/bin/env python
import sys


def assign_ala_result(input_file,attr_file,attribute_name):
    # 读取输入文件
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            if line.strip():  # 忽略空行
                line = line.strip().split()
                residue = line[1]
                value = line[-1]
                data.append((residue, value))

    # 写入属性文件
    with open(attr_file, 'w') as f:
        f.write(f"attribute: {attribute_name}\n")
        f.write("match mode: 1-to-1\n")
        f.write("recipient: residues\n")
        for residue, value in data:
            f.write(f"\t:{residue}\t{value}\n")
        
        
if __name__ == '__main__':

    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <attr_file> <attribute_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    attr_file = sys.argv[2]
    attribute_name = sys.argv[3]
    assign_ala_result(input_file,attr_file,attribute_name)
