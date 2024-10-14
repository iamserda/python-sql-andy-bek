import sqlite3
import json


from old_phone import old_phone_contacts as old_contacts

db_connector = sqlite3.connect("base1.db")
my_cursor = db_connector.cursor()

try:
    my_cursor.execute(
        """
        CREATE TABLE contacts(
            id INTEGER PRIMARY KEY,
            first TEXT,
            last TEXT,
            email TEXT,
            phone TEXT);"""
    )
except sqlite3.OperationalError as err:
    print("Table already exists. Will continue...")
    pass

# my_cursor.executemany("""INSERT INTO contacts (first, last, email, phone) VALUES(:first, :last, :email,:phone)""", old_contacts)
# db_connector.commit()

# READ
def get_contact_by_id(id:int):
    local_cursor = db_connector.cursor()
    sql_stmnt = "SELECT * FROM contacts WHERE id=:id"
    local_cursor.execute(sql_stmnt,{"id": id})
    db_connector.commit()
    print(local_cursor.fetchone())
    # print(local_cursor)
    # for item in local_cursor:
    #     print(item)
    local_cursor.close()
# # TESTING
# get_contact_by_id(100)
# get_contact_by_id(10)
# get_contact_by_id(1)

# # UPDATE
# def change_contact_by_id(id, new_data):
#     pass

# # CREATE 
# def create_new_contact():
#     pass

# # DELETE
# def delete_contact_by_id(id):
#     local_cursor = db_connector.cursor()
#     statement = "DELETE FROM contacts WHERE id=:id"
#     local_cursor.execute(statement, {"id": id})
#     db_connector.commit()
#     local_cursor.close()
# # TESTING 
# delete_contact_by_id(1)
# delete_contact_by_id(2)

# # DB DUMP: SAVING ALL SQL STATEMENTS USED TO CREATE AND MODIFY THE DB. WE CAN RECREATE THE DB WITH THAT FILE.
# with open("./data/base1_db.sql", "w+") as wf:
#     statement_generator = db_connector.iterdump()
#     for row in statement_generator:
#         wf.write(row + "\n")

