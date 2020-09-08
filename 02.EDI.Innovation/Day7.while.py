#Loop 반복문
#While, if와 조건문 작성 법이 같음.
#while조건문이 만족을 하면 명령1~2를 반복적으로 수행함., false가 되면 구문 밖으로 나온다.
"""
while 조건:
    실행할 명령1
    실행할 명령2
"""
"""
count = 0
while count < 3:
    print('횟수:',count)
    count += 1 #만약 이구간을 빠뜨리면 무한반복 문제가 발생함. 주의!!
#0~2까지 출력됨. 횟수:0,횟수:1,횟수:2
"""
#continue, break
#continue를 만나면 그 아래 수행문을 더이상 수행하지 않고 다시 처음 부터 수행.
#break를 만나면 while문 밖으로 빠져 나온다.

count = 0
while count < 10:
    count += 1
    if count < 4:
        continue #이 조건 아래로는 수행 하지 않는다. 그러므로 아래 print를 수행하지 않는다.
    print('횟수:',count)
    if count == 8:
        break #8을 만족하는 순간 while문을 빠져나온다.
#4~8까지만 출력됨. 횟수:4, ~ ,횟수:8
