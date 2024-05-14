import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

# Firebase 프로젝트의 서비스 계정 키 경로
cred = credentials.Certificate("C:\\Users\\minta\\Downloads\\teampj-86c76-firebase-adminsdk-rm0t6-ac8c745bc7.json")

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://teampj-86c76-default-rtdb.firebaseio.com'
})

# 데이터베이스 레퍼런스
ref = db.reference('medi')  # 'medi' 노드에 데이터 추가

# 새 데이터 추가
new_data = {
    'name': '0.45%엔에이시엘.케이20주',
    'effect': '탈수증, 수술전후 등의 수분ㆍ전해질 보급',
    'storage': ' 실온보관',
    'precautions': ' 과민반응의 징후 또는 증상이 발생 시 즉시 주입을 중단',
    'side_effect': '발열, 주사부위의 감염, 정맥혈전증, 정맥염, 혈관밖유출, 과다혈량'
}

# 현재 시간을 기반으로 고유한 ID 생성
new_id = str(int(time.time() * 1000))

# 데이터베이스에 값 추가
ref.child(new_id).set(new_data)

print("Data added to Firebase database with auto-generated ID:", new_id)


# myenv\Scripts\activate
# python data.py

#디비에 약 데이터 넣음