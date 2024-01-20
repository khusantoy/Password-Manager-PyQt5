from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QListWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import (
    Qt,
    QTimer
)

from core import Core

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.setWindowTitle('New User')
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #212529;
        """)
        self.setFixedSize(400, 500)
        self.v_box = QVBoxLayout()

        self.username_edit = QLineEdit()
        self.username_edit.setStyleSheet("""
        color: #fff;
        border: 2px solid #0D6EFD;
        border-radius: 10px;
        """)
        self.username_edit.setFixedHeight(40)
        self.username_edit.setPlaceholderText("Enter username")

        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("""
        color: #fff;
        border: 2px solid #0D6EFD;
        border-radius: 10px;
        """)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setFixedHeight(40)
        self.password_edit.setPlaceholderText("Enter password")
        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignCenter)

        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedHeight(40)
        self.save_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0D6EFD;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0D6EFD;
        }
        """)

        self.show_btn = QPushButton("Show Users")
        self.show_btn.setFixedHeight(40)
        self.show_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0D6EFD;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0D6EFD;
        }
        """)

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.setFixedHeight(40)
        self.exit_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #DC3545;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #DC3545;
        }
        """)

        self.v_box.addWidget(self.username_edit)
        self.v_box.addWidget(self.password_edit)
        self.v_box.addWidget(self.status)
        self.v_box.addStretch()
        self.v_box.addWidget(self.save_btn)
        self.v_box.addWidget(self.show_btn)
        self.v_box.addWidget(self.exit_btn)

        self.setLayout(self.v_box)

        self.show()

        self.save_btn.clicked.connect(self.save_user)
        self.show_btn.clicked.connect(self.users_list)
        self.exit_btn.clicked.connect(self.exit_win)

    def save_user(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        if username and password and 15 > len(password) >= 8 and len(username) < 13 and username[0].isalpha() and username.isalnum():
            self.core.insert_user(username, password)
            self.status.setStyleSheet("""
                            background-color: #198754;
                            color: #FFF;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Successfuly Added")
            self.username_edit.clear()
            self.password_edit.clear()

        elif not username.isalnum() and username:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Write Username like a-z, 0-9")
        elif len(username) > 13:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Username max length 13")
        elif len(password) > 15:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Password max length 15")
        elif len(username) > 0 and not username[0].isalpha():
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Start Username With a-z")
        elif 0 < len(password) < 8:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-family: Arial;
                font-size: 18px;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
            """)
            self.status.setText("Password is Less From 8")
        else:
            self.status.setStyleSheet("""
                background-color: #DC3545;
                color: #FFF;
                font-family: Arial;
                font-size: 18px;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
            """)
            self.status.setText("Fill Empty Spaces")
        QTimer.singleShot(3000, self.remove_label)

    def remove_label(self):
        self.status.setStyleSheet("")
        self.status.setText("")


    def clear_edit(self):
        self.username_edit.clear()
        self.password_edit.clear()

    def users_list(self):
        self.close()
        self.win = DisplayWindow()

    def exit_win(self):
        self.close()

class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Users')
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #212529;
        """)
        self.core = Core()
        self.setFixedSize(400, 500)
        self.v_box = QVBoxLayout()

        self.text = QLabel(self)
        self.text.setText('Username List:')
        self.text.setStyleSheet("""
            font-size:20px;
            color: #fff;
        """)

        self.list = QListWidget(self)
        self.list.setStyleSheet("""
        border: 2px solid #0D6EFD;
        color: #fff;
        border-radius: 10px;
        """)
        self.back_btn = QPushButton(self)
        self.back_btn.setFixedHeight(40)
        self.back_btn.setText("Back")
        self.back_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0D6EFD;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0D6EFD;
        }
        """)

        self.view_btn = QPushButton("View Password")
        self.view_btn.setFixedHeight(40)
        self.view_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0DCAF0;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0DCAF0;
        }
        """)

        self.edit_btn = QPushButton("Edit")
        self.edit_btn.setFixedHeight(40)
        self.edit_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #FFC107;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #FFC107;
        }
        """)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.setFixedHeight(40)
        self.delete_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #DC3545;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #DC3545;
        }
        """)

        self.v_box.addWidget(self.text)
        self.v_box.addWidget(self.list)
        self.v_box.addWidget(self.view_btn)
        self.v_box.addWidget(self.edit_btn)
        self.v_box.addWidget(self.delete_btn)
        self.v_box.addWidget(self.back_btn)

        self.setLayout(self.v_box)

        self.show()
        self.show_all_user()

        self.back_btn.clicked.connect(self.back_win)
        self.view_btn.clicked.connect(self.view_password)
        self.edit_btn.clicked.connect(self.edit_data)
        self.delete_btn.clicked.connect(self.delete_data)

    def back_win(self):
        self.close()
        self.win = Window()

    def show_all_user(self):
        list = self.core.get_users()
        count = 1
        for i in list:
            sec = (len(i[2])) * '*'
            self.list.addItem(f"{count}. {i[1]} {sec} {i[0]}")
            count+=1

    def view_password(self):
        count = self.core.amount()
        if count[0][0] == 0:
            self.err_win = WindowError()
            QTimer.singleShot(3000, self.close_win)
        else:
            item = self.list.currentItem().text()
            item = item.split()
            data = self.core.get_info(item[-1])
            self.win = DisplayPass()
            self.win.set_data(data[0][0], data[0][1])

    def edit_data(self):
        count = self.core.amount()
        if count[0][0] == 0:
            self.err_win = WindowError()
            QTimer.singleShot(3000, self.close_win)
        else:
            item = self.list.currentItem().text()
            item = item.split()
            data = self.core.get_info(item[-1])
            self.close()
            self.win = WindowEdit()
            self.win.set_data(item[-1], data[0][0], data[0][1])

    def close_win(self):
        self.err_win.close()
    def delete_data(self):
        count = self.core.amount()
        if count[0][0] == 0:
            self.err_win = WindowError()
            QTimer.singleShot(3000, self.close_win)
        else:
            item = self.list.currentItem().text()
            item = item.split()
            id = item[-1]
            self.close()
            self.win = WindowDelete()
            self.win.get_id(id)

class DisplayPass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Info")
        self.setFixedSize(300, 250)
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #212529;
        """)

        self.v_box = QVBoxLayout()

        self.username_label = QLabel(self)
        self.username_label.setText("Username:")
        self.username_label.setStyleSheet("color: #FFF")
        self.username_text = QLineEdit(self)
        self.username_text.setReadOnly(True)
        self.username_text.setFixedHeight(45)
        self.username_text.setText("username")
        self.username_text.setStyleSheet("""
            background-color: #343A40;
            color: #FFF;
            font-family: Arial;
            font-size: 18px;
            font-weight: bold;
            padding-top: 10px;
            padding-bottom: 10px;
            border-radius: 10px;
        """)

        self.pass_label = QLabel(self)
        self.pass_label.setText("Password:")
        self.pass_label.setStyleSheet("color: #FFF;")
        self.pass_text = QLineEdit(self)
        self.pass_text.setReadOnly(True)
        self.pass_text.setFixedHeight(45)
        self.pass_text.setText("12345678")
        self.pass_text.setStyleSheet("""
            background-color: #343A40;
            color: #FFF;
            font-family: Arial;
            font-size: 18px;
            font-weight: bold;
            padding-top: 10px;
            padding-bottom: 10px;
            border-radius: 10px;
        """)

        self.close_btn = QPushButton(self)
        self.close_btn.setFixedHeight(45)
        self.close_btn.setText("Close")
        self.close_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0D6EFD;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0D6EFD;
        }
        """)

        self.v_box.addWidget(self.username_label)
        self.v_box.addWidget(self.username_text)
        self.v_box.addWidget(self.pass_label)
        self.v_box.addWidget(self.pass_text)
        self.v_box.addWidget(self.close_btn)

        self.setLayout(self.v_box)

        self.show()

        self.close_btn.clicked.connect(self.close_win)

    def close_win(self):
        self.close()

    def set_data(self, username, password):
        self.username_text.setText(username)
        self.pass_text.setText(password)

class WindowEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.setWindowTitle('Edit')
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #212529;
        """)
        self.setFixedSize(400, 300)
        self.v_box = QVBoxLayout()

        self.index = 0

        self.username_edit = QLineEdit()
        self.username_edit.setStyleSheet("""
        color: #fff;
        border: 2px solid #0D6EFD;
        border-radius: 10px;
        """)
        self.username_edit.setFixedHeight(40)
        self.username_edit.setPlaceholderText("Enter username")

        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("""
        color: #fff;
        border: 2px solid #0D6EFD;
        border-radius: 10px;
        """)
        self.password_edit.setFixedHeight(40)
        self.password_edit.setPlaceholderText("Enter password")
        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignCenter)

        self.update_btn = QPushButton("Update")
        self.update_btn.setFixedHeight(40)
        self.update_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #198754;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #198754;
        }
        """)

        self.close_btn = QPushButton(self)
        self.close_btn.setFixedHeight(40)
        self.close_btn.setText("Close")
        self.close_btn.setStyleSheet("""
        QPushButton {
            border: 2px solid #0D6EFD;
            border-radius: 10px;
            color: #fff;
        }
        QPushButton:hover {
            background-color: #0D6EFD;
        }
        """)

        self.v_box.addWidget(self.username_edit)
        self.v_box.addWidget(self.password_edit)
        self.v_box.addWidget(self.status)
        self.v_box.addStretch()
        self.v_box.addWidget(self.update_btn)
        self.v_box.addWidget(self.close_btn)

        self.setLayout(self.v_box)

        self.show()

        self.update_btn.clicked.connect(self.update_info)
        self.close_btn.clicked.connect(self.close_win)

    def set_data(self, id, username, password):
        self.username_edit.setText(f"{username}")
        self.password_edit.setText(f"{password}")

        self.index = id

    def update_info(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        id = self.index

        if username and password and 15 > len(password) >= 8 and len(username) < 13 and username[0].isalpha() and username.isalnum():
            self.core.update_info(id, username, password)
            self.status.setStyleSheet("""
                            background-color: #198754;
                            color: #FFF;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Successfuly Added")
            self.close()
            self.win = DisplayWindow()
        elif not username.isalnum() and username:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Write Username like a-z, 0-9")
        elif len(username) > 13:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Username max length 13")
        elif len(password) > 15:
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Password max length 15")
        elif len(username) > 0 and not username[0].isalpha():
            self.status.setStyleSheet("""
                            background-color: #FFC107;
                            color: #FFF;
                            font-family: Arial;
                            font-size: 18px;
                            font-weight: bold;
                            padding-top: 10px;
                            padding-bottom: 10px;
                            border-radius: 10px;
                        """)
            self.status.setText("Start Username With a-z")
        elif 0 < len(password) < 8:
            self.status.setStyleSheet("""
                background-color: #FFC107;
                color: #FFF;
                font-family: Arial;
                font-size: 18px;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
            """)
            self.status.setText("Password is Less From 8")
        else:
            self.status.setStyleSheet("""
                background-color: #DC3545;
                color: #FFF;
                font-family: Arial;
                font-size: 18px;
                font-weight: bold;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 10px;
            """)
            self.status.setText("Fill Empty Spaces")
        QTimer.singleShot(3000, self.remove_label)

    def remove_label(self):
        self.status.setStyleSheet("")
        self.status.setText("")

    def close_win(self):
        self.close()
        self.win = DisplayWindow()

class WindowDelete(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete All Info")
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 18px;
        background-color: #212529;
        """)
        self.setFixedSize(400, 200)

        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.text = QLabel(self)
        self.text.setText("Are You Sure?")
        self.text.setStyleSheet("color: #fff")
        self.text.setAlignment(Qt.AlignCenter)

        self.btn_yes = QPushButton(self)
        self.btn_yes.setFixedHeight(40)
        self.btn_yes.setText("Purge Remove")
        self.btn_yes.setStyleSheet("""
            background-color: #DC3545;
            border-radius: 10px;
            color: #fff;
        """)

        self.btn_cancel = QPushButton(self)
        self.btn_cancel.setFixedHeight(40)
        self.btn_cancel.setText("Cancel")
        self.btn_cancel.setStyleSheet("""
            background-color: #6C757D;
            border-radius: 10px;
            color: #fff;
        """)

        self.h_box.addWidget(self.btn_yes)
        self.h_box.addWidget(self.btn_cancel)

        self.v_box.addWidget(self.text)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.btn_yes.clicked.connect(self.purge_remove)
        self.btn_cancel.clicked.connect(self.cancel)

        self.show()

    def get_id(self, id):
        self.id = id

    def purge_remove(self):
        self.core = Core()
        self.core.delete(self.id)
        self.close()
        self.win = DisplayWindow()

    def cancel(self):
        self.close()
        self.win = DisplayWindow()

class WindowError(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Warning!")
        self.setStyleSheet("""
        font-family: Arial;
        font-size: 24px;
        background-color: #212529;
        """)
        self.setFixedSize(400, 100)

        self.v_box = QVBoxLayout()

        self.text = QLabel(self)
        self.text.setText("Empty Box 📦")
        self.text.setStyleSheet("color: #fff")
        self.text.setAlignment(Qt.AlignCenter)

        self.v_box.addWidget(self.text)

        self.setLayout(self.v_box)

        self.show()

app = QApplication([])
win = Window()
app.exec_()