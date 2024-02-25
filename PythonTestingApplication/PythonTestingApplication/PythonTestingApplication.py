from genericpath import exists
import tkinter as tk
from pymongo import MongoClient


def insert_data():
    name = entry_name.get()
    age = int(entry_age.get())
    if int(age) < 18:
        status_label.config(text="You're too young!")
    else:
        db.my_collection.insert_one({'name': name, 'age': age})
        status_label.config(text="Data inserted successfully")
        
def cv_check():
    # Получаем подходящих пользователей из коллекции my_collection
    suitable_users_cursor = db.my_collection.find({'age': {"$gte": int(25), "$lte": int(40)}})
    
    # Создаем список подходящих пользователей
    suitable_users = list(suitable_users_cursor)
    
    if suitable_users:
        # Вставляем подходящих пользователей в коллекцию suitable_users
        db.suitable_users.insert_many(suitable_users)
        info_label.config(text="All suitable users were sorted")
    else:
        info_label.config(text="No suitable users found")
        

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']


if exists: db.drop_collection('suitable_users')
db.create_collection('suitable_users')
print('collection created')


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

insert_button = tk.Button(root, text="Find suitable users", command=cv_check)
insert_button.grid(row=4, columnspan=2)

info_label = tk.Label(root, text="")
info_label.grid(row=5, columnspan=2)

root.mainloop()

