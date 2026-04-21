# md5去重配置，记录上传文件txt，检查是否重复
md5_path = "./md5.text"

# Chroma向量数据库配置
collection_name="rag"
persist_directory="./chroma_db"

# spliter文本切割配置
chunk_size= 500    # 每块最大字符
chunk_overlap= 100  # 块与块直接重叠的字符
separators =["\n\n","\n",".","!","?","。","！","？"," ",""]    # 分割的优先级

max_spliter_char_number= 1000  # 文本分割阈值

# 相似度K值
top_k = 1     # 检索返回匹配的文档数量

# 模型配置
embedding_model_name="text-embedding-v4"
chat_model_name="qwen3-max-2026-01-23"

#会话配置
session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}