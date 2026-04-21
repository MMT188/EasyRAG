EasyRAG 一体化本地知识库问答系统
极简部署・单页面全功能・多格式文档・实时生效・RAG 智能问答
基于 Streamlit + LangChain + Chroma 构建的轻量化一站式 RAG 检索增强生成系统。真正实现文档上传 + 智能对话一体化，无需切换页面、无需重启服务，上传即生效，开箱即用，非常适合本地知识库落地、RAG 学习实践与简历项目展示。
✨ 项目核心亮点
✅ 一体化单页面架构文档上传、知识库入库、智能问答、多轮对话，一个页面全部完成，无需拆分服务。
✅ 多格式文档支持支持 TXT / PDF / DOCX（Word） 自动解析、文本提取、智能分块。
✅ 知识库实时更新上传文档后立即写入向量库，无需重启服务，AI 即刻使用最新知识。
✅ MD5 内容级去重基于文件内容生成唯一指纹，相同内容自动跳过，避免重复入库。
✅ 标准 RAG 检索问答向量检索 + 上下文拼接 + 大模型生成，回答精准、可解释、可控。
✅ 多轮对话记忆支持上下文理解、连续追问，对话历史本地持久化。
✅ AI 流式输出回答逐字显示，交互流畅，接近商用智能客服体验。
✅ 全本地轻量部署无数据库依赖，无环境复杂度，数据完全本地化，安全可控。
🧩 项目结构
EasyRAG-main/├── app_chat.py # 主程序（一体化页面：上传 + 对话）├── file_parser.py # 多格式文档解析器（TXT/PDF/DOCX）├── knowledge_base.py # 文档处理、切片、MD5 去重、向量入库├── rag.py # RAG 核心链、对话历史管理├── vector_stores.py # Chroma 向量库封装├── file_history_store.py # 对话历史本地存储├── config_data.py # 全局配置├── requirements.txt # 依赖包└── README.md # 说明文档
🛠️ 环境部署
1. 克隆项目
git clone https://github.com/你的用户名 / EasyRAG.gitcd EasyRAG
2. 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
3. 配置 API Key（通义千问）
Windowsset DASHSCOPE_API_KEY = 你的 APIKEY
Mac/Linuxexport DASHSCOPE_API_KEY = 你的 APIKEY
也可直接写入 config_data.py 中。
4. 启动系统（仅需一条命令）
streamlit run app_chat.py
📌 使用流程
打开浏览器页面
左侧上传文档（.txt / .pdf / .docx）
自动解析 → 去重 → 分块 → 向量入库
右侧直接聊天提问
AI 基于你上传的知识库进行精准回答
🧠 技术栈
Python 3.10+
Streamlit — Web 交互界面
LangChain — RAG 流程编排
Chroma — 本地轻量级向量数据库
DashScope Embedding — 文本向量化
Qwen / 通义千问 — 大语言模型
PyPDF2 /python-docx — 多格式文档解析
📁 支持格式
✅ .txt
✅ .pdf
✅ .docx（Word）
📋 功能清单
 单页面一体化：上传 + 对话
 多格式文档自动解析
 实时向量入库，无需重启服务
 MD5 内容去重
 智能文本递归分块
 RAG 检索增强问答
 多轮对话历史记忆
 AI 流式打字输出
 本地持久化存储
 极简部署，开箱即用
🛟 常见问题
1. 上传文档后需要重启吗？
不需要！上传即生效。
2. 重复上传会重复入库吗？
不会，系统自动 MD5 去重，已存在内容会直接提示。
3. 为什么回答没有用到知识库？
确认上传后提示 [Success]
检查 config_data.py 中向量库路径、集合名一致
问题与文档内容匹配度较低
🌟 扩展方向（进阶升级）
支持 Excel、Markdown、PPT、图片 OCR
加入 Rerank 重排序模型，提升检索精度
增加知识库管理：查看、删除、清空文档
多用户会话隔离
扩展为 Agent 智能体
替换向量库为 FAISS / Milvus
📄 许可证
MIT License 开源免费
