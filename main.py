import qrcode
import tkinter as tk
from tkinter import messagebox
from firebase_admin import credentials, db
from medi import get_id_from_name
import time
from createUser import createuser

# Firebase 프로젝트의 서비스 계정 키 경로
cred_path = "C:\\Users\\minta\\Downloads\\teampj-86c76-firebase-adminsdk-rm0t6-ac8c745bc7.json"

# 데이터베이스 레퍼런스
ref1 = db.reference('user_medi')  # 'user_medi' 노드에 데이터 추가
ref2 = db.reference('user')  # 'user' 노드에 데이터 추가
user_id = createuser()

def add_medicine():
    num = int(entry_num.get())

    for _ in range(num):
        frame = tk.Frame(root)
        frame.grid(row=3 + _ + 1, column=0, columnspan=2, pady=5)

        label_name = tk.Label(frame, text="약 이름:")
        label_name.grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(frame)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        label_take = tk.Label(frame, text="복용법:")
        label_take.grid(row=1, column=0, padx=10, pady=5)
        entry_take = tk.Entry(frame)
        entry_take.grid(row=1, column=1, padx=10, pady=5)

        button_save = tk.Button(frame, text="저장",
                                command=lambda: save_medicine(entry_name.get(), entry_take.get(), user_id))
        button_save.grid(row=2, column=0, columnspan=2, pady=5)


def save_medicine(name, take, user_id):
    medi_id = get_id_from_name(name)
    if medi_id:
        new_data = {'take': take, 'medi_id': medi_id, 'user_id': user_id}
        new_id = str(int(time.time() * 1000))
        # 데이터베이스에 값 추가
        ref1.child(new_id).set(new_data)
        print("Data added to Firebase database with auto-generated ID:", new_id)
    else:
        print("약을 찾을 수 없습니다.")

def generate_qr_code():
    if user_id.strip() == "":
        messagebox.showerror("Error", "Please enter a new_id value")
        return

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(user_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"C:\\minseo\\teampj\\qrimg\\{user_id}.png"
    img.save(filename)
    messagebox.showinfo("Success", f"QR Code generated successfully and saved as {filename}")

def submit():
    add_medicine()

# Tkinter 창 생성
root = tk.Tk()
root.title("Medicine Input Form")

# 약 개수 입력
label_num = tk.Label(root, text="약 개수:")
label_num.grid(row=0, column=0, padx=10, pady=5)
entry_num = tk.Entry(root)
entry_num.grid(row=0, column=1, padx=10, pady=5)

# 입력 완료 버튼
button_submit = tk.Button(root, text="입력 완료", command=submit)
button_submit.grid(row=1, column=0, columnspan=2, pady=10)

button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
button_generate.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
