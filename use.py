from dml import db_insert, db_delete, db_updateName, db_updatePhone, db_updateEmail, db_select
from pprint import pprint

# db_delete(1)
# db_delete(3)

# db_insert('fulano', '5567993328678', 'fulano@mail.com')
# db_insert('ciclano', '5567993328678', 'ciclano@mail.com')
# db_insert('beltrano', '5567993328678', 'beltrano@mail.com')
# db_insert('Jane Doe', '5567993328678', 'jane_doe@mail.com')
# db_insert('John Doe', '5567993328678', 'john_doe@mail.com')

pprint(db_select('5567993328678', 'phone'))