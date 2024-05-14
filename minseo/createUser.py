import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time

# Firebase 프로젝트의 서비스 계정 키 경로
cred = credentials.Certificate("C:\\Users\\minta\\Downloads\\teampj-86c76-firebase-adminsdk-rm0t6-ac8c745bc7.json")


# 데이터베이스 레퍼런스
ref = db.reference('user')  # 'user' 노드에 데이터 추가

def createuser():
    new_id = str(int(time.time() * 1000))

    new_data = {
        'id': new_id
    }

    # 데이터베이스에 값 추가
    ref.push().set(new_data)
    return new_id

#유저 생성 (시간기반)