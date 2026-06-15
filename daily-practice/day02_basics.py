# Day 02 - Python 基础巩固

"""
说明：每道题补全函数体，运行 `python day02_basics.py` 全绿即通过。
      今天的题全是基础——加深理解、减少盲区，不赶进度。
"""

# ============================================================
# 题1：字符串切片
# 写一个函数，返回字符串的后三位。不足3位返回原字符串。
# 例："abcdef" → "def", "ab" → "ab"
# ============================================================
def last_three(s):
    if len(s) <= 3:
        return s
    return s[-3:]
    # TODO
    pass


# ============================================================
# 题2：字符串方法
# 写一个函数，把字符串中所有空格替换为下划线，并转小写
# 例："Hello World Python" → "hello_world_python"
# ============================================================
def slugify(s):
    s = s.replace(" ", "_")
    s = s.lower()
    return s
    # TODO
    pass


# ============================================================
# 题3：列表切片
# 写一个函数，返回列表前一半的元素（向上取整）
# 例：[1,2,3,4,5] → [1,2,3]，[1,2,3,4] → [1,2]
# ============================================================
def first_half(lst):
    return lst[:(len(lst) + 1) // 2]



    # TODO
    pass


# ============================================================
# 题4：列表去重（保持顺序）
# 写一个函数，去掉列表中的重复元素，保持原顺序
# 例：[1,3,2,3,1,4] → [1,3,2,4]
# ============================================================
def dedupe_ordered(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

    # TODO
    pass


# ============================================================
# 题5：字典取值 + 默认值
# 写一个函数，从字典中取 key 对应的值，key 不存在返回默认值 0
# 例：get_or_zero({"a":1,"b":2}, "a") → 1, get_or_zero({"a":1}, "x") → 0
# ============================================================
def get_or_zero(d, key):
    if key in d:
        return d[key]
    else:
        return 0

    # TODO
    pass


# ============================================================
# 题6：enumerate 使用
# 写一个函数，返回列表中所有偶数下标的元素
# 例：[10,20,30,40,50] → [10,30,50]
# ============================================================
def even_index_items(lst):
    result = []
    for idx, item in enumerate(lst):
        if idx % 2 == 0:
            result.append(item)
    return result
            

    # TODO
    pass


# ============================================================
# 题7：zip 使用
# 写一个函数，把两个列表交错合并
# 例：[1,3,5], [2,4,6] → [1,2,3,4,5,6]
# ============================================================
def interleave(a, b):
    result = []
    zipp = zip(a, b)
    for i,j in zipp:
        result.append(i)
        result.append(j)
        
    
    return result


    # TODO
    pass


# ============================================================
# 题8：while 循环
# 写一个函数，用 while 循环计算一个正整数的各位数字之和
# 例：123 → 6, 999 → 27
# ============================================================
def digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
    # TODO
    pass


# ============================================================
# 题9：嵌套循环
# 写一个函数，生成一个 n×n 的乘法表（二维列表）
# 例：n=3 → [[1,2,3],[2,4,6],[3,6,9]]
# ============================================================
def multiplication_grid(n):
    result = []
    for i in range(1,n+1):
        row = []
        for j in range(1, n + 1):
            row.append(i*j)
        result.append(row)
    return result
    # TODO
    pass


# ============================================================
# 题10：综合 - 学生成绩统计
# 输入是一个字典 {学生名: [分数列表]}，返回一个新的字典 {学生名: 平均分(保留1位小数)}
# 例：{"小明":[85,90,78], "小红":[92,88]} → {"小明":84.3, "小红":90.0}
# ============================================================
def avg_scores(students):
    result = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        result[name] = round(avg, 1)
    return result
    # TODO
    pass


# ============================================================
# 测试代码 - 不动
# ============================================================
if __name__ == "__main__":
    tests = []

    tests.append(("题1a", last_three("abcdef") == "def"))
    tests.append(("题1b", last_three("ab") == "ab"))
    tests.append(("题1c", last_three("") == ""))

    tests.append(("题2", slugify("Hello World Python") == "hello_world_python"))

    tests.append(("题3a", first_half([1, 2, 3, 4, 5]) == [1, 2, 3]))
    tests.append(("题3b", first_half([1, 2, 3, 4]) == [1, 2]))

    tests.append(("题4", dedupe_ordered([1, 3, 2, 3, 1, 4]) == [1, 3, 2, 4]))

    tests.append(("题5a", get_or_zero({"a": 1, "b": 2}, "a") == 1))
    tests.append(("题5b", get_or_zero({"a": 1}, "x") == 0))

    tests.append(("题6", even_index_items([10, 20, 30, 40, 50]) == [10, 30, 50]))

    tests.append(("题7", interleave([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]))

    tests.append(("题8a", digit_sum(123) == 6))
    tests.append(("题8b", digit_sum(999) == 27))
    tests.append(("题8c", digit_sum(0) == 0))

    tests.append(("题9", multiplication_grid(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]))

    result = avg_scores({"小明": [85, 90, 78], "小红": [92, 88]})
    tests.append(("题10a", result["小明"] == 84.3))
    tests.append(("题10b", result["小红"] == 90.0))

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
