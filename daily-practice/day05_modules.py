# Day 05 - 实用模块与综合练习

"""
说明：补全函数体，运行 `python day05_modules.py` 全绿即通过。
      今天学 collections、re、datetime、csv——日常开发四大金刚。
"""

import os, tempfile, csv, re
from collections import defaultdict
from datetime import datetime, timedelta
from functools import reduce

# ============================================================
# 题1：defaultdict 计数
# 用 defaultdict(int) 统计列表中每个元素出现的次数
# 例：["a","b","a","c","b","a"] → {"a":3, "b":2, "c":1}
# ============================================================
def count_with_defaultdict(items):
    count = defaultdict(int)
    for item in items:
        count[item] += 1
    return count
    # TODO
    pass


# ============================================================
# 题2：正则 - 提取数字
# 写一个函数，提取字符串中所有的数字（连续的数字串），返回整数列表
# 例："订单号123和456，共2件" → [123, 456, 2]
# 提示：re.findall(r"\d+", s)
# ============================================================
def extract_numbers(s):
    return [int(x) for x in re.findall(r"\d+", s)]
    # TODO
    pass


# ============================================================
# 题3：正则 - 验证手机号
# 写一个函数，判断字符串是否是有效手机号
# 规则：1 开头，第二位 3-9，共 11 位数字
# 例："13812345678" → True, "12345678901" → False
# ============================================================
def is_valid_phone(s):
    right_phone = r"1[3-9]\d{9}"
    return re.fullmatch(right_phone, s) is not None

    # TODO：re.fullmatch
    pass


# ============================================================
# 题4：datetime - 计算日期差
# 写一个函数，计算两个日期字符串（格式 YYYY-MM-DD）之间相差多少天
# 例：days_between("2026-06-01", "2026-06-18") → 17
# ============================================================
def days_between(date1, date2):
    return (datetime.strptime(date2, "%Y-%m-%d") - datetime.strptime(date1, "%Y-%m-%d")).days
    # TODO：datetime.strptime
    pass


# ============================================================
# 题5：reduce
# 写一个函数，用 reduce 计算列表中所有数的乘积
# 例：[1,2,3,4] → 24
# ============================================================
def product_reduce(nums):
    return reduce(lambda x,y : x * y,nums)
    # TODO：return reduce(lambda ...
    pass


# ============================================================
# 题6：CSV 读取
# 写一个函数，读取 CSV 文件，返回所有行的列表（每行是一个字典，表头为 key）
# 例：文件 name,age\n小明,20\n → [{"name":"小明","age":"20"}]
# ============================================================
def read_csv(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
    # TODO：用 csv.DictReader
    pass


# ============================================================
# 题7：CSV 写入
# 写一个函数，把字典列表写入 CSV 文件（第一行是表头）。
# 字典的 keys 就是表头。
# 例：write_csv("t.csv", [{"name":"小明","age":"20"}])
# 提示：用 csv.DictWriter，fieldnames=list(data[0].keys())
# ============================================================
def write_csv(filepath, data):
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
    # TODO
    pass


# ============================================================
# 题8：**kwargs
# 写一个函数，接收任意关键字参数，返回一个列表 ["key=value", ...] 按 key 排序
# 例：format_kwargs(name="小明", age="20") → ["age=20", "name=小明"]
# ============================================================
def format_kwargs(**kwargs):
    return [f"{key}={value}" for key, value in sorted(kwargs.items())]
    # TODO
    pass


# ============================================================
# 题9：文件逐行处理
# 写一个函数，读取文件，返回所有包含关键词的行（大小写不敏感）
# 例：文件含 "Hello\nworld\nHELLO"，关键词 "hello" → ["Hello", "HELLO"]
# ============================================================
def grep_lines(filepath, keyword):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if keyword.lower() in line.lower()]
    # TODO：逐行读取，用 in 和 lower()
    pass


# ============================================================
# 题10：综合 - CSV 成绩分析
# 读取一个 CSV 文件（表头 name,score），返回最高分者的姓名。
# 如果文件不存在或多人都为最高分，返回第一个。
# 例：文件 name,score\n小明,85\n小红,92 → "小红"
# ============================================================
def top_student(filepath):

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return max(reader, key=lambda x: int(x["score"]))["name"]
    except FileNotFoundError:
        return ""  # 
    # TODO：用 csv.DictReader
    pass


# ============================================================
# 测试代码 - 不动
# ============================================================
if __name__ == "__main__":
    tests = []
    tmpdir = tempfile.mkdtemp()

    # 题1
    expected = {"a": 3, "b": 2, "c": 1}
    tests.append(("题1", count_with_defaultdict(["a", "b", "a", "c", "b", "a"]) == expected))

    # 题2
    tests.append(("题2", extract_numbers("订单号123和456，共2件") == [123, 456, 2]))

    # 题3
    tests.append(("题3a", is_valid_phone("13812345678") == True))
    tests.append(("题3b", is_valid_phone("12345678901") == False))
    tests.append(("题3c", is_valid_phone("1381234567") == False))

    # 题4
    tests.append(("题4", days_between("2026-06-01", "2026-06-18") == 17))

    # 题5
    tests.append(("题5", product_reduce([1, 2, 3, 4]) == 24))

    # 题6
    f6 = os.path.join(tmpdir, "t6.csv")
    with open(f6, "w", encoding="utf-8", newline="") as f:
        f.write("name,age\n小明,20\n小红,22\n")
    result6 = read_csv(f6)
    tests.append(("题6", result6 == [{"name": "小明", "age": "20"}, {"name": "小红", "age": "22"}]))

    # 题7
    f7 = os.path.join(tmpdir, "t7.csv")
    write_csv(f7, [{"name": "小明", "age": "20"}, {"name": "小红", "age": "22"}])
    with open(f7, "r", encoding="utf-8") as f:
        content = f.read()
    tests.append(("题7", "name,age" in content and "小明,20" in content))

    # 题8
    tests.append(("题8", format_kwargs(name="小明", age="20") == ["age=20", "name=小明"]))

    # 题9
    f9 = os.path.join(tmpdir, "t9.txt")
    with open(f9, "w", encoding="utf-8") as f:
        f.write("Hello\nworld\nHELLO\n")
    tests.append(("题9", grep_lines(f9, "hello") == ["Hello", "HELLO"]))

    # 题10
    f10 = os.path.join(tmpdir, "t10.csv")
    with open(f10, "w", encoding="utf-8", newline="") as f:
        f.write("name,score\n小明,85\n小红,92\n小刚,78\n")
    tests.append(("题10a", top_student(f10) == "小红"))
    tests.append(("题10b", top_student(os.path.join(tmpdir, "nope.csv")) == ""))

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
