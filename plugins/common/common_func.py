def get_sftp():
    print("SFTP 작업을 시작합니다.") 
    
def regist(name, sex, *args):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {args}')
    
def regist_kwargs(**kwargs):
    # Airflow가 넣어준 수많은 정보 중 내가 보낸 것만 꺼냅니다.
    # 인자가 없을 경우를 대비해 기본값(None)을 설정하면 안전합니다.
    name = kwargs.get("name", "이름없음")
    sex = kwargs.get("sex", "알수없음")
    
    # 전달받은 특정 옵션들만 리스트로 묶고 싶다면 직접 지정하세요.
    options = [kwargs.get("option1"), kwargs.get("option2")]

    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션들: {options}')