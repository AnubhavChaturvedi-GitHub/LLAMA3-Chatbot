from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QFont, QColor, QTextCursor
from PyQt5.QtCore import Qt, QTimer
from brain import Main_Brain  # Importing the Main_Brain class

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Net Hi-Tech Chatbot Login")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #1b1f23; color: white;")

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.username_label)

        self.username_input = QLineEdit()
        self.username_input.setFont(QFont("Arial", 12))
        self.username_input.setStyleSheet("background-color: #2c3136; color: white; border: none; padding: 10px;")
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_label.setFont(QFont("Arial", 12))
        layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setStyleSheet("background-color: #2c3136; color: white; border: none; padding: 10px;")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont("Arial", 12, QFont.Bold))
        self.login_button.setStyleSheet("background-color: #ff5e6c; color: white; padding: 10px; border-radius: 10px;")
        self.login_button.clicked.connect(self.check_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "admin@123":
            self.close()
            self.open_chatbot()
        else:
            self.username_input.clear()
            self.password_input.clear()
            self.username_input.setPlaceholderText("Invalid credentials, try again.")

    def open_chatbot(self):
        self.chatbot_window = ChatbotWindow()
        self.chatbot_window.show()

class ChatbotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Net Hi-Tech Chatbot")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background-color: #1b1f23; color: white;")

        main_layout = QVBoxLayout()

        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setFont(QFont("Arial", 14))
        self.chat_display.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #262b30, stop:1 #1e2126);
            color: white;
            border: 2px solid #ff5e6c;
            border-radius: 15px;
            padding: 10px;
        """)
        self.chat_display.setReadOnly(True)
        main_layout.addWidget(self.chat_display)

        # Input area
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 14))
        self.input_field.setStyleSheet("""
            background-color: #2c3136;
            color: white;
            border-radius: 10px;
            padding: 10px;
            border: 2px solid #ff5e6c;
        """)
        self.input_field.returnPressed.connect(self.handle_return_pressed)
        input_layout.addWidget(self.input_field)

        # Sci-Fi styled send button
        self.send_button = QPushButton("🚀 Send")
        self.send_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #ff5e6c;
                color: white;
                padding: 15px;
                border-radius: 45px;
                border: 2px solid #ff5e6c;
                
                
            }
            QPushButton:hover {
                background-color: #ff7489;
               
            }
        """)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)

    def handle_return_pressed(self):
        if self.input_field.text().strip():
            self.send_message()

    def send_message(self):
        message = self.input_field.text()
        if message:
            self.chat_display.append(f"<p style='color: #ff5e6c;'><b>You:</b> {message}</p>")
            self.input_field.clear()

            # Simulate typing animation
            self.chat_display.append("<p style='color: #888;'><i>Net Hi-Tech Chatbot is thinking...</i></p>")
            QTimer.singleShot(2000, lambda: self.display_response(message))  # 2-second delay to simulate thinking

    def display_response(self, user_message):
        response = Main_Brain(user_message)  # Use Main_Brain to generate the response
        self.chat_display.append(f"<p style='color: #66cc99;'><b>Net Hi-Tech Chatbot:</b> {response}</p>")
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.End)
        self.chat_display.setTextCursor(cursor)

# Main application
def main():
    app = QApplication([])
    login = LoginWindow()
    login.show()
    app.exec_()

if __name__ == "__main__":
    main()
