#Operator #Assing 할당 연산자 , = += -= *= /= 등...
#왼쪽에 변수 오른쪽에 값.
#= 오른쪽의 값을 왼쪽에 할당한 다는 의미. , == 같다는 의미로 사용.
#파이썬 튜터 사이트가 있음., 실제동작하는 것을 확인할 수 있다.
my_int = 1 #=이 할당 연산자. int 1로 메모리에 저장됨.
my_float = 2.0 #float 2.0
my_list = [] #empty list
#위의 그림에서 오른쪽의 값을 보기 좋게 하기 위하여 변수에 담는다.
"""
#+= , 복합 할당 연산자.
count = count + 1 
#print(count) #2
count = count + 1 
#print(count) #3
#복합할당 연산자.
count += 1 #count = count + 1 을 줄여서 표현
print(count)
count -= 1
print(count)
"""
"""
#산술 연산자 , + - * /
print(3 + 3) #6
print(6 * 2) #12
print(12 / 3) #4.0
"""
"""
#특수 연산자 , ** // %
#**는 제곱, //는 나누었을때의 몫, %는 나머지를 의미.
print(3 ** 2) #3의 2제곱.
print(7 // 3 ) #7/3은 2.33333 -> 7//3을 하면 몫인 2만 남음.
print(7 % 3 ) #7/3에 대한 나머지 1이 출력됨.
"""
"""
#%연산자는 홀수 또는 짝수를 구할 때 사용될 수 있다.
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    #안에서 홀짝 구분하기.
    if number % 2 == 1:
        odd_number = number
        print(odd_number, "= odd_number")
    else:
        even_number = number
        print(even_number, "= even_number")
"""
"""
#String 문자열 연산자
#+ , *
#+는 문자열을 합치는 역할을 한다.
print('이제열' + 'X' + '파이썬') #이제열X파이썬
print('안녕하세요' + ' ' + '반갑습니다.') #안녕하세요 반갑습니다.
#문자열에 *를 붙히면 문자 반복이 가능하다.
print('안녕'*5) #안녕안녕안녕안녕안녕
print('안녕 '*5) #안녕 안녕 안녕 안녕 안녕
"""
"""
#함수로 만들어서 문자열을 다룰때 사용하기도 한다.
def cls():
    print('\n'*100) #enter를 100번한것을 의미.
cls() #실행 enter를 10번 실행하게끔 하는 것.
"""
"""
#비교연산자. Comparison
#== , != , > , < , >= , <=
#같다, 다르다, 크다, 작다, 크거나 작다, 작거나 크다.
1 < 2 #true
2 < 1 #false
1 != 1 #false
1 == 1 #true
4 <= 6 #true
5 >= 5 #true
"""
"""
#Logical 논리 연산자.
#and , or , not
print(True) #True
print(False) #False
print(True and True) #True
print(True and False) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or False) #False
print(not True) #False
print(not False) #True
"""
"""
#논리 연산자를 이용한 조건 확인.
#Ex1
height = 12
age = 8
print(height > 140 and age > 10) #False
#Ex2
height = 190
age = 9
print(height > 140 and age > 10) #False
#Ex3
height = 150
age = 32
print(height > 140 and age > 10) #True
"""
"""
#Membership 리스트들 안에 값이 존재하는지 여부를 확인하는 것
#in , not in
이제열과_EMP팀원들 = ['이제열','이기택','정상원','정선현','최정목','손인기','김재운']
print(이제열과_EMP팀원들)
print('이제열' in 이제열과_EMP팀원들) #True
print('이제열' not in 이제열과_EMP팀원들) #False
print('홍태화' in 이제열과_EMP팀원들) #False
이제열과_EMP팀원들.append('홍태화') #추가.
print('홍태화' in 이제열과_EMP팀원들) #True
"""
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = [number for number in numbers if number % 2 ==1]
even_numbers = [number for number in numbers if number % 2 ==0]
print(odd_numbers, even_numbers)
"""

#숙제
oddeven_numbers = [('odd_nubers',number) if number%2 == 1 else ('even_nubers', number) for number in range(1,10)]
print(oddeven_numbers)
