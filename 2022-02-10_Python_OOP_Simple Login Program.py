# simple login program in python-Object and class-OOP
#Computer Programming Tutor- March 4, 2021

class login:
    def __init__(self,id,pas):
        self.id="admin"
        self.pas="admin"

    def check(self,id,pas):
        print(id)
        print(pas)
        if(self.id==id and self.pas==pas):
            print("Login Success!!!")
            print("Login Page")

        else:
            print("Invalid Username or Password")


log = login("","")
id1=input("Enter Login ID: ")
pas1=input("Enter Password: ")
log.check(id1,pas1)



