from tkinter import *

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("Authentication")
window.geometry("600x300")


def check_qualification():
    #   IMPORT THE messagebox FROM tkinter
    from tkinter import messagebox

    try:
        account_balance = int(balance_entry.get())

        if account_balance <= 3000:
            messagebox.showinfo(title=None, message="Please deposit more funds for this excursion.")
        if account_balance > 3000:
            messagebox.showinfo(title=None, message="You qualify for the Malaysia trip. Congratulations.")
    except ValueError:
        messagebox.showerror(title="Value Error", message="Inappropriate value in input")


balance_label = Label(window, text="Enter amount in your account: ", fg="blue")
balance_label.place(x=100, y=50)
balance_entry = Entry(window)
balance_entry.place(x=300, y=50)

verify_btn = Button(window, text="Check Qualification", command=check_qualification, fg="white", bg="blue",
                    width=42).place(x=100, y=100)

window.mainloop()
