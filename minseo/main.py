import qrcode
import tkinter as tk
from tkinter import messagebox
from firebase_admin import credentials, db
from medi import get_id_from_name
import time
from createUser import createuser

cred_path = "C:\\Users\\minta\\Downloads\\teampj-86c76-firebase-adminsdk-rm0t6-ac8c745bc7.json"
ref1 = db.reference('user_medi')
ref2 = db.reference('user')
user_id = createuser()

def create_frame(root, row):
    frame = tk.Frame(root)
    frame.grid(row=row, column=0, columnspan=2, pady=5)
    return frame

def create_label(frame, text, row):
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=0, padx=10, pady=5)
    return label

def create_entry(frame, row):
    entry = tk.Entry(frame)
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

def create_button(frame, text, command, row):
    button = tk.Button(frame, text=text, command=command)
    button.grid(row=row, column=0, columnspan=2, pady=5)
    return button

def add_medicine():
    num = int(entry_num.get())
    entries = []
    for _ in range(num):
        frame = create_frame(root, 3 + _ + 1)
        create_label(frame, "약 이름:", 0)
        entry_name = create_entry(frame, 0)
        create_label(frame, "복용법:", 1)
        entry_take = create_entry(frame, 1)
        entries.append((entry_name, entry_take))
    create_button(root, "저장", lambda: save_medicines(entries, user_id), 3 + num + 1)

def save_medicines(entries, user_id):
    for entry_name, entry_take in entries:
        name = entry_name.get()
        take = entry_take.get()
        medi_id = get_id_from_name(name)
        if medi_id:
            new_data = {'take': take, 'medi_id': medi_id, 'user_id': user_id}
            new_id = str(int(time.time() * 1000))
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

root = tk.Tk()
root.title("Medicine Input Form")

create_label(root, "약 개수:", 0)
entry_num = create_entry(root, 0)
create_button(root, "입력 완료", add_medicine, 1)
create_button(root, "Generate QR Code", generate_qr_code, 2)

root.mainloop()