#if 조건. , if, else, elif
"""
조건이 true이냐 false이냐를 체크.
if 조건:
    #True일때 코드 블락 수행.
    실행할 명령1
    실행할 명령2
#false일때 코드 블락을 빠져나온다.
"""
"""
조건이 true이냐 false이냐를 체크.
if 조건:
    실행할 명령1
    실행할 명령2
elif 조건:
    실행할 명령1
    실행할 명령2
else:
    실행할 명령1
"""
input_name = '이제열'
if input_name == '이제열':
    print('만나서 반가워요,', input_name)
elif input_name == '이제열!':
    print('다시 만났군요,',input_name)
else:
    print('누구세요?',input_name)
