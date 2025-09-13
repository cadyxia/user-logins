# for SHA256 hashing
import hashlib
# for sql database handling
import sqlite3
# for hiding password
from getpass import getpass

# checking against query from sql database (passwords hashed)
DATABASE = "ppab6.db"

def hash_sha256(plaintext):
  result = hashlib.sha256(plaintext.encode())
  return result.hexdigest()

def check_credentials(username, password):
  connection = sqlite3.connect(DATABASE)
  cur = connection.cursor()
  command = "SELECT * FROM users WHERE username = ?"
  res = cur.execute(command, (username,)).fetchone()

  valid = 0
  if res != None:
    if res[1] == hash_sha256(password):
      valid = 1

  connection.close()
  return (valid == 1)
    
if __name__ == "__main__":
  username = str(input("Username? "))
  password = getpass("Password? ")
  if check_credentials(username, password):
    print("You're logged in! Here's a secret!")
  else:
    print("Incorrect credentials")