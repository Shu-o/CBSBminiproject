#!/usr/bin/env python

import sys

def generate_mutation_file(pdb_file, mutation_file, target_base, mutated_base):
    mutations = []

    # 创建氨基酸三字母代码到单字母代码的映射
    aa_mapping = {
        'ALA': 'A',
        'CYS': 'C',
        'ASP': 'D',
        'GLU': 'E',
        'PHE': 'F',
        'GLY': 'G',
        'HIS': 'H',
        'ILE': 'I',
        'LYS': 'K',
        'LEU': 'L',
        'MET': 'M',
        'ASN': 'N',
        'PRO': 'P',
        'GLN': 'Q',
        'ARG': 'R',
        'SER': 'S',
        'THR': 'T',
        'VAL': 'V',
        'TRP': 'W',
        'TYR': 'Y'
    }

    # 读取PDB文件，提取氨基酸序列信息和残基编号
    sequence = ''
    residue_numbers = []
    with open(pdb_file, 'r') as f:
        for line in f:
            if line.startswith('ATOM'):
                residue_number = line[22:26].strip()
                residue_numbers.append(residue_number)
                amino_acid = line[17:20].strip()
                sequence += aa_mapping.get(amino_acid, 'X')  # 如果找不到映射，默认使用X表示

    # 生成突变文件中的每个突变
#     residue_numbers = list(set(residue_numbers))
    
    with open(mutation_file, 'w') as f:
        for i, residue_number in enumerate(residue_numbers, start=1):
            amino_acid = sequence[i - 1]
            if amino_acid == target_base:
                mutation = f'{target_base}A{residue_number}{mutated_base};'
                mutations.append(mutation)

        # 写入突变文件
        f.write('\n'.join(mutations))

        
def remove_duplicate_lines(file_path):
    lines_seen = set()  # 用于存储已经出现过的行
    output_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # 去除行首和行尾的空白字符
            if line not in lines_seen:  # 如果行不在已出现行的集合中，则将其添加到输出列表中
                lines_seen.add(line)
                output_lines.append(line + '\n')  # 添加行到输出列表，并加上换行符

    with open(file_path, 'w') as file:
        file.writelines(output_lines)



if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: python script.py <pdb_file> <mutation_file> <target_base> <mutated_base>")
        sys.exit(1)

    pdb_file = sys.argv[1]
    mutation_file = sys.argv[2]
    target_base = sys.argv[3]
    mutated_base = sys.argv[4]

    # 调用生成突变文件的函数
    generate_mutation_file(pdb_file, mutation_file, target_base, mutated_base)
    remove_duplicate_lines(mutation_file)
























