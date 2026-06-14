# Day 01 - Python 基础语法复习

"""
说明：每题是一个独立的函数，补全函数体使其通过测试。
      写完运行 `python day01_basics.py`，终端显示"全部通过"即为完成。
      建议：先用自己思路写，写不动再用 Codex 帮忙，但最终要能自己讲清楚每行在干什么。
"""

# ============================================================
# 题1：变量与类型
# 写一个函数，接收姓名、年龄、身高（米），返回一句话介绍
# ============================================================
def introduce(name, age, height):
    return f"{name}今年{age}岁，身高{height}米"
    # TODO: 返回 f"{name}今年{age}岁，身高{height}米"
    pass


# ============================================================
# 题2：字符串操作
# 写一个函数，判断一个字符串是否是回文（正反读一样，忽略大小写）
# 例："Racecar" -> True, "hello" -> False
# ============================================================
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
    # TODO
    pass
# ============================================================
# 题3：列表操作
# 写一个函数，接收一个数字列表，返回 [最大值, 最小值, 平均值(保留2位小数)]
# 例：[3,1,4,1,5,9] -> [9, 1, 4.67]
# 要求：使用循环，不用max()/min()
# ============================================================
def list_stats(numbers):
    max_val = numbers[0]
    min_val = numbers[0]
    total = 0
    for n in numbers:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
        total += n
    avg = round(total / len(numbers), 2)
    return [max_val, min_val, avg]
    # TODO
    pass
# ============================================================
# 题4：字典操作
# 写一个函数，统计字符串中每个字符出现的次数，返回字典
# 例："hello" -> {"h":1, "e":1, "l":2, "o":1}
# ============================================================
def char_count(s):
    result = {}
    for a in s:
        if a in result:
            result[a] += 1
        else:
            result[a] = 1
    return result
 # TODO
    pass


# ============================================================
# 题5：条件判断
# 写一个函数，输入分数(0-100)，返回等级:
#   90-100: "A", 80-89: "B", 70-79: "C", 60-69: "D", 0-59: "F"
# ============================================================
def grade(score):
    if 100 >= score >= 90:
        return "A"
    elif 89 >= score >=80 :
        return "B"
    elif 79 >= score >=70 :
        return "C"
    elif 69 >= score >=60 :
        return "D"
    else:
        return "F"
            
    # TODO
    pass
   


# ============================================================
# 题6：循环
# 写一个函数，打印九九乘法表的前 n 行，以字符串列表返回（每行一个字符串）
# 例：n=3 -> ["1×1=1", "2×1=2 2×2=4", "3×1=3 3×2=6 3×3=9"]
# ============================================================
def multiplication_table(n):
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(f"{i}×{j}={i * j}")
        result.append(" ".join(row))
    return result
    # TODO
    pass
# ============================================================
# 题7：函数与参数
# 写一个函数，计算任意个数字的乘积
# 例：product(1,2,3,4) -> 24, product() -> 1 (空参数返回1)
# ============================================================
def product(*args):
    result = 1
    for i in args:
        result = result * i

    return result

    # TODO
    pass


# ============================================================
# 题8：列表推导式
# 写一个函数，返回 1 到 n 中所有能被 3 或 5 整除的数
# 要求：用列表推导式
# 例：n=10 -> [3,5,6,9,10]
# ============================================================
def divisible_by_3_or_5(n):
    result = [i for i in range(1,n+1) if i % 3 == 0 or i % 5 ==0 ]
    return result
    # TODO
    pass


# ============================================================
# 题9：集合
# 写一个函数，接收两个列表，返回它们的交集（去重后的列表）
# 例：[1,2,2,3], [2,3,4] -> [2,3]（顺序不限）
# ============================================================
def common_elements(a, b):
    result = []
    for i in a:
        if i  in b and i not in result:
            result.append(i)
    return result

        


    # TODO
    pass


# ============================================================
# 题10：综合
# 写一个函数，接收一个英文句子，返回出现次数最多的单词（忽略大小写和标点）
# 例："Hello world, hello Python world" -> "hello"
# 提示：用 str.split(), str.strip(",.") 清理标点
# ============================================================
def most_frequent_word(sentence):
    sentence = sentence.lower()
    import string
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    words = sentence.split()
    count_word = {}
    for word in words:
        count_word[word] = count_word.get(word, 0) + 1
    max_count = 0
    most_word = ""
    for word, count in count_word.items():
        if count > max_count:
            max_count = count
            most_word = word
    return most_word
    # TODO
    pass
# ============================================================
# 测试代码 - 不用动
# ============================================================
if __name__ == "__main__":
    tests = []

    # 题1
    result = introduce("小明", 20, 1.75)
    tests.append(("题1", result == "小明今年20岁，身高1.75米"))

    # 题2
    tests.append(("题2a", is_palindrome("Racecar") == True))
    tests.append(("题2b", is_palindrome("hello") == False))
    tests.append(("题2c", is_palindrome("Aba") == True))

    # 题3
    result = list_stats([3, 1, 4, 1, 5, 9])
    tests.append(("题3", result == [9, 1, 3.83]))

    # 题4
    tests.append(("题4", char_count("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}))

    # 题5
    tests.append(("题5a", grade(95) == "A"))
    tests.append(("题5b", grade(82) == "B"))
    tests.append(("题5c", grade(55) == "F"))

    # 题6
    tests.append(("题6", multiplication_table(3) == ["1×1=1", "2×1=2 2×2=4", "3×1=3 3×2=6 3×3=9"]))

    # 题7
    tests.append(("题7a", product(1, 2, 3, 4) == 24))
    tests.append(("题7b", product() == 1))

    # 题8
    tests.append(("题8", divisible_by_3_or_5(10) == [3, 5, 6, 9, 10]))

    # 题9
    result = common_elements([1, 2, 2, 3], [2, 3, 4])
    tests.append(("题9", set(result) == {2, 3}))

    # 题10
    tests.append(("题10", most_frequent_word("Hello world, hello Python world") == "hello"))

    # 出结果
    all_pass = True
    for name, passed in tests:
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_pass = False
        print(f"[{status}] {name}")

    print("\n==========")
    if all_pass:
        print("OK 全部通过！可以提交了。")
    else:
        print("X 有未通过的题目，继续加油！")
