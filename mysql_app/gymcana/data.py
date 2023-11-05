from uu import Error

import mysql.connector


class DataEngine:
    def __init__(self, username, password, host, database=None) -> None:
        self._username = username
        self._password = password
        self._host = host
        try:
            self._connection = mysql.connector.connect(
                host="localhost",
                database=database,
                user=username,
                password=password,
            )
            if self._connection.is_connected():
                db_info = self._connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                self._cursor = self._connection.cursor()
                self._cursor.execute("select database();")
                record = self._cursor.fetchone()
                print("You're connected to database: ", record)
        except ValueError as e:
            print("Error while connecting to MySQL", e)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    @property
    def cursor(self):
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = value

    def run_query(self, sql_query: str) -> bool:
        if self.connection.is_connected():
            try:
                self.cursor.execute(sql_query)
            except Error as e:
                # Re-raise the exception to be caught by the calling function
                raise Error(f"Failed to execute {sql_query}: {e}")
            finally:
                # Close the cursor and connection
                self.cursor.close()
                self.connection.close()
        return True

    def close(self):
        if self._connection.is_connected():
            self._cursor.close()
            self._connection.close()
            print("MySQL connection is closed")
