import os
import re

def read_file_with_encoding(file_path):
    encodings = ['utf-8', 'gbk']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            return content, encoding
        except UnicodeDecodeError:
            pass
    raise UnicodeDecodeError(f"Cannot decode file {file_path} with supported encodings {encodings}")

def write_file_with_encoding(file_path, content, encoding):
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(content)

def replace_jsp_expressions(file_path):
    content, encoding = read_file_with_encoding(file_path)

    # 正则表达式匹配 ${xxx} 格式的字符串，但忽略以 ${# 开头的
    pattern = r'\$\{(?!#)([^}]+)\}'

    def replacement(match):
        variable = match.group(1)
        return f'${{JspStringUtils.retainExpression({variable}, "${{{variable}}}")}}'

    new_content = re.sub(pattern, replacement, content)

    write_file_with_encoding(file_path, new_content, encoding)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jsp'):
                file_path = os.path.join(root, file)
                print(f'Processing: {file_path}')
                replace_jsp_expressions(file_path)


if __name__ == '__main__':
    directory = '/Users/quandaling/work/martini/start/src/main/resources/META-INF/resources'  # 请替换为你的JSP文件夹路径
    process_directory(directory)
