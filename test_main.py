from main import add

def test_add():
    # 这就是测试逻辑：如果 add(1, 1) 不等于 2，就会报错
    assert add(1, 1) == 2
    print("测试通过！")
