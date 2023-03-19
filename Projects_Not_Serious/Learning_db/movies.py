import sqlite3
import os
import time
conn = sqlite3.connect('movies.db')

def show_main_menu():
    print('''What would you like to do?\n
    1. Create new database (If accidentally deleted)\n
    2. Show movies list\n
    3. Get a random movie\n
    4. Add new movie\n
    5. Edit movie details\n
    6. Delete a movie\n
    7. End program\n''')

def show_edit_menu():
    print('''What would you like to edit?\n
    1. Title\n
    2. Genre\n
    3. Link\n
    4. Quit
    ''')

def show_delete_menu():
    print('''What would you like to delete?''')


def create_database():
    try:
        conn.execute(''' CREATE TABLE movies
        (id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        link TEXT)
        ''')
        print("New database has been created...")
    except sqlite3.OperationalError:
        print('Database already exists')

def add_movie():
    user_title = input("Movie Title: ")
    user_genre = input("Movie Genre: ")
    user_link = input("Movie Link: ")
    conn.execute('INSERT INTO movies (title, genre, link) VALUES (?,?,?)', (user_title, user_genre, user_link))
    conn.commit()

def exit_program():
    conn.close()

def show_movies(): # Figure out a way to make it so that I don't have to copy and paste this for the randomizer
    try:
        cursor = conn.execute("SELECT id, title, genre, link FROM movies")
        cursor_2 = conn.execute("SELECT COUNT(*) FROM movies")
        result = cursor_2.fetchone()
        if result[0] == 0:
            print("There is nothing in this database. Please add a movie record")
        else:
            for row in cursor:
                print(f'ID: {row[0]}, Title: {row[1]}, Genre: {row[2]}, Link: {row[3]}')
    except sqlite3.OperationalError:
        print("There is no database. Please create one.")
    return cursor

def randomize_movies():
    try:
        cursor = conn.execute("SELECT id, title, genre, link FROM movies")
        cursor_2 = conn.execute("SELECT COUNT(*) FROM movies")
        result = cursor_2.fetchone()
        if result[0] == 0:
            print("There is nothing in this database. Please add a movie record")
        else:
            for row in cursor:
                print(row[0])
    except sqlite3.OperationalError:
        print("There is no database. Please create one.")

def edit_movie():
    # Show a new menu with all the movies and their IDs. 
    # Then have the user select the ID of the movie they want to edit or if they want to go back
    # Then have the user select what item they want to edit
    # Then have the user input the new update and ask if they need to update anything else
    # Go back to the main menu
    show = show_movies()
    cursor = conn.execute("SELECT id, title, genre, link FROM movies")
    movies = cursor.fetchall()

    while True:
        try:
            edited = int(str(input('What movie would you like to edit: ')))
            if edited < 1 or edited > len(movies):
                os.system('cls')
                print("INCORRECT VALUE")
                time.sleep(2)
            else:
                show_edit_menu()
                user_title = ''
                user_genre = ''
                user_link = ''
                try:
                    user_edit_choice = int(str(input('Input a corresponding menu choice: ')))
                    if user_edit_choice < 1 or user_edit_choice > 4:
                        os.system('cls')
                        print("INCORRECT VALUE")
                        time.sleep(2)
                    else:
                        if user_edit_choice == 1:
                            user_title = input('What is the new title: ')
                            cursor.execute("UPDATE movies SET title=? WHERE id=?", (user_title, edited))
                            conn.commit()
                            break
                        elif user_edit_choice == 2:
                            user_genre = input('What is the new genre: ')
                            cursor.execute("UPDATE movies SET genre=? WHERE id=?", (user_genre, edited))
                            conn.commit()
                            break
                        elif user_edit_choice == 3:
                            user_link = input('What is the new link: ')
                            cursor.execute('UPDATE movies SET link=?, WHERE id=?', (user_link, edited))
                            conn.commit()
                            break
                        elif user_edit_choice == 4:
                            break
                except ValueError:
                    os.system('cls')
                    print("INCORRECT VALUE")
                    time.sleep(2)
        except ValueError:
            os.system('cls')
            print("INCORRECT VALUE")
            time.sleep(2)
        


def get_menu_choice():
    while True:
        try:
            show_main_menu()
            user_choice = int(str(input('Input a corresponding menu choice: ')))
            if user_choice < 1 or user_choice > 7:
                os.system('cls')
                print("INCORRECT VALUE")
                time.sleep(2)
            else:
                return user_choice
        except ValueError:
            os.system('cls')
            print("INCORRECT VALUE")
            time.sleep(2)

def select_menu_item():
    user_input = get_menu_choice()
    if user_input == 1:
        create_database()
        conn.close()
    elif user_input == 2:
        show_movies()
        conn.close()
    elif user_input == 3:
        randomize_movies()
        conn.close()
    elif user_input == 4:
        add_movie()
        conn.close()
    elif user_input == 5:
        edit_movie()
        conn.close()
    elif user_input == 7:
        exit_program()
    else:
        print("Yup")

select_menu_item()



    

