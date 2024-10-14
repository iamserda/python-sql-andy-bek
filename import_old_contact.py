def import_old_contacts(my_connection):
    from contact_import import old_contacts as contact_records
    my_cursor = my_connection.cursor()
    # # Way 1:
    # for contact_record in contact_records:
    #     my_cursor.execute(
    #         "INSERT INTO contacts (first, last, email, phone) VALUES(:first,:last,:email,:phone)",
    #         contact_record
    #     )
    # WAY 2: BETTER
    my_cursor.executemany(
        "INSERT INTO contacts (first, last, email, phone) VALUES(:first,:last,:email,:phone)",
        contact_records
    )
    my_connection.commit()
