import sqlite3
from tkinter import *

__author__ = 'Robert'

database_filename = "rpg.db"


class LoginGUI(Frame):
    def __init__(self):

        Frame.__init__(self)
        self.master.title("Login Screen")

        self.master.minsize(300, 200)
        self.pack()

        self._usernameLabel = Label(self, text="Enter username")
        self._usernameLabel.pack()

        self._usernameVar = StringVar()
        self._usernameEntry = Entry(self, textvariable=self._usernameVar, width=30)
        self._usernameEntry.pack()

        self._passwordLabel = Label(self, text="Enter password")
        self._passwordLabel.pack()

        self._passwordVar = StringVar()
        self._passwordEntry = Entry(self, textvariable=self._passwordVar, width=30)
        self._passwordEntry.pack()

        self._loginButton = Button(self, text="Login", command=self._login)
        self._loginButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()

        self._quitButton = Button(self, text="Quit", command=self._quit)
        self._quitButton.pack()

    def _auth(self, uname, password):

        print('Attempting to login user with username: %s \npassword: %s' % (uname, password))

        db = sqlite3.connect('rpg.db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        sql_statement = '''SELECT name FROM users WHERE username = '%s' and password = '%s' ''' % (uname, password)

        print('About to execute the following SQL statement: \n' + sql_statement)
        cursor.execute(sql_statement)

        result = None

        for row in cursor:
            result = row['name']
            break
        db.close()

        return result

    def _quit(self):

        exit(0)

    def _login(self):
        username = self._usernameVar.get()
        password = self._passwordVar.get()
        result = self._auth(username, password)

        if result is None:
            display_result = "Username or password incorrect"
        else:
            display_result = "Welcome, " + result

        self._resultVar.set(display_result)

    def setup_database(self):

        db = sqlite3.connect('rpg.db')
        cursor = db.cursor()

        cursor.execute('DROP TABLE IF EXISTS users')

        db.commit()

        cursor.execute('CREATE TABLE user( username text, name text, password text)')

        cursor.execute('''INSERT INTO user VALUES ('admin', 'Rob Admin', 'Heros')''')
        cursor.execute('''INSERT INTO user VALUES ('bart', 'Bart Simpson', 'eatmyshorts')''')
        db.commit()
        db.close()

    def start_gui(self):

        LoginGUI().mainloop()

    def quit(self):

        sys.exit()

    def main(self):
        setup_database()
        start_gui()

    if __name__ == '__main__':

         mainloop()