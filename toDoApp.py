import tkinter as tk
from tkinter import simpledialog
import sqlite3
from sqlite3 import Error
from datetime import datetime

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        print(f"Connected to the SQLite database version {sqlite3.version}")
        return connection
    except Error as e:
        print(e)
    return connection

def create_table(connection):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        timestamp TEXT NOT NULL
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
        print("Table created successfully")
    except Error as e:
        print(e)

def insert_task(connection, task):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_task_sql = """
    INSERT INTO tasks (task, timestamp) VALUES (?, ?);
    """
    try:
        cursor = connection.cursor()
        cursor.execute(insert_task_sql, (task, timestamp))
        connection.commit()
        print("Task inserted successfully")
    except Error as e:
        print(e)

def on_button_click():
    task = entry.get()
    if task:
        insert_task(db_connection, task)
        update_task_list()
        entry.delete(0, tk.END)

def update_task_list():
    cursor = db_connection.cursor()
    cursor.execute("SELECT task FROM tasks ORDER BY timestamp DESC")
    tasks = cursor.fetchall()
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task[0])

# Main program
db_connection = create_connection("/Users/home/Documents/5. Extra Curriculair/toDoApp/tasks.db")
if db_connection:
    create_table(db_connection)

    # Create the GUI window
    root = tk.Tk()
    root.title("Task Manager")

    # Create and place the entry widget in the window
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # Create and place the button in the window
    button = tk.Button(root, text="Add Task", command=on_button_click)
    button.pack(pady=10)

    # Create and place the listbox for tasks
    task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
    task_listbox.pack(pady=10)

    # Populate the task list
    update_task_list()

    # Start the GUI event loop
    root.mainloop()

    # Close the database connection when the GUI is closed
    db_connection.close()
