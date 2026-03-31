import pandas as pd
from dashscope import Generation

# 配置阿里云 DashScope 的 API Key
DASHSCOPE_API_KEY = "sk-3dc68e67f85847098ce3908f4c741498"  # 替换为你的阿里云 DashScope API Key

# 定义分类提示词模板
CLASSIFICATION_PROMPT_TEMPLATE = """
请根据以下预定义的类别对问题进行分类：
类别选项：[不会英语,费用介绍,客户拒绝,没有效果,平台介绍,如何合作,身份确认,行业咨询,已经合作,做线下业务,关税相关问题]
要求1：只输出分类结果，禁止输出其他无关文字
要求2：如果没有命中类别，输出null

问题：{question}
"""

# 读取 Excel 文件中的指定 Sheet
def read_excel(file_path, sheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Excel 文件中的 {sheet_name} 工作表读取成功！")
        return df
    except Exception as e:
        print(f"读取 Excel 文件失败: {e}")
        return None

# 调用 LLM 模型进行问题分类
def classify_question(question):
    try:
        # 构造 Prompt
        prompt = CLASSIFICATION_PROMPT_TEMPLATE.format(question=question)

        # 调用阿里云的文本生成模型
        response = Generation.call(
            api_key=DASHSCOPE_API_KEY,
            prompt=prompt,
            model="qwen-max"  # 替换为具体的模型名称（如 Qwen 或其他）
        )
        if response.status_code == 200:
            # 提取模型返回的分类结果
            classification_result = response.output["text"].strip()
            print(f"LLM ai input: {question}. ai result: {classification_result}")
            return classification_result
        else:
            print(f"模型调用失败: {response.message}")
            return None
    except Exception as e:
        print(f"调用 LLM 模型时发生错误: {e}")
        return None

# 处理 Excel 数据并新增分类列
def process_excel(df):
    if df is None:
        return None

    # 新增一列 "问题分类"
    df["问题分类"] = None

    for index, row in df.iterrows():
        original_question = row["原始问题"]
        refined_question = row["问题抽取"]

        # 优先使用提炼后的问题进行分类
        question_to_classify = refined_question if refined_question else original_question

        # 调用 LLM 模型进行分类
        classification = classify_question(question_to_classify)

        # 将分类结果写入 DataFrame
        df.at[index, "问题分类"] = classification

    print("问题分类完成！")
    return df

# 写回 Excel 文件
def write_excel(df, output_file_path):
    try:
        df.to_excel(output_file_path, index=False)
        print(f"结果已写入文件: {output_file_path}")
    except Exception as e:
        print(f"写入 Excel 文件失败: {e}")

# 主函数
def main():
    input_file_path = "/Users/quandaling/Desktop/新QA分类明细.xlsx"  # 输入 Excel 文件路径
    output_file_path = "/Users/quandaling/Desktop/新QA分类明细done.xlsx"  # 输出 Excel 文件路径
    sheet_name = "Sheet1"  # 指定要读取的工作表名称

    # 读取 Excel 数据
    df = read_excel(input_file_path, sheet_name)
    if df is None:
        return

    # 处理数据并新增分类列
    df = process_excel(df)
    if df is None:
        return

    # 写回结果到新的 Excel 文件
    write_excel(df, output_file_path)

if __name__ == "__main__":
    main()
