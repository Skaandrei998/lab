# import sqlite3
#
# from sqlite3 import Error
#
#
# def sql_connection():
#     try:
#         con = sqlite3.connect('mydatabase.db')
#         return con
#     except Error:
#         print(Error)
#
#
# def sql_table(con):
#     cursorObj = con.cursor()
#     cursorObj.execute(
#         "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
#     con.commit()
#
#
# con = sql_connection()
# sql_table(con)

#
# import sqlite3
#
# con = sqlite3.connect('mydatabase.db')
#
#
# def sql_insert(con, entities):
#     cursorObj = con.cursor()
#     cursorObj.execute(
#         'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
#     con.commit()
#
#
# entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
#
# sql_insert(con, entities)


# import sqlite3
#
# con = sqlite3.connect('mydatabase.db')
#
#
# def sql_update(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
#     con.commit()
#
#
# sql_update(con)

# import sqlite3
#
# con = sqlite3.connect('mydatabase.db')
#
#
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('SELECT * FROM employees')
#     rows = cursorObj.fetchall()
#
#     for row in rows:
#         print(row)
#
#

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('DROP table if exists employees')
    con.commit()


sql_fetch(con)
# sql_fetch(con)
#
import sqlite3

con = sqlite3.connect('mydatabase.db')

con.close()