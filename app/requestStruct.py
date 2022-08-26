def Register():
    schema = {
        "userName": str,
        "userEmail": str,
        "userFirstName": str,
        "userLastName": str,
        "userPhoneNumber": str,
        "userPassword1": str,
        "userPassword2": str
    }
    return schema

def Login():
    schema = {
        "userName": str,
        "userPassword": str
    }
    return schema

def Task():
    schema = {
        "taskName": str,
        "taskDetail": str
    }
    return schema