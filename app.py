import sqlite3
import tornado.web, tornado.ioloop
import json
from import_old_contact import import_old_contacts as ioc

# create a connect obj
# if db with given name does not exist, creates it.
my_connection = sqlite3.connect("sqliteDB.db")

# create a cursor object to execute sql statements
my_cursor = my_connection.cursor()

try:
    # try to create a table in the db using cursor generated from the connection
    my_cursor.execute(
    """
        CREATE TABLE contacts(
            id INTEGER PRIMARY KEY,
            first TEXT,
            last TEXT,
            phone TEXT,
            email TEXT);
    """)
except sqlite3.OperationalError as err:
    pass

# my_cursor.execute(
#     """
#     INSERT INTO contacts (first, last, phone, email)
#     VALUES ('Karl', 'Jablonski', '917-500-5000', 'kjab@jablonskiresorts.com'), 
#     ('Lesly Junior', 'Jean', '917-500-4000', 'ljjr@theleslyans.com'),
#     ('Jean Mario David', 'Percy', '917-400-4400', 'jmdpercy@thepercycompany.com'),
#     ('Marckly', 'Mathurin', '917-200-2000', 'marckly@mathurinent.com'),
#     ('Serda', 'Simus', '917-524-5245', 'rogue_swe@rogueones.com');
#     """)
# my_cursor.execute("""DELETE FROM contacts;""")
# my_connection.commit()

# using fetchall()
# res = my_cursor.execute("""SELECT first, last, email, phone FROM contacts LIMIT 100;""").fetchall()


# USING fetchone() WHICH RETURNS A PYTHON ITER() OBJECT
# returns  contacting data relate to a single row
# returns the first item on the table

# my_cursor.execute("""SELECT first,last,phone,email FROM contacts LIMIT 10;""")

# while True:
#     try:

#         f,l,p, e = next(my_cursor)
#         print(f"F| {f}, \tL| {l} - \tE| {e}, \tP| {p}")
#     except StopIteration as err:
#         break

# print()
# print("*" * 20)
# print("*" * 20,"\n")

# for _,f,l,p,e in my_cursor.execute("SELECT * FROM contacts"):
#     print(f"First: {f}, Last: {l}, Email: {e}, Phone: {p}")

# USING fetchmany()
# fetchone  == fetchmany(1) # at a time.
# fetchall == fetchmany(number_of_rows) in the table being fetched
# with open(r"my_file.txt", mode="w") as wf:
#     cur_obj = my_cursor.execute("SELECT * FROM contacts")
#     while True:
#         try:
#             i,f,l,p,e = next(cur_obj)
#             print(f"Contact {f} {l} at {p} or via email at {e}.", file=wf, sep="\n")
#         except StopIteration as err:
#             break

# Iterator Test for Understanding
# my_iter = my_cursor.execute("SELECT * FROM contacts")

# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration as err:
#         break


# my_iter = iter(my_cursor.execute("SELECT * FROM contacts").fetchall())

# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration as err:
#         break


# my_iter = my_cursor.execute("SELECT * FROM contacts")

# while True:
#     try:
#         print(my_iter.fetchmany(1))
#     except StopIteration as err:
#         break


# # WAY 1 converts data into dictionaries, 
# # but requires knowledge of data's structure, may yield errors.
# with open(r"./data/datafile1.txt", mode="w+") as wf:
#     my_iter = my_cursor.execute("SELECT * FROM contacts")
#     table_headers = [row[0] for row in my_iter.description]
#     my_data1 = [{table_headers[index]: each_value[index] for index in range(len(table_headers))} for each_value in my_iter]
#     print(my_data1)
#     for data in my_data1:
#         a_record = ""
#         for key, value in data.items():
#             a_record += f"{key}: {value}, "
#         print(a_record, file=wf, sep="\n")



# # WAY 2: Use Zip which comes with built-in error-handling,
# # in cases where data sizes don't match.
# with open(r"./data/datafile2.txt", mode="w+") as wf:
#     my_iter = my_cursor.execute("SELECT * FROM contacts")
#     table_headers = [row[0] for row in my_iter.description]
#     my_data2 = [dict(zip(table_headers, item))for item in my_iter]
#     print(my_data2)
#     for data in my_data2:
#         a_record = ""
#         for key, value in data.items():
#             a_record += f"{key}: {value}, "
#         print(a_record, file=wf, sep="\n")


# # # WAY 3: Use Zip and the cursor row factory method
# with open(r"./data/datafile3.txt", "w+") as wf:
#     my_cursor.execute("SELECT * FROM contacts")
#     table_headers = [item[0] for item in my_cursor.description]
#     my_cursor.row_factory = lambda cur, row: dict(zip(table_headers, row))
#     for item in my_cursor:
#         # print(item)
#         print(item, file=wf, sep="\n")


# # # WAY 3: Binding the row_factory method to sqlite3.Row
# with open(r"./data/datafile4.txt", "w+") as wf:
#     my_cursor.execute("SELECT * FROM contacts")
#     my_cursor.row_factory = sqlite3.Row
#     for item in my_cursor.fetchall():
#         print(f"{item} => {dict(item)}", sep="\n", file=wf)

# getting values from user, protecting against SQL Injections
# with open(r"./data/last_user_added.txt", "w+") as wf:
#     print("Enter new contact as: First, Last, Email, Phone")
#     print("Example: James, Bond, jamesbond@agent007.com, 212-212-5555")
#     input = input("$: ")
#     user_input = dict(zip(["first", "last", "email", "phone"], [item.strip() for item in input.strip().split(",")]))
#     print(user_input, file=wf)
#     my_cursor = my_connection.cursor()
#     # DO NOT DO THIS, ISSUES WITH SQL INJECTIONS
#     # my_cursor.execute(f"""
#     #                   INSERT INTO contacts (first, last, email, phone)
#     #                   VALUES({user_input['first']}, {user_input['last']},{user_input['email']},{user_input['phone']})""")
#     #DO THIS INSTEAD:
#     # user_input_to_sanitize = tuple( user_input.values())
#     # my_cursor.execute("INSERT INTO contacts (first, last, email, phone) VALUES(?,?,?,?)", user_input_to_sanitize)
#     # my_connection.commit()
    
#     # USING Key-Value Pairs:
#     user_input_to_sanitize = tuple( user_input.values())
#     my_cursor.execute("INSERT INTO contacts (first, last, email, phone) VALUES(:first,:last,:email,:phone)", user_input)
#     my_connection.commit()

# USING .executemany method in SQLite3
# executemany works when we want to insert more than one value, 
# it executes the given statement multiple times for as many values as needed.


ioc(my_connection)




# class HomeRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Home Page")
        
# class ContactsRequestHandler(tornado.web.RequestHandler):
#     def get(self):
#         my_cursor.execute("SELECT first, last, email, phone FROM contacts")
#         my_connection.commit()
#         my_cursor.row_factory = lambda cursor, row: dict(zip(["first", "last", "email", "phone"], row))
#         self.write(json.dumps(my_cursor.fetchall()))

# class ContactRequestHandler(tornado.web.RequestHandler):
#     def get(self, user_id=None):
#         my_cursor.execute("SELECT first, last, email, phone FROM contacts WHERE id=?", user_id)
#         my_connection.commit()
#         self.write(json.dumps(*my_cursor.fetchall()))

# if __name__ == "__main__":
#     app = tornado.web.Application([
#         (r"/", HomeRequestHandler),
#         (r"/contact/([0-9]+)", ContactRequestHandler),
#         (r"/contacts", ContactsRequestHandler)])

#     port = 8882
#     app.listen(port)
#     print(f"app is listening on port: {port}")
#     tornado.ioloop.IOLoop.current().start()
