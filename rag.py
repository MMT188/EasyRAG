from langchain_core.documents import Document # 文档对象（文本+元数据）
from langchain_core.output_parsers import StrOutputParser # 输出转字符串
# 链式调用核心
from langchain_core.runnables.history import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from file_history_store import get_history # 对话历史存储（文件存储）
from vector_stores import VectorStoreService # 向量库服务类
from langchain_community.embeddings import DashScopeEmbeddings # 阿里向量模型
import config_data as config
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # 提示词模板 + 历史占位
from langchain_community.chat_models.tongyi import ChatTongyi # 通义千问


def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)

    return prompt


class RagService(object):
    # 初始化
    def __init__(self):
        self.vector_service = VectorStoreService(
                    # DashScopeEmbeddings：阿里灵积向量模型
            embedding=DashScopeEmbeddings(model=config.embedding_model_name)
        )

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "我将参考资料，并根据资料信息简洁和专业的回答用户问题。参考资料:\n{context}"
                           "并且我提供用户的对话历史记录，如下："),
                #  "简洁和专业的回答用户问题。参考资料:{context}。"),
                # ("system", "并且我提供用户的对话历史记录，如下："),
                MessagesPlaceholder("history"),
                ("user", "请回答用户提问：{input}")
            ]
        )

        self.chat_model = ChatTongyi(model=config.chat_model_name)

        self.chain = self.__get_chain()

    def __get_chain(self):
        """获取最终的执行链"""

        retriever = self.vector_service.get_retriever()     # 检索文档数量控制

        # 文档格式化
        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"

            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段：\n{doc.page_content}\n文档元数据：{doc.metadata}\n\n"

            return formatted_str

        # 数据预处理
        def format_for_retriever(value: dict)->str:

            return value["input"]

        # 重组成提示词模板需要的格式
        def format_for_prompt_template(value):
            # {input, context, history}
            new_value = {}
            new_value["input"] = value["input"]["input"]
            new_value["context"] = value["context"]
            new_value["history"] = value["input"]["history"]
            return new_value


        chain = (
            {
                "input": RunnablePassthrough(),
                "context": RunnableLambda(format_for_retriever) | retriever | format_document
            }
            | RunnableLambda(format_for_prompt_template)
            | self.prompt_template
            | print_prompt
            | self.chat_model
            | StrOutputParser()
        )
        # 增强的链
        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

        return conversation_chain

# 测试
if __name__ == '__main__':

    res = RagService().chain.invoke({"input":"我之前问了什么"},config.session_config)
    print(res)

