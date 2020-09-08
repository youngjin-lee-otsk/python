#정수, 실수 등을 표현할 수 있다.
#1,2,3 정수형 자료 / 1.2, 3.2 실수형 자료
#모두 변수로 담을 수 있다.
my_float = 3.14
my_int = 3
#type을 이용하여 변수의 타입을 알 수 있다.
type(my_float)
print(type(my_float))
type(my_int)
print(type(my_int))
#numeric 숫자형이며, 1 + 2를 넣을 경우 자동으로 3으로 계산됨.
#string 문자형, '또는 "로 감싸서 표현할 수 있음.
string = 'str입니다.'
type(string)
print(type(string))

#블린 자료형 True, False가 있으면 모두 예약어.
my_biil_t = True
print(my_biil_t)
my_biil_f = False
print(my_biil_f)

#List 여러가지 타입을 모어서 표현할 수 있는 것.
#[]를 사용하며, [1,2,3] 이런식으로 작성함. 숫자, 문자 모두 가능
my_list = [1,2,3]
print(my_list)
students = ['이제열1','이제열2','이제열3']
print(students[0]) #이제열1
students.append('이제열4')
print(students)
print(students[2])
students[2] = '이제열5'
print(students)
for std in students:
  print('for :'+std)

#Dictionary #{Key:Value} 형태로 구성되어 있음
my_dict = {'이제열1':'남1', '이제열2':'남2'}
my_dict2 = {'이제열3':'남3'}
print(my_dict['이제열1']) #남1이 출력됨.
print(my_dict2['이제열3']) #남1이 출력됨.

my_int1 = 1
print(type(my_int1)) #int로 인식.
float(my_int1)
print(float(my_int1)) #1.0
print(type(str(my_int1))) #str로 인식

my_coding = 'CODING'
print(list(my_coding)) #['C', 'O', 'D', 'I', 'N', 'G'] list형태로 자료 구조가 변경됨.