import mysql.connector

class Core:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='<mysql>',
            database='chat_db'
        )

        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL,
            username VARCHAR(32) NOT NULL,
            password VARCHAR(32) NOT NULL
            )
            """
        )
        cursor.close()

    def insert_user(self, username, password):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            INSERT INTO users (username, password)
            VALUES ("{username}", "{password}")
            """
        )
        # cursor.close()
        self.connection.commit()
        # self.connection.close()

    def get_users(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT id, username, password FROM users
            """
        )
        data = cursor.fetchall()
        return data

    def get_info(self, index):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            SELECT username, password FROM users WHERE id={index}
            """
        )
        data = cursor.fetchall()
        return data

    def update_info(self, id, username, password):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            UPDATE users SET username = "{username}", password = "{password}" WHERE id ={id};
            """
        )
        self.connection.commit()

    def delete(self, index):
        cursor = self.connection.cursor()
        cursor.execute(
            f"""
            DELETE FROM users WHERE id={index};
            """
        )
        self.connection.commit()

    def amount(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT COUNT(*) FROM users;
            """
        )
        data = cursor.fetchall()
        return data
