#튜플(tuple)은 셀 수 있는 수량의 순서 있는 열거.
#리스트와 튜플의 차이에 대한 참고자료 : https://itholic.github.io/python-list-tuple/
#여러값을 모아서 저장. 대신 값을 변경할 수 없음.
#tuple은 immutable : 값 변경 불가.
#(a1,b1,c1) ()로 표현함.
my_tuple = (1,2,3)
print(type(my_tuple))
print(my_tuple)
#괄호 없이 값만 입력해도 가능.
#packing, unpacking.
my_tuple = 1,2,3 #1,2,3을 튜플로 묶어서 한꺼번에 저장. 이것이 패킹.
num1, num2, num3 = my_tuple #num1 ~ num3에 1~3을 저장. 이것이 언패킹
print(num1, num2, num3)
#num1 = 2, num2 =1을 넣고 싶을때 어떻게?
num1, num2 = num2, num1 #num2, num1 패킹이 num1, num2로 언패킹됨.
print(num1, num2, num3)

"""
#packing
my_tuple2 = (1,2,3)
my_tuple2 = 1,2,3

print(my_tuple2)
a1, a2, a3 = my_tuple2 #unpaking하겠다.
print(a1, a2, a3)
print(a1)
print(a2)
print(a3)

a1, a2, a3 = a2, a3, a1
print(a1, a2, a3)
print(a1)
print(a2)
print(a3)

a1, a2, a3 = a2, a3, 9
print(a1, a2, a3)
"""