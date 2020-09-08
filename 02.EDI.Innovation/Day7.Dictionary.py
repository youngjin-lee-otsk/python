#Dictionary, List, tuple과 마찬가지로 여러개의 값을 다룬다.
#Dictionary는 관련된 값을 모아놓는다.
#{key1: val1, ket2: val2, ...}
#각 값에 이름을 붙힌다고 볼 수 있다.

my_dic = {} #print(type(my_dic)) #<class 'dict'>
my_dic[0] = 'a' #key에 값을 담는다.
#print(my_dic) #{0: 'a'}
my_dic['b'] = 2
#print(my_dic) #{0: 'a', 'b': 2}
my_dic['학생1'] = '이제열'
#print(my_dic)
my_dic['학생2'] = '정상원'
#print(my_dic)
my_dic['학생3'] = '정성현'
#print(my_dic) #{0: 'a', 'b': 2, '학생1': '이제열', '학생2': '정상원', '학생3': '정성현'}
#값을 가져오는 방법.
print(my_dic['학생3']) #학생3 찾기., 정성현
#불필요한 값을 del을 이용해 제거할 수 있음.
del  my_dic[0] #0: 'a' 찾아 지우기.
#print(my_dic) #{'b': 2, '학생1': '이제열', '학생2': '정상원', '학생3': '정성현'}
del  my_dic['b'] #b: '2' 찾아 지우기.
#print(my_dic) #{'학생1': '이제열', '학생2': '정상원', '학생3': '정성현'}

#dictionary의 method.
#함수와 method의 차이) method는 Dictionary만 사용할 수 있는 함수.
#dict.values() 값만 뽑아 온다.
print(my_dic)
for std in my_dic.values():
    print(std)
    #이제열, 정상원, 정성현 출력됨.

#dict.keys() 키만 뽑아 온다.
for key in my_dic.keys():
    print(key)
    #학생1, 학생2, 학생3이 출력됨.

#dict.items() 키와 값만 뽑아 온다.
for key, val in my_dic.items():
    print(key, val)
    #학생1 이제열 , 학생2 정상원 , 학생3 정성현이 출력됨.