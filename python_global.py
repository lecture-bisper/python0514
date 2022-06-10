print("-" * 5, "전역 변수 사용하기", "-" * 5)

g_value = 100
g_value2 = 200

print("변수 g_value의 값 확인 : {0}".format(g_value))


def func1():
    val1 = 10
    print("func1 함수의 지역 변수 val1의 값 : {0}".format(val1))


def func2():
    print("func2 함수의 전역 변수 g_value의 값 : {0}".format(g_value))


def func3():
    g_value = 1000
    val2 = 20
    print("func3 함수의 지역 변수 val2의 값 : {0}".format(val2))
    print("func3 함수의 전역 변수 g_value의 값 : {0}".format(g_value))


def func4():
    global g_value
    g_value = 2000
    print("func4 함수의 전역 변수 g_value의 값 : {0}".format(g_value))


print("함수 밖에서 전역 변수 g_value의 값 : {0}".format(g_value))

func1()
func2()
func3()

print("함수 밖에서 전역 변수 g_value의 값 : {0}".format(g_value))
# print("함수 밖에서 func3 함수의 지역 변수 val2의 값 : {0}".format(val2))

func4()
print("함수 밖에서 전역 변수 g_value의 값 : {0}".format(g_value))

