# for SHA256 hashing
import hashlib
# for sql database handling
import sqlite3
# for hiding password
from getpass import getpass

# adding user credentials to existing sql database (passwords hashed)
DATABASE = "ppab6.db"

def hash_sha256(plaintext):
  result = hashlib.sha256(plaintext.encode())
  return result.hexdigest()

def add_user(username, password):
  connection = sqlite3.connect(DATABASE)
  cur = connection.cursor()
  pwd_hashed = hash_sha256(password)
  command = "INSERT INTO users VALUES (?, ?)"
  cur.execute(command, (username, pwd_hashed))
  connection.commit()
  connection.close()

def username_is_taken(username):
  connection = sqlite3.connect(DATABASE)
  cur = connection.cursor()
  command = "SELECT * FROM users WHERE username = ? "
  res = cur.execute(command, (username,)).fetchone()
  connection.close()
  return (res != None)
    
if __name__ == "__main__":
  username = str(input("username? "))
  while username_is_taken(username):
    print("This username is already taken. Please select a different one.")
    username = str(input("username? "))
  else:
    password = getpass("Password? ")
    add_user(username, password)
    print("User " + username + " added!")