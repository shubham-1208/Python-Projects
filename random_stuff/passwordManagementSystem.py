import tkinter
import tkinter.messagebox 
import pickle

shift = 6
alpha = "a890~!@#$dDeHiENoxXyYzOpPW^&*(qbB4MnvVwZ1Qc567%)jAFghI3rRsStTuGKlLUfmCJk2"

root = tkinter.Tk()
root.geometry('1000x700')
root.title("Password Management System")

def encrypt(s, shift = shift):
    encrypted_str = ""
    for character in s:
        index = alpha.index(character)
        shifted_index = (index + shift) % len(alpha)
        encrypted_str += alpha[shifted_index]
    return encrypted_str

def add_password():
    password = entry_password.get()
    app_name = entry_app_name.get()
    shift = int(entry_shift.get())
    password1 = encrypt(password, shift)
    data = password1 +" is the password for " + app_name + " with a shift of " + entry_shift.get()
    if password != "" and app_name != "" and entry_shift.get():
        listbox_password.insert(tkinter.END, data)
        entry_password.delete(0, tkinter.END)
        entry_app_name.delete(0, tkinter.END)
        entry_shift.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter an APP NAME and a PASSWORD and SHIFT must be an integer.")

def delete_password():
    try:
        password_index = listbox_password.curselection()[0]
        listbox_password.delete(password_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a password.")

def load_password():
    try:
        password = pickle.load(open("password.dat", "rb"))
        listbox_password.delete(0, tkinter.END)
        for password in password:
            listbox_password.insert(tkinter.END, password)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must save a password.")

def save_password():
    password = listbox_password.get(0, listbox_password.size())
    pickle.dump(password, open("password.dat", "wb"))

frame_password = tkinter.Frame(root)
frame_password.pack()

listbox_password = tkinter.Listbox(frame_password, height = 30, width = 185, bg ="#93FF33")
listbox_password.pack(side=tkinter.LEFT)

scrollbar_password = tkinter.Scrollbar(frame_password)
scrollbar_password.pack(side=tkinter.RIGHT, fill=tkinter.Y)

scrollbar_password.config(command = listbox_password.yview)
listbox_password.config(yscrollcommand = scrollbar_password.set)

label_kg = tkinter.Label(root, text ="APP NAME: ")
label_kg.pack()

entry_app_name = tkinter.Entry(root, width = 60, bg = "#33FFE3")
entry_app_name.pack()

label_kg = tkinter.Label(root, text ="PASSWORD CHARACTERS: ")
label_kg.pack()

entry_password = tkinter.Entry(root, width = 60, bg = "#33FFE3")
entry_password.pack()

label_kg = tkinter.Label(root, text ="SHIFT: ")
label_kg.pack()

entry_shift = tkinter.Entry(root, width = 60, bg = "#33FFE3")
entry_shift.pack()

button_add_password = tkinter.Button(root, text = "Add password", width = 160, command = add_password, bg = 'YELLOW')
button_add_password.pack()

button_delete_password = tkinter.Button(root, text = "Delete password", width = 160, command = delete_password, bg = "RED")
button_delete_password.pack()

button_load_password = tkinter.Button(root, text = "Load passwords", width = 160, command = load_password, bg = "GREEN")
button_load_password.pack()

button_save_password = tkinter.Button(root, text = "Save passwords", width = 160, command = save_password, bg = "BLUE")
button_save_password.pack()

root.mainloop()