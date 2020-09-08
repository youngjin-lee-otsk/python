#Module 다양한 모듈이 이미 존재하므로 불러서 사용하기만 하면됨.
#import라는 keywork를 사용하고 .(마침표)를 이용해 module을 사용할 수 잇다.
#random 모듈, 난수를 만들거나 무작위와 관련된 함수를 포함하고 있음
#random.choice() / list안에 있는 값중 한가지를 뽑아주는 것
import random #random 모듈을 사용하기 위해 선언한 것.
students = ['제열','상원','성현','인기','재운','정목','기택']
students.append('정은')
students.append('영진')
students.append('재원')
students.append('태현')
print(random.choice(students)) #임의의 대상이 출력됨.

#random.sample() / #임의의 대상 둘을 뽑아주는 함수. 
print(random.sample(students, 2)) #임의의 대상 2개가 출력됨.
print(random.sample(students, 4)) #임의의 대상 4개가 출력됨.
print(random.sample(range(1, 46), 6)) #1~46중 임의의 숫자 6개 뽑기

#random.randint() / 숫자의 범위를 지정해서 그중 한가지를 선택하는 함수.
print(random.randint(8, 10)) #8~10 사이의 값중 하나가 정수로 출력됨.
