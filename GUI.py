"""
The Main Graphical User Interface for PasswordVault

"""
import Tkinter
from Tkinter import *
import CryptoOps
import tkMessageBox


def main():
    """
    Authentication Window
    """

    def authwindow():
        # The Window
        auth_window = Tkinter.Tk(screenName=None, baseName=None, className="Authentication", useTk=1)
        # Welcome Message
        welcome = Label(auth_window, text="Welcome to PasswordVault!\n")
        welcome.grid(row=0, column=0, columnspan=2, rowspan=2)

        # Enter Username
        username_label = Label(auth_window, text="Username:")
        username_label.grid(row=2, column=0)
        username_entry = Entry(auth_window, bd=5)
        username_entry.grid(row=2, column=1)

        # Authentication (Passes credentials to CryptoOps)
        def authenticate():
            global username
            username = username_entry.get()
            password = password_entry.get()
            global key
            key, auth = CryptoOps.authenticate(username, password)
            if not auth:
                return
            auth_window.destroy()
            mainwindow()

        def about():
            tkMessageBox.showinfo("About PasswordVault",
                                  "PasswordVault securely encrypts your login credentials\nusing AES-256 with a key derived from your passphrase.\nBy Tony Tan.     www.tonytan98.com")

        # Enter Passphrase
        password_label = Label(auth_window, text="Passphrase:")
        password_label.grid(row=3, column=0)
        password_entry = Entry(auth_window, show="*", bd=5)
        password_entry.grid(row=3, column=1)
        authenticate = Button(auth_window, text="Authenticate", command=authenticate)
        authenticate.grid(row=4, column=1)
        about = Button(auth_window, text="About", command=about)
        about.grid(row=4, column=0)
        auth_window.iconbitmap('icon.ico')
        auth_window.mainloop()

    """
    Main Window
    """

    def mainwindow():
        main_window = Tkinter.Tk(screenName=None, baseName=None, className="PasswordVault: Access", useTk=1)
        welcome = Label(main_window, text="PasswordVault")
        welcome.grid(row=0, column=0, columnspan=2, rowspan=2)

        def read():
            accounts_list = CryptoOps.read_database(username, key)
            tkMessageBox.showinfo("Accounts List", accounts_list)

        def write():
            account = account_entry.get()
            password = password_entry.get()
            CryptoOps.write_database(username, key, account, password)
            tkMessageBox.showinfo("Message", "Details have been added to database.")
            account_entry.delete(0, Tkinter.END)
            password_entry.delete(0, Tkinter.END)

        access_database = Button(main_window, text="Access Database", command=read)
        access_database.grid(row=1, column=0, columnspan=2)

        explain = Label(main_window, text="To add an account, please enter the following:")
        explain.grid(row=2, column=0, columnspan=2)

        # Enter Account
        account_label = Label(main_window, text="Account:")
        account_label.grid(row=3, column=0)
        account_entry = Entry(main_window, bd=5)
        account_entry.grid(row=3, column=1)

        # Enter Password
        password_label = Label(main_window, text="Password:")
        password_label.grid(row=4, column=0)
        password_entry = Entry(main_window, show="*", bd=5)
        password_entry.grid(row=4, column=1)

        write_database = Button(main_window, text="Write to Database", command=write)
        write_database.grid(row=5, column=0, columnspan=2)
        main_window.iconbitmap('icon.ico')
        main_window.mainloop()

    # Display auth window
    authwindow()


if __name__ == "__main__":
    main()