# Day 04 - 类、异常处理与生成器

"""
说明：补全函数体，运行 `python day04_oop_error.py` 全绿即通过。
      今天进入新阶段：面向对象、异常处理、yield 生成器。
"""

import os, tempfile

# ============================================================
# 题1：定义一个类
# 写一个 Student 类，有 name 和 score 两个属性，以及一个 introduce 方法
# 返回 "我叫{name}，分数{score}"
# 例：s = Student("小明", 85); s.introduce() → "我叫小明，分数85"
# ============================================================
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def introduce(self):
        return "我叫%s，分数%d" % (self.name, self.score)
    # TODO
    pass


# ============================================================
# 题2：类方法
# 给 Student 类加一个 is_pass 方法，分数 >= 60 返回 True
# 例：Student("小明", 85).is_pass() → True
# ============================================================
    # TODO（接在题1的 class 定义里）
    def is_pass(self):
        if self.score >= 60:
            return True
        else:
            return False
    pass


# ============================================================
# 题3：try/except - 安全转整数
# 写一个函数，尝试把字符串转整数，转换失败返回 0
# 例：safe_int("123") → 123, safe_int("abc") → 0
# ============================================================
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return 0
        # TODO
    pass


# ============================================================
# 题4：try/except - 安全读文件
# 写一个函数，读取文件第一行。文件不存在返回空字符串 ""。
# 例：文件第一行是 "hello" → "hello"
# ============================================================
def read_first_line(filepath):
    try:
        with open(filepath,"r",encoding = "utf-8") as f:
            return f.readline().strip()
    except FileNotFoundError:
        return ""
    # TODO
    pass


# ============================================================
# 题5：生成器 yield
# 写一个生成器函数，每次 yield 下一个偶数，从 0 开始共 n 个
# 例：list(even_generator(5)) → [0, 2, 4, 6, 8]
# ============================================================
def even_generator(n):
    for i in range(0, n):
        yield i * 2
    # TODO：用 yield
    pass


# ============================================================
# 题6：集合运算
# 写一个函数，返回两个列表中都出现过的元素（交集），用集合实现
# 例：[1,2,3,4], [3,4,5,6] → [3,4] (顺序不限)
# ============================================================
def intersect(a, b):
    result = set(a)&set(b)
    return result
    # TODO：用 set
    pass


# ============================================================
# 题7：列表嵌套字典
# 输入一个学生列表 [{"name":..., "score":...}, ...]，返回平均分(保留1位小数)
# 例：[{"name":"a","score":80},{"name":"b","score":90}] → 85.0
# ============================================================
def avg_from_dicts(students):
    total = 0
    for i in students:
        score = i["score"] 
        total = total + score
    return round(total / len(students),1)
    # TODO
    pass


# ============================================================
# 题8：字符串分割解析
# 写一个函数，把 "name:score" 格式的字符串列表转成字典
# 例：["小明:85","小红:90"] → {"小明":85, "小红":90}
# ============================================================
def parse_pairs(pairs):
    result = {}
    for i in pairs:
        name, score = i.split(":")
        result[name] = int(score)
    return result
    # TODO：用 split(":")
    pass


# ============================================================
# 题9：enumerate + 条件
# 写一个函数，返回列表中大于均值的元素及其下标
# 例：[10, 20, 30, 40] → [(2,30), (3,40)]  # 均值25
# ============================================================
def above_average(nums):
    list = []
    for index,num in enumerate(nums):
        if num > sum(nums) /len(nums):
            list.append((index,num))
    return list
        
    # TODO
    pass


# ============================================================
# 题10：综合 - 读取成绩文件并统计
# 文件每行 "姓名,分数"，写一个函数返回 {"及格人数":n, "平均分":avg(1位小数)}
# 文件不存在返回 {"及格人数":0, "平均分":0.0}
# ============================================================
def score_stats(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        scores = []
        passed_count = 0
        
        for line in lines:
            line = line.strip()
            if line:  # 确保不是空行
                parts = line.split(",")
                if len(parts) == 2:
                    name, score_str = parts
                    score = int(score_str)
                    scores.append(score)
                    if score >= 60:
                        passed_count += 1
        
        if len(scores) == 0:
            average_score = 0.0
        else:
            average_score = round(sum(scores) / len(scores), 1)
            
        return {
            "及格人数": passed_count,
            "平均分": average_score
        }
    except FileNotFoundError:
        return {"及格人数": 0, "平均分": 0.0}
    # TODO：用 split(",")、try/except
    pass


# ============================================================
# 测试代码 - 不动
# ============================================================
if __name__ == "__main__":
    tests = []
    tmpdir = tempfile.mkdtemp()

    # 题1 & 题2
    s = Student("小明", 85)
    tests.append(("题1", s.introduce() == "我叫小明，分数85"))
    tests.append(("题2a", s.is_pass() == True))
    tests.append(("题2b", Student("小红", 55).is_pass() == False))

    # 题3
    tests.append(("题3a", safe_int("123") == 123))
    tests.append(("题3b", safe_int("abc") == 0))
    tests.append(("题3c", safe_int("") == 0))

    # 题4
    f4 = os.path.join(tmpdir, "t4.txt")
    with open(f4, "w", encoding="utf-8") as f:
        f.write("hello\nworld")
    tests.append(("题4a", read_first_line(f4) == "hello"))
    tests.append(("题4b", read_first_line(os.path.join(tmpdir, "nope.txt")) == ""))

    # 题5
    tests.append(("题5", list(even_generator(5)) == [0, 2, 4, 6, 8]))

    # 题6
    result = intersect([1, 2, 3, 4], [3, 4, 5, 6])
    tests.append(("题6", set(result) == {3, 4}))

    # 题7
    tests.append(("题7", avg_from_dicts([{"name": "a", "score": 80}, {"name": "b", "score": 90}]) == 85.0))

    # 题8
    tests.append(("题8", parse_pairs(["小明:85", "小红:90"]) == {"小明": 85, "小红": 90}))

    # 题9
    tests.append(("题9", above_average([10, 20, 30, 40]) == [(2, 30), (3, 40)]))

    # 题10
    f10 = os.path.join(tmpdir, "t10.txt")
    with open(f10, "w", encoding="utf-8") as f:
        f.write("小明,85\n小红,55\n小刚,92\n")
    result = score_stats(f10)
    tests.append(("题10a", result["及格人数"] == 2))
    tests.append(("题10b", result["平均分"] == 77.3))
    tests.append(("题10c", score_stats(os.path.join(tmpdir, "nope.txt")) == {"及格人数": 0, "平均分": 0.0}))

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
