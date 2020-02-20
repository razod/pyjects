from yolo import yolo

y = yolo()

def initSession(countrycode, phonenumber):
    y.sendVerfCode(countrycode,phonenumber)
    i = str(input("code? "))
    y.loginWithVerfCode(i)
    print(y.getSessionToken())

def getSession():
    return print(y.getSessionToken())

# get the info for your yolo profile
def myInfo():
    print(y.selfInfo())

# get the info for someones yolo profile
def getInfo(usr):
    print(y.getUser(usr))

# sends a message to someone else's yolo
def sendMsg(usr, msg):
    y.sendMessage(usr, msg)

# get 100 last messages on your yolo
def lastMsgs():
    print(y.getMessages(0))

initSession(1, 8880000000)
myInfo()
lastMsgs()