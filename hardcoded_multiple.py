# checking against multiple hardcoded credentials
credentials = {"magdalene": "marathon", "conrad": "shard", "nicho": "spheres"}

def check_password(username, password):
  valid = 0
  for user in credentials:
    if username == user:
      if password == credentials[user]:
        valid = 1
  return (valid == 1)
    
if __name__ == "__main__":
  username = str(input("username? "))
  password = str(input("password? "))
  if check_password(username, password):
    print("You're logged in! Here's a secret!")
  else:
    print("Incorrect credentials")