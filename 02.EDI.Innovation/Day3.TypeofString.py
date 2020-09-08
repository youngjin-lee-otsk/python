##섹션 6.주석
#comment로 #을 입력하여 주석처리한다.
print('Hello Workld!') #안녕을 출력합니다.
#섹션 7. 문자열
my_str1 = "내가족1"
print(my_str1) # '와 "모두 가능
my_str2 = '내가족2'
print(my_str2) # '와 "모두 가능
my_str3 = """제스퍼
토미
메타"""
print(my_str3) #""" 세개를 쓰면 여러줄 입력이 가능하다.

#Formatting
# %연산자를 입력하여 숫자나 문자를 대입할 수 있다.
# %s
my_str = 'My name is %s' % 'Young Choi'
print(my_str)
#Young Choi문자열이 %s에 대입이 됨.
#%d
print('%d %d' % (1, 2))
#%f
print('%f' % 3.14)
#'{}'.format() 연산자.
#%보다 foramt을 더 많이 사용함.
print('My name is {}'.format('이제열')) #%s와 같은 의미
print('{} x {} = {}'.format(2,3,2*3)) #%d와 같은 의미
print('{1} x {0} = {2}'.format(2,3,2*3)) #순서를 지정하여 처리할 수 있음. 배열의 순서로 0~2를 위치시킬 수 있다.

#indexing 지정된 위치 한가지만 뽑아오는 것
#python의 012345 -> index 여기서 [2]는 t.
my_name = "이제열의 코딩"
print(my_name[5]) #코 출력. #0,1,2,3,4,5,6
# -주소도 사용 가능.
my_name = "이제열의 코딩" #-1, -2, -3, -4, -5, -6, -7 딩코 의열제이
print(my_name[-1]) #딩 출력.

#slicing 여러개를 뽑아오는 것.
#리스트를 자르는 것.
my_name = "이제열의 코딩" #0~6중 어디서 부터 [1:4] 어디까지
print(my_name[1:4]) #제열의 출력. 슬라이스 하는 것이므로 가운데 3자를 가져옴.
print(my_name[0:3]) #이제열 출력
#앞의 숫자와 뒷숫자를 제외할 수 있다. 만약 다 없다면 전체.
print(my_name[:3]) #이제열 출력.
print(my_name[3:]) #의 코딩 출력.
print(my_name[:]) #이제열의 코딩 출력.

#string.split() 메소드, 문자열을 공백 단위로 잘라줌.
#예제1
my_name = "이제열의 코딩"
print(my_name.split()) #['이제열의','코딩'] 출력.
my_list = my_name.split()
print(my_list[1]) #코딩 출력
# 예제2
fruit_str = '거봉 수박 포도 복숭아 망고 딸기 배 참외 찹쌀떡'
fruits = fruit_str.split()
print(fruits) #['거봉', '수박', '포도', '복숭아', '망고', '딸기', '배', '참외', '찹쌀떡']
print(fruits[5]) #딸기
print(fruits[1:5]) #['수박', '포도', '복숭아', '망고']

#Docstring, 문자열을 쓸 때 """을 주석으로 사용하는 것.
"""이렇게도 주석으로 사용할 수 있음""" #프로그램에 영향을 주지 않는다.

#print('', end='') #print함수에 옵션이 존재함. end = ''으로 출력의 끝을 지정할 수 있음.
print('집단 지성') #출력할 경우 기본으로 enter가 들어간다.
print('집단 지성', end='') #end를 아무것도 없게 지정하면 enter가 없어짐.
print('집단 지성', end='끝임.') #end를 아무것도 없게 지정하면 enter가 없어짐.

#Escape code # \n(줄바꿈) 와  \t(tab)으로 사용할 수 잇음
print('집단 지성\n테스트') #테스트가 줄바꿀 출력됨.
print('집단 지성\t테스트') #테스트앞에 탭 출력됨.
print('집단 지성\n테스트', end='\t다') #테스트가 줄바꿈 출력됨. 마지막에 탭과 다가 출력됨.

#한줄에 한 문장이 약속이지만 ;를 넣으면 한줄에 여러개의 문장을 입력할 수 있음.
print('집단 지성\n테스트2'); print('집단 지성\t테스트2'); print('집단 지성\n테스트', end='\t다2')
