import sqlite3
conn = sqlite3.connect('books.db')
conn.execute('''CREATE TABLE books
(id INTEGER PRIMARY KEY,
title TEXT,
author TEXT,
year TEXT)
''')

def insert_book():
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Harry Potter and The Sorcerers Stone', 'JK Rowling', '1997')")
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Harry Potter and The Chamber Of Secrets', 'JK Rowling', '1998')")
    conn.execute("INSERT INTO books (title, author, year) VALUES ('Harry Potter and The Prisoner Of Azkaban', 'JK Rowling', '1999')")

def query_database():
    cursor = conn.execute("SELECT id, title, author, year FROM books")
    for row in cursor:
        print(f"id = {row[0]}, title = {row[1]}, author = {row[2]}, year = {row[3]}")

def update_database():
    conn.execute("UPDATE books SET title='Harry Potter and The Philosophers Stone' WHERE id=1")
    conn.commit()

def delete_from_database():
    conn.execute("DELETE FROM books WHERE id=2")
    conn.commit()

def close_connection():
    conn.close()

insert_book()
query_database()
update_database()
query_database()
delete_from_database()
close_connection()
