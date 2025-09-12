# for SHA256 hashing
import hashlib

# checking against multiple hardcoded credentials (passwords hashed)
CREDENTIALS = {"magdalene": "6d205806e19dba5306a09df6e5b7205737f301bfaf15086e20200f356eb9ccef", 
               "conrad": "df3598cd66f1bb5bc4e2c17be89b7c7ecf0c81e53939f471a6b72db8d139edae", 
               "nicho": "5a033573f153df4e7cdc69d6cf4e94e46bd773a2af3a52936a97de4a5bb8a8e5"}

def hash_sha256(plaintext):
  result = hashlib.sha256(plaintext.encode())
  return result.hexdigest()

def check_credentials(username, password):
  valid = 0
  for user in CREDENTIALS:
    if username == user:
      if hash_sha256(password) == CREDENTIALS[user]:
        valid = 1
  return (valid == 1)
    
if __name__ == "__main__":
  username = str(input("username? "))
  password = str(input("password? "))
  if check_credentials(username, password):
    print("You're logged in! Here's a secret!")
  else:
    print("Incorrect credentials")