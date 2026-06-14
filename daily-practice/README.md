# 每日练习工作流

## 目录结构
```
C:\Users\迪迦\Documents\Codex\python-ai-practice\
  daily-practice/     ← 每日 Python 练习题
  docs/               ← 路线图、比赛方案等文档
  projects/           ← 未来比赛项目、个人作品
```

## 每日流程

### 写代码
打开当天的题目文件，补全函数体：
```
daily-practice\day01_basics.py
```

### 运行测试
```bash
cd C:\Users\迪迦\Documents\Codex\python-ai-practice
python daily-practice\day01_basics.py
```

### 全部通过 → 提交到 GitHub
```bash
cd C:\Users\迪迦\Documents\Codex\python-ai-practice
git add daily-practice/day01_basics.py
git commit -m "day01: Python基础语法复习"
git push
```

## GitHub 配置（一次）

1. 浏览器打开 https://github.com/new
2. Repository name: `python-ai-practice`
3. 选 Private，不要勾选任何初始化选项
4. 创建后执行：
```bash
cd C:\Users\迪迦\Documents\Codex\python-ai-practice
git remote add origin https://github.com/YOUR_USERNAME/python-ai-practice.git
git branch -M main
git push -u origin main
```

## Tips
- 写不动用 Codex 帮忙，但最终要能自己讲清楚
- 每天 30-45 分钟
- 遇到卡住的题，直接贴代码给我
