# EasyRAG
一站式文件上传 + RAG 检索增强问答系统，单页面完成文档上传、实时入库、流式对话、多轮记忆，无需切换页面、无需重启服务。
🌟 项目介绍
UniRAG 是一款基于 Streamlit + LangChain + Chroma 构建的一体化本地知识库问答系统。将文档上传、解析、切片、向量化、智能问答、多轮对话、流式输出整合到单个页面，无需切换服务、无需重启，上传文档即可实时问答，开箱即用，适合学习、演示、简历项目、轻量级企业落地。
🚀 核心特性（升级完整版）
✅ 单页面一体化架构上传文件 + 智能对话同屏操作，无需多页面跳转，极致简洁
✅ 支持多格式文档TXT / PDF / DOCX（Word） 自动解析、文本提取
✅ 知识库实时生效上传文档 → 立即入库 → 无需重启服务，AI 立刻读取新知识
✅ MD5 内容去重相同内容不会重复入库，节省存储、提升检索效率
✅ 标准 RAG 检索生成向量检索 → 上下文拼接 → 大模型回答，精准可靠
✅ 多轮对话记忆支持上下文理解、连续追问
✅ AI 流式打字输出回答逐字显示，交互体验接近商用产品
✅ 全本地持久化向量库、对话历史全部本地存储，无需数据库
🧩 项目结构
plaintext
UniRAG-main/
├── app_chat.py              # 主程序：一体化上传 + 对话页面（唯一启动入口）
├── file_parser.py           # 多格式文档解析器（TXT/PDF/DOCX）
├── knowledge_base.py        # 文档处理：切片、MD5去重、向量入库
├── rag.py                   # RAG 核心链、对话历史管理
├── vector_stores.py         # Chroma 向量库封装
├── file_history_store.py    # 对话历史本地存储
├── config_data.py           # 全局配置文件
├── requirements.txt         # 依赖包
└── README.md                # 说明文档
🛠️ 环境部署
1. 克隆项目
bash
运行
git clone https://github.com/你的用户名/UniRAG.git
cd UniRAG
2. 安装依赖
bash
运行
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. 配置 API Key（通义千问）
Windows
cmd
set DASHSCOPE_API_KEY=你的APIKEY
Mac/Linux
bash
运行
export DASHSCOPE_API_KEY=你的APIKEY
也可直接写入 config_data.py 中。
4. 启动系统（唯一命令）
bash
运行
streamlit run app_chat.py
📌 使用流程
打开浏览器页面
左侧上传文档（支持 .txt/.pdf/.docx）
自动解析 → 自动去重 → 自动入库
右侧直接聊天提问
AI 基于你上传的知识库进行回答
🧠 技术栈
Python 3.10+
Streamlit — Web 交互界面
LangChain — RAG 链式调用
Chroma — 本地轻量向量数据库
DashScope Embedding — 文本向量化
Qwen / 通义千问 — 大语言模型
PyPDF2 /python-docx — 多格式文档解析
📁 支持文件格式
✅ .txt
✅ .pdf
✅ .docx（Word）
📝 功能清单
 单页面一体化：上传 + 对话
 多格式文档自动解析
 实时向量入库，无需重启
 MD5 内容去重
 智能文本分块
 RAG 检索增强问答
 多轮对话记忆
 AI 流式输出
 本地持久化存储
 极简部署，开箱即用
🛟 常见问题
1. 上传文档后需要重启吗？
不需要！上传即生效。
2. 重复上传会重复入库吗？
不会，系统自动 MD5 去重。
3. 为什么 AI 没有检索到知识？
确认上传后提示 Success
检查 config_data.py 中向量库路径一致
问题与文档内容不匹配
🌟 扩展方向（进阶升级）
支持 Excel、PPT、图片 OCR
加入 Rerank 重排模型
知识库管理（查看 / 删除文档）
多用户会话隔离
升级为 Agent 智能体
替换向量库为 FAISS / Milvus
📄 许可证
MIT License 开源免费
