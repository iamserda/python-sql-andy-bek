import sqlite3

# create a connection to an existing database
# If database is not found, it creates it then connect to that db.
conn = sqlite3.connect("base2.db")  # object type -> sqlite3.Connection

# cursor: control structure that enables traversal of records in the database
# We use it to execute commands: create, update, delete, read data from database records.
cursor = conn.cursor()

try:
    cursor.execute(
        """
    CREATE TABLE ice_cream_flavors(
    id INTEGER PRIMARY KEY,
    flavor TEXT,
    rating DOUBLE(4,2));
    """
    )
except Exception as e:
    pass

cursor.execute(
    """
    INSERT INTO ice_cream_flavors (flavor, rating)
    VALUES ('strawberry', 7.99),
    ('Vanilla', 9.25), 
    ('Chocolate', 8.90), 
    ('Café', 8.50), 
    ('Lemon', 5.00);
    """
)
conn.commit()
