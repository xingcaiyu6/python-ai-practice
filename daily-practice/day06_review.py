# Day 06 - 综合巩固

"""
说明：补全函数体，运行 `python day06_review.py` 全绿即通过。
      今天题目混合了前五天的知识点，考验综合运用能力。
"""

import os, tempfile, json
from itertools import chain
from collections import defaultdict

# ============================================================
# 题1：展平嵌套列表
# 写一个函数，把一个嵌套列表（最多两层）展平成一维
# 例：[[1,2],[3,4],[5]] → [1,2,3,4,5]
# 提示：用 itertools.chain 或双层循环
# ============================================================
def flatten(nested):
    return list(chain.from_iterable(nested))
    # TODO
    pass


# ============================================================
# 题2：按首字母分组
# 写一个函数，把单词列表按首字母分组，返回 {首字母: [单词列表]}
# 忽略大小写，统一用小写首字母。用 defaultdict(list)
# 例：["Apple","ant","Bee"] → {"a":["Apple","ant"],"b":["Bee"]}
# ============================================================
def group_by_first(words):
    groups = defaultdict(list)
    for word in words:
        if word:  # 检查单词不为空
            first_char = word[0].lower()
            groups[first_char].append(word)
    return dict(groups)
    # TODO
    pass


# ============================================================
# 题3：类 + __str__
# 写一个 Book 类，属性 title、author，__str__ 返回 "《title》- author"
# 例：str(Book("活着", "余华")) → "《活着》- 余华"
# ============================================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"《{self.title}》- {self.author}"
    # TODO
    pass


# ============================================================
# 题4：JSON 读写
# 写一个函数，把字典写入 JSON 文件，ensure_ascii=False, indent=2
# 例：save_json("t.json", {"a":1}) → 文件内容为格式化 JSON
# ============================================================
def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    # TODO
    pass


# ============================================================
# 题5：排序对象列表
# 写一个函数，输入 Book 对象列表，按 title 长度升序返回 title 列表
# 例：[Book("A","x"), Book("CCC","y"), Book("BB","z")]
#     → ["A", "BB", "CCC"]
# ============================================================
def sort_books_by_title_len(books):
    sorted_books = sorted(books, key=lambda book: len(book.title))
    return [book.title for book in sorted_books]
    # TODO
    pass


# ============================================================
# 题6：集合推导式
# 写一个函数，返回 1 到 n 中所有质数的集合，用集合推导式
# 例：primes(10) → {2,3,5,7}
# ============================================================
def primes(n):
    return {x for x in range(2, n+1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))}
    # TODO：{x for x in range(2,n+1) if ...}
    pass


# ============================================================
# 题7：字符串加密
# 写一个函数，把字符串每个字符的 Unicode 码加 1，返回新字符串
# 例："abc" → "bcd"
# ============================================================
def shift_chars(s):
    return ''.join(chr(ord(c) + 1) for c in s)
    # TODO：用 chr(ord(c)+1)
    pass


# ============================================================
# 题8：路径拼接
# 写一个函数，用 os.path.join 拼接目录和文件名，返回完整路径
# 例：join_path("C:/data", "file.txt") → "C:/data/file.txt"
# ============================================================
def join_path(directory, filename):
    return os.path.join(directory, filename)
    # TODO
    pass


# ============================================================
# 题9：统计文件大小
# 写一个函数，返回文件的大小（字节数）。文件不存在返回 -1
# 例：一个 100 字节的文件 → 100
# ============================================================
def file_size(filepath):
    try:
        return os.path.getsize(filepath)
    except FileNotFoundError:
        return -1
    # TODO：os.path.getsize + try/except
    pass


# ============================================================
# 题10：综合 - 词频报表
# 输入一个文本文件路径，返回出现次数前 n 的单词 [(单词,次数),...]，降序
# 忽略大小写、忽略标点（只保留字母和数字）
# 例：文件 "Hello world\nHello Python" → top_words(path, 2) → [("hello",2),("world",1)]
# ============================================================
def top_words(filepath, n):
    from collections import Counter
    
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char.lower()
        else:
            cleaned_text += ' '
    
    words = [word for word in cleaned_text.split() if word]
    
    counter = Counter(words)
    
    return counter.most_common(n)[:n]
    # TODO：读文件→分词→计数→排序→取前n
    pass


# ============================================================
# 测试代码 - 不动
# ============================================================
if __name__ == "__main__":
    tests = []
    tmpdir = tempfile.mkdtemp()

    # 题1
    tests.append(("题1a", flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]))
    tests.append(("题1b", flatten([]) == []))

    # 题2
    expected = {"a": ["Apple", "ant"], "b": ["Bee"]}
    tests.append(("题2", group_by_first(["Apple", "ant", "Bee"]) == expected))

    # 题3
    b = Book("活着", "余华")
    tests.append(("题3", str(b) == "《活着》- 余华"))

    # 题4
    f4 = os.path.join(tmpdir, "t4.json")
    save_json(f4, {"name": "小明", "age": 20})
    with open(f4, "r", encoding="utf-8") as f:
        data = json.load(f)
    tests.append(("题4", data == {"name": "小明", "age": 20}))

    # 题5
    books = [Book("A", "x"), Book("CCC", "y"), Book("BB", "z")]
    tests.append(("题5", sort_books_by_title_len(books) == ["A", "BB", "CCC"]))

    # 题6
    tests.append(("题6", primes(10) == {2, 3, 5, 7}))

    # 题7
    tests.append(("题7", shift_chars("abc") == "bcd"))

    # 题8
    tests.append(("题8", join_path("C:/data", "file.txt") == os.path.join("C:/data", "file.txt")))

    # 题9
    f9 = os.path.join(tmpdir, "t9.txt")
    with open(f9, "w", encoding="utf-8") as f:
        f.write("hello")
    tests.append(("题9a", file_size(f9) == 5))
    tests.append(("题9b", file_size(os.path.join(tmpdir, "nope.txt")) == -1))

    # 题10
    f10 = os.path.join(tmpdir, "t10.txt")
    with open(f10, "w", encoding="utf-8") as f:
        f.write("Hello world\nHello Python")
    result = top_words(f10, 2)
    tests.append(("题10", result == [("hello", 2), ("python", 1)] or result == [("hello", 2), ("world", 1)]))

    all_pass = True
    for name, passed in tests:
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_pass = False
        print(f"[{status}] {name}")

    print("\n==========")
    if all_pass:
        print("OK 全部通过！git commit 吧。")
    else:
        print("X 有未通过的题目，继续加油！")
