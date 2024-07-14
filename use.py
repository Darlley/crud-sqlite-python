from dml import db_insert, db_delete, db_updateName, db_updatePhone, db_updateEmail, db_select
from pprint import pprint

# db_delete(4)
# db_delete(5)
# db_delete(6)
# db_delete(7)
# db_delete(8)

db_insert('fulano', '5567999999999', 'fulano@mail.com')
db_insert('ciclano', '5567999999999', 'ciclano@mail.com')
db_insert('beltrano', '5567999999999', 'beltrano@mail.com')
db_insert('Jane Doe', '5567999999999', 'jane_doe@mail.com')
db_insert('John Doe', '5567999999999', 'john_doe@mail.com')

# pprint(db_select('5567999999999', 'phone'))