#튜플(tuple)은 셀 수 있는 수량의 순서 있는 열거.
#리스트와 튜플의 차이에 대한 참고자료 : https://itholic.github.io/python-list-tuple/
#여러값을 모아서 저장. 대신 값을 변경할 수 없음.
#tuple은 immutable : 값 변경 불가.
#(a1,b1,c1) ()로 표현함.

#LIST
#여러개의 값을 한곳에 모아놓으 수 있는 것.
#여러개의 변수를 손쉽게 관리할 수 있음., 같은 값이든 다른 값이든 상관 없음.
#그리고 변경도 가능함. 값을 변경하는 immutable, mutable이라는 용어가 있음.
#immutable : 값 변경 불가. / mutable : 값 변경 가능. list는 mutable.
#[a1,a2,a3..]으로 표현됨.

world_name = 'yjLee'
print(world_name)

numbers = [1,2,3,4,5] ## array
odd_numbers = []
my_tuple = ('LEE','KIM','SON') ## tuple 배열과 다르게 값 변경 불가능

for number in numbers:
    divide = 2
    if number %divide == 1:
        odd_numbers.append(number)

print(odd_numbers)
print(my_tuple)

a1, a2, a3 = my_tuple ## packing / unpacking
print(a1, a2, a3)