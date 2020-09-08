#for
#반복문., 파이썬에서는 2가지 반복 문법이있음. for와 while
"""
for 변수 in 컨테이너:
     실행할 명령1
     실행할 명령2
"""
#예) 컨테이너 [1,2,3]인 경우 첫번째부터 변수에 들어가면 명령1, 2실행후 같이 동작을 반복한다.
#반복할 실행 명령을 코드블럭이라고 한다. 이 부분을 :과 띄어씌기(4개)로 구분한다.
#While, if, def 등 모든 언어에 들여쓰기를 해줘야 한다.
#띄어쓰기 를 2칸, 4칸, tab 이런식으로 구분할 수 없다. 반드시 동일한 기준으로 코드를 작성해야 한다.
animals = ['캥거루','코알라','원숭이','강아지','고양이']
for animal in animals:
    print(animal)

#아래와 같이 컨테이너 바로 설정할 수 있다.
for num in [1,2,3]:
    print(num)

#스트링을 입력 글자수 만큼 출력된다.
for my_str in "이제열의 파이썬 기초 강의":
    print(my_str)

#range()
#범위를 설정하여 큰 단위의 숫자 범위를 쉽게 처리할 수 있다.
for n in range(0,3):
    print(n) #0~2까지 출력.
for n in range(0,100):
    print(n) #0~99까지 출력.
print(range(3)) #range(0, 3)로 인식 된다.

#다중 for 문. for x 2 중첩 반복문.
"""
for num in range(5):
    print(num)
for int in range(1,10):
    print(int)
"""
#구구단. 2단.
for int in range(1,10):
    print('{}x{}={}'.format(2,int,2*int))

#구구단. 2단 ~ 9단. if 문으로 짝수단의 9단만 출력하기
for int1 in range(2,10):
    if int1 % 2 == 0:
        for int2 in range(1,10):
            if int2 == 9:
                print('{}x{}={}'.format(int1,int2,int1*int2))

#Comprehension
#어렵지만 자주 쓰인다. 소스를 한줄로 표현하는 방법.
#예) 홀수만 뽑아서 담기.
#참고자료 : https://wikidocs.net/22805
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []
for number in numbers:
    if number % 2 == 1: #2로 나눴을때 나머지가 1이란 의미.
        odd_numbers.append(number)
print(odd_numbers)

#위의 소스를 아래와 같이 표현할 수 있다. 그것이 Comprehension이다.
#print([number for number in numbers if number % 2 ==1])
odd_numbers = [number for number in numbers if number % 2 ==1]
print(odd_numbers)

#응용편 화살표 함수처럼 포문이랑 if 절을 약식으로 표현하는 걸로 보임
members = ['제열1', '영진2', '정은1', '인기2']
odd_strings = [person for person in members if str(person).__contains__('2')]
print(odd_strings)
#과제 : 숫자를 입력받아서 정렬하는 프로그램 작성.
