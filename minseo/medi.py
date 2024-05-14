import firebase_admin
from firebase_admin import credentials, db

# Firebase 프로젝트의 서비스 계정 키 경로
cred = credentials.Certificate("C:\\Users\\minta\\Downloads\\teampj-86c76-firebase-adminsdk-rm0t6-ac8c745bc7.json")

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://teampj-86c76-default-rtdb.firebaseio.com'
})

# RTDB 레퍼런스 생성
ref = db.reference('medi')


def get_id_from_name(name):
    # 'medi' 경로의 모든 데이터 가져오기
    data = ref.get()

    # 데이터 반복하여 name이 포함된 id 찾기
    for key, value in data.items():
        if 'name' in value and name in value['name']:
            return key

    # 일치하는 name을 찾지 못한 경우 None 반환
    return None

#약 코드 가져오는