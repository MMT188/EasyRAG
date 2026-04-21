import streamlit as st
from rag import RagService
import config_data as config
from knowledge_base import KnowledgeBaseService
from file_parser import parse_file  # 导入多格式解析

# 页面配置
st.set_page_config(page_title="RAG智能客服", layout="wide")
st.title("智能客服 🤖")
st.divider()

# ======================
# 左侧：文件上传区域
# ======================
with st.sidebar:
    st.header("📁 上传知识库文件")
    uploaded_file = st.file_uploader(
        "支持 PDF / DOCX / TXT",
        type=['txt', 'pdf', 'docx'],
        accept_multiple_files=False
    )

    # 上传文件 → 实时入库
    if uploaded_file is not None:
        with st.spinner("解析并入库中..."):
            # 1. 解析文件
            file_content = parse_file(
                file_bytes=uploaded_file,
                file_name=uploaded_file.name
            )

            # 2. 实时入库
            kb_service = KnowledgeBaseService()
            result = kb_service.upload_by_str(file_content, uploaded_file.name)

            st.success(result)

# ======================
# 右侧：聊天对话区域
# ======================
# 初始化聊天历史
if "message" not in st.session_state:
    st.session_state["message"] = [
        {"role": "assistant", "content": "你好！我可以帮你解答文档问题～"}
    ]

# 初始化RAG（只初始化一次）
if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

# 渲染历史消息
for msg in st.session_state["message"]:
    st.chat_message(msg["role"]).write(msg["content"])

# 用户输入
prompt = st.chat_input("请输入你的问题...")

if prompt:
    # 显示用户问题
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    ai_ans = []
    with st.spinner("思考中..."):
        # 调用RAG（实时读取最新向量库）
        stream = st.session_state["rag"].chain.stream(
            {"input": prompt},
            config.session_config
        )

        # 流式输出
        def capture(stream_gen, cache):
            for chunk in stream_gen:
                cache.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(stream, ai_ans))

    # 保存回答
    full_ans = "".join(ai_ans)
    st.session_state["message"].append({"role": "assistant", "content": full_ans})