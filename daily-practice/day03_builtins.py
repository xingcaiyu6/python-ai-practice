# Day 03 - 内置函数与文件入门

"""
说明：补全函数体，运行 `python day03_builtins.py` 全绿即通过。
      今天覆盖 map/filter/lambda、递归、字典推导式、文件读写入门。
"""

import os
import tempfile

# ============================================================
# 题1：map + lambda
# 写一个函数，把列表中每个数平方，返回新列表。用 map 一行搞定。
# 例：[1,2,3] → [1,4,9]
# ============================================================
def square_all(nums):
    return list(map(lambda x: x ** 2, nums))
    # TODO：return list(map(lambda ...
    pass


# ============================================================
# 题2：filter + lambda
# 写一个函数，过滤列表中所有偶数。用 filter 一行搞定。
# 例：[1,2,3,4,5,6] → [2,4,6]
# ============================================================
def filter_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
    # TODO：return list(filter(lambda ...
    pass


# ============================================================
# 题3：sorted + key
# 写一个函数，按字符串长度排序（短→长），长度相同时按字母序
# 例：["dog","apple","cat","banana"] → ["cat","dog","apple","banana"]
# ============================================================
def sort_by_length(words):
    return sorted(words,key=lambda x:(len(x),x))

    # TODO：return sorted(..., key=lambda ...
    pass


# ============================================================
# 题4：递归
# 写一个递归函数，计算阶乘 n!。n>=0，0!=1。
# 例：factorial(5) → 120
# ============================================================
def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        s = n * factorial(n - 1)
        return s
    # TODO
    pass


# ============================================================
# 题5：字典推导式
# 写一个函数，输入一个列表，返回 {元素: 出现次数}，用字典推导式。
# 提示：用 set 去重，然后 {x: lst.count(x) for x in set(lst)}
# 例：[1,2,2,3,3,3] → {1:1, 2:2, 3:3}
# ============================================================
def count_dict(lst):
    return {x: lst.count(x) for x in set(lst)}
    # TODO
    pass


# ============================================================
# 题6：any / all
# 写一个函数，判断列表中是否所有元素都大于 0。
# 用 all() 一行。
# 例：[1,2,3] → True, [1,-2,3] → False
# ============================================================
def all_positive(nums):
    return all(x > 0 for x in nums)
    # TODO
    pass


# ============================================================
# 题7：zip 三个列表
# 写一个函数，把三个列表打包成元组列表，长度以最短的为准。
# 例：[1,2],[3,4],[5,6] → [(1,3,5),(2,4,6)]
# ============================================================
def zip_three(a, b, c):
    return list(zip(a, b, c))
    # TODO
    pass


# ============================================================
# 题8：文件读写 - 写
# 写一个函数，把字符串列表写入文件，每行一个。
# 例：write_file("test.txt", ["a","b"]) → 文件内容 a\nb
# ============================================================
def write_file(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    # TODO：用 with open(..., "w") as f
    pass


# ============================================================
# 题9：文件读写 - 读数字求和
# 写一个函数，读取文件（每行一个整数），返回总和。文件不存在返回 0。
# 例：文件内容 10\n20\n30 → 60
# ============================================================
def sum_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return sum(int(line.strip()) for line in f)
    except FileNotFoundError:
        return 0
    # TODO：用 try/except 处理文件不存在
    pass


# ============================================================
# 题10：综合 - 成绩筛选
# 写一个函数，输入 {"姓名":分数}，返回 60 分及以上的人名，按分数降序排列。
# 例：{"小明":85,"小红":55,"小刚":92,"小丽":60} → ["小刚","小明","小丽"]
# ============================================================
def passed_sorted(scores):
    passed_name = {name:score for name, score in scores.items() if score >= 60}
    return sorted(passed_name.keys(), key=lambda x: -passed_name[x])
    # TODO
    pass


# ============================================================
# 测试代码 - 不动
# ============================================================
if __name__ == "__main__":
    tests = []
    tmpdir = tempfile.mkdtemp()

    # 题1
    tests.append(("题1", square_all([1, 2, 3, 0]) == [1, 4, 9, 0]))

    # 题2
    tests.append(("题2", filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]))

    # 题3
    tests.append(("题3", sort_by_length(["dog", "apple", "cat", "banana"]) == ["cat", "dog", "apple", "banana"]))

    # 题4
    tests.append(("题4a", factorial(0) == 1))
    tests.append(("题4b", factorial(5) == 120))

    # 题5
    result = count_dict([1, 2, 2, 3, 3, 3])
    tests.append(("题5", result == {1: 1, 2: 2, 3: 3}))

    # 题6
    tests.append(("题6a", all_positive([1, 2, 3]) == True))
    tests.append(("题6b", all_positive([1, -2, 3]) == False))

    # 题7
    tests.append(("题7", zip_three([1, 2], [3, 4], [5, 6]) == [(1, 3, 5), (2, 4, 6)]))

    # 题8
    f8 = os.path.join(tmpdir, "t8.txt")
    write_file(f8, ["hello", "world"])
    with open(f8, "r", encoding="utf-8") as f:
        tests.append(("题8", f.read() == "hello\nworld\n"))

    # 题9
    f9 = os.path.join(tmpdir, "t9.txt")
    with open(f9, "w", encoding="utf-8") as f:
        f.write("10\n20\n30\n")
    tests.append(("题9a", sum_file(f9) == 60))
    tests.append(("题9b", sum_file(os.path.join(tmpdir, "nope.txt")) == 0))

    # 题10
    tests.append(("题10", passed_sorted({"小明": 85, "小红": 55, "小刚": 92, "小丽": 60}) == ["小刚", "小明", "小丽"]))

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
