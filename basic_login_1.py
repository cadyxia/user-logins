# checking hardcoded credentials
def check_password(username, password):
  return (username == "robert" and password == "password123")
    
if __name__ == "__main__":
  username = str(input("username? "))
  password = str(input("password? "))
  if check_password(username, password):
    print("You're logged in! Here's a secret!")
  else:
    print("Incorrect credentials")