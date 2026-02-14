def get_sftp():
    print("SFTP 작업을 시작합니다.") 
    
def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    
def regist_kwargs(**kwargs):
# 1. 값들만 리스트로 변환: list(kwargs.values())
    # 2. 첫 번째 이후부터 슬라이싱: [1:]
    other_options = list(kwargs.values())[1:]
    print(f'첫 번째 값(이름): {list(kwargs.values())[0]}')
    print(f'나머지 모든 값들: {other_options}')