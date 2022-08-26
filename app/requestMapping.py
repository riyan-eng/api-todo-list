def Register(bodyJson):
    data = {
        "userName":bodyJson["userName"],
        "userEmail":bodyJson["userEmail"],
        "userFirstName": bodyJson["userFirstName"],
        "userLastName": bodyJson["userLastName"],
        "userPhoneNumber": bodyJson["userPhoneNumber"],
        "userPassword1": bodyJson["userPassword1"],
        "userPassword2": bodyJson["userPassword2"]
    }
    return data

def Login(bodyJson):
    data = {
        "userName": bodyJson["userName"],
	    "userPassword": bodyJson["userPassword"]
    }
    return data

def Task(bodyJson):
    data = {
        "taskName": bodyJson["taskName"],
	    "taskDetail": bodyJson["taskDetail"]
    }
    return data