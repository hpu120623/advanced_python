# 生成器读取大文件
def my_readLines(f, newline):
    buf = '' # 缓存
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline)]
        chuck = f.read(4096)
        if not chuck:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chuck

with open('input.txt') as f:
    for line in my_readLines(f, "{|}"):
        print(line)