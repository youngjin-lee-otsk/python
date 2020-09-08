#반복적으로 사용되는 것들을 이름을 붙혀서 만들어 사용하는 것.
#내장함수, 모듈의 함수, 사용자 정의 함수.
"""
def 함수이름 (인자1,...): #매개변수라고도 함.
    실행할 명령1
    실행할 명령2

    return 결과 #있을수도 없을수도 있다.
"""
#Why Function?
#재사용., 코드관리가 쉬워진다.

def add(num1, num2):
    return num1 + num2
print(add(1,2)) #결과 값은 3 add function을 실행한 것.

#값 어려개를 돌려 받기.
"""
def 함수이름 (인자1,...): #매개변수라고도 함.
    실행할 명령1
    실행할 명령2

    return 결과1, 결과2, ..
"""
def add_mul(num1, num2):
    return num1 + num2, num1 * num2
print(add_mul(1,2)) #결과 값은 (3, 2) 소괄로가 있으면 튜플을 의미.
"""
>> 두개의 값을 각각 return하는 개념이 아니라
return값을 packing해서 한개의 튜플 값으로 return한 것이다.
"""
#packing해서 튜플로 리턴된 값을 unpacking해서 출력.
my_add, my_mul = add_mul(1,2)
print(my_add) #3 , unpacking해서 돌려준다.
print(my_mul) #2 , unpacking해서 돌려준다.