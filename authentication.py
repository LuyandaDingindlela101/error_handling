from tkinter import *

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("Authentication")
window.geometry("600x300")

users = {
    "not_Luyanda": "Luyanda_99",
    "not_Ashton": "Ashton_00",
    "not_Nathan": "Nathan_00"
}


def sign_user_in():
    #   IMPORT THE messagebox FROM tkinter
    from tkinter import messagebox

    try:
        #   GET THE VALUES FROM THE ENTRIES
        username_value = username_entry.get()
        password_value = password_entry.get()

        #   FIRST, WE CHECK IF THE username_value ISN'T EMPTY
        if username_value != "" and password_value != "":
            #   NEXT, WE CHECK IF THE username_value ACTUALLY EXISTS IN THE users_object
            if username_value in users:
                #   NOW, WE CHECK IF THE username_value HAS A PASSWORD ATTACHED
                if users.get(username_value):
                    #   ONCE WE GET THE PASSWORD ATTACHED TO THE username_value, WE ASSIGN IT TO db_password
                    db_password = users.get(username_value)
                    #   FINALLY, WE CHECK IF THE PROVIDED PASSWORD(password_value) MATCHES THE SAVED db_password
                    if password_value == db_password:
                        #   HERE, WE KNOW THAT BOTH THE USERNAME AND PASSWORD ARE CORRECT, SO RETURN True
                        window.destroy()
                        import exception_handling
                    #   IF, THE PROVIDED PASSWORD(password_value) DOESNT MATCH THE SAVED db_password, NOTIFY THE USER
                    else:
                        messagebox.showinfo(title=None, message="Password is incorrect")
                else:
                    messagebox.showinfo(title=None, message="Password doesnt match username")
            else:
                messagebox.showinfo(title=None, message="Username doesnt exist in our database")
        #   IF THE input_value IS EMPTY, INFORM THE USER/
        else:
            messagebox.showinfo(title=None, message="Inputs cannot be empty, please enter a value")
            # clear_entries()
    except Exception as exception:
        messagebox.showinfo(exception)
    finally:
        pass


username_label = Label(window, text="Please enter your username", fg="blue")
username_label.place(x=100, y=10)
username_entry = Entry(window)
username_entry.place(x=300, y=10)

password_label = Label(window, text="Please enter your password", fg="blue")
password_label.place(x=100, y=50)
password_entry = Entry(window)
password_entry.place(x=300, y=50)

verify_btn = Button(window, text="Login", command=sign_user_in, fg="white", bg="blue", width=42).place(x=100, y=100)

window.mainloop()
