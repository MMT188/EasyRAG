def parse_file(file_bytes, file_name):
    """
    通用文件解析：支持 TXT, PDF, DOCX
    """
    file_type = file_name.split(".")[-1].lower()
    content = ""

    # 关键：先读取 bytes
    file_data = file_bytes.read()

    # 1. 解析 TXT
    if file_type == "txt":
        content = file_data.decode("utf-8")

    # 2. 解析 PDF
    elif file_type == "pdf":
        from pypdf import PdfReader
        import io
        reader = PdfReader(io.BytesIO(file_data))
        for page in reader.pages:
            content += page.extract_text()

    # 3. 解析 Word (docx)
    elif file_type == "docx":
        import docx
        import io
        doc = docx.Document(io.BytesIO(file_data))
        content = "\n".join([para.text for para in doc.paragraphs])

    else:
        raise Exception("不支持的文件格式")

    return content