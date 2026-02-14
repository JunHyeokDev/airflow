def get_sftp():
    print("SFTP 작업을 시작합니다.") 
    
def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    
def regist_kwargs(**kwargs):
    # kwargs.values()를 리스트로 바꿔서 0번, 1번, 그리고 나머지[2:]로 분리
    vals = list(kwargs.values())
    
    name = vals[0]
    sex = vals[1]
    args = vals[2:] # 2번째 인덱스부터 끝까지 (리스트처럼 동작)

    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')