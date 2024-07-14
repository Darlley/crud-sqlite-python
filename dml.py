"""
DML - Manipulação de Dados
"""
import sqlite3

def commit_close(func):
  def decorator(*args):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    sql = func(*args)
    cur.execute(sql)
    con.commit()
    con.close()
  return decorator

@commit_close
def db_insert(name, phone, email):
  return """
  INSERT INTO users(name, phone, email) 
    VALUES('{}', '{}', '{}')
  """.format(name, phone, email)

@commit_close
def db_updateName(id, name):
  return """
  UPDATE users SET name = '{}' WHERE id = '{}'
  """.format(name, id)

@commit_close
def db_updatePhone(id, phone):
  return """
  UPDATE users SET phone = '{}' WHERE id = '{}'
  """.format(phone, id)

@commit_close
def db_updateEmail(id, email):
  return """
  UPDATE users SET email = '{}' WHERE id = '{}'
  """.format(email, id)
  
@commit_close
def db_delete(id):
  return """
  DELETE FROM users WHERE id = '{}'
  """.format(id)

def db_select(data, field):
  con = sqlite3.connect('sqlite.db')
  cur = con.cursor()

  sql = """
    SELECT * FROM users WHERE {}={}
  """.format(field, data)
  
  cur.execute(sql)
  data = cur.fetchall()
  con.close()
  return data