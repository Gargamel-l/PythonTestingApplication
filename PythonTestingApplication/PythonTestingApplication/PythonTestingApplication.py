import pymongo

import tkinter as tk
from pymongo import MongoClient

def insert_data():
    name = entry_name.get()
    age = entry_age.get()
    
    db.my_collection.insert_one({'name': name, 'age': age})
    status_label.config(text="Data inserted successfully")


# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Создание графического интерфейса с использованием Tkinter
root = tk.Tk()
root.title("MongoDB GUI")

# Создание и размещение элементов управления
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=2, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=3, columnspan=2)

root.mainloop()
