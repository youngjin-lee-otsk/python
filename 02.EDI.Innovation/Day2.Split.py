msg = "life is short"
print(msg.split())
#Result : ['life','is','short']
print(msg.split()[2])
#Result : short

#응용편
#split은 javascript와 다르게 list 에서 쓰는 함수가 아니고 string 에 쓰는 함수이다.
#list를 string화해서 split 가능함 확인. list 자체를 split 하는 내장함수가 따로 있지 않을까?
example = ['apple', 'banana', 'watermelon']
print(str(example).replace('[', '').replace(']', '').split('b'))