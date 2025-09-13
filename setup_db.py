# for json file handling
import json
# for sql database handling
import sqlite3

# setting up database with json config file
DATABASE = "ppab6.db"

def add_credentials(cur):
  with open('credentials.json', 'r') as file:
    data = json.load(file)
  for user in data['credentials']:
    command = "INSERT INTO users VALUES ('" + user['username'] + "', '" + user['password_hash'] + "')"
    cur.execute(command)
    
if __name__ == "__main__":
  # create file
  connection = sqlite3.connect(DATABASE)
  cur = connection.cursor()
  cur.execute("CREATE TABLE users(username, password)")
  res = cur.execute("SELECT name FROM sqlite_master")
  # modify and close connection
  add_credentials(cur)
  connection.commit()
  connection.close()