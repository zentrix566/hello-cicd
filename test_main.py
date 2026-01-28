from main import add

print("--- 开始自动化测试 ---")

# 如果 add(1, 1) 的结果不是 2，程序会在这里“炸掉”并报错
assert add(1, 1) == 2, f"错误：期待结果为 2，但实际得到的是 {add(1,1)}"

print("--- 测试通过！ ---")
