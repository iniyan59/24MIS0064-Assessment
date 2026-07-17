def login_user(username, password):
    if username == "admin" and password == "secure123":
        print("Login successful!")
        return True
    print("Invalid credentials.")
    return False