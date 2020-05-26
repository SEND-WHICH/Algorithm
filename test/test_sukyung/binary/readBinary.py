'''
# 바이너리 쓰기
data = [1, 2, 3, 4, 5]
with open("test.bin", "wb") as f:
    f.write(bytes(data))
'''
# 바이너리 읽기
#with open("word.docx", "rb") as f:
with open("hwp.hwp", "rb") as f:
    content = f.read()  # 모두 읽음
    print(type(content))  # bytes class
    for b in content:
        print(b)
