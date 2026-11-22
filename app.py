import sqlite3

# Test file for CodeRabbit review - contains intentional issues.
PASSWORD = "hunter2-secret-password"

unused_variable = 42


def get_user_by_name(name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '%s'" % name
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    print(get_user_by_name("alice"))
