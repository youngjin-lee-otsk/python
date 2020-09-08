#여러개의 값을 한곳에 모아놓으 수 있는 것.
#여러개의 변수를 손쉽게 관리할 수 있음., 같은 값이든 다른 값이든 상관 없음.
#그리고 변경도 가능함. 값을 변경하는 immutable, mutable이라는 용어가 있음.
#immutable : 값 변경 불가. / mutable : 값 변경 가능. list는 mutable.
#[a1,a2,a3..]으로 표현됨.
my_list = [] #빈 리스트 작성.
print(type(my_list)) #list type출력.
my_list = [1,2,3] #빈 리스트 작성.
print(my_list)

names = ['ljy1','ljy2','ljy3'] #빈 리스트 작성.
print(names)
names.append('ljy4') #append() 로 추가 가능. append는 list에만 추가 가능
print(names)

#Indexing.
names.append('ljy5')
names.append('ljy6')
names.append('ljy6')
names.append('ljy9')
names.append('ljy8')
names.append('ljy7')
names.append('ljy7')
print(names) #['ljy1', 'ljy2', 'ljy3', 'ljy4', 'ljy5', 'ljy6', 'ljy7']
#names에서 ljy4를 출력
print(names[3]) #ljy4
#name 에서 ljy5를 제거하기.
del names[4] #del을사용하면 list에서 제거할 수 있음
print(names) #['ljy1', 'ljy2', 'ljy3', 'ljy4', 'ljy6', 'ljy7']
#slicing 여러개의 값 가져오기.
print(names[0:3]) #['ljy1', 'ljy2', 'ljy3']
print(names[1:3]) #ljy2~ljy3
#sort() 함수. 정렬가능.
names.sort() #문자와 숫자로 정렬 가능.
print(names)
#count() 함수.
print(names.count('ljy6')) #ljy6이 몇개인지 찾을 수 있음.
#그외에도 아주 많은 list관련 함수들이 있음.

#함수로 전체 갯수를 찾을 수 있음. 이것은 메소드가 아님.
#len() 파이썬에서 지원하는 기본 함수
print(len(names))
