from main import add

# 注意：函数名必须以 test_ 开头
def test_answer():
    print("正在验证 1+1 是否等于 2...")
    assert add(1, 1) == 2
