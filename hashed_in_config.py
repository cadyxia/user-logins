# for SHA256 hashing
import hashlib
# for json handling
import json

# checking against multiple credentials from config file (passwords hashed)

def hash_sha256(plaintext):
  result = hashlib.sha256(plaintext.encode())
  return result.hexdigest()

def check_credentials(username, password):
  with open('credentials.json', 'r') as file:
    data = json.load(file)
  valid = 0
  for user in data['credentials']:
    if username == user['username']:
      if hash_sha256(password) == user['password_hash']:
        valid = 1
  return (valid == 1)
    
if __name__ == "__main__":
  username = str(input("username? "))
  password = str(input("password? "))
  if check_credentials(username, password):
    print("You're logged in! Here's a secret!")
  else:
    print("Incorrect credentials")