print("----------------MENU---------------")
print("press 1 to creat twitter account")
print("press 2 to view profile")
print("press 3 to update twitter profile")
print("press 4 to retrive particular information")
print("press 5 to delete details of particular account")
print("press 6 to exit")
class twitter:
            def gettwitterDetails(self):
                self.age=int(input("Enter age : "))
                self.username = input("Enter username : ")
                self.mail = input("Enter user mail : ")
                self.password = input("Enter user password : ")
                self.gender = input("Enter gender : ")
            def printprofile(self):
                print(self.age,self.username,self.mail,self.password,self.gender)
            def get_age(self):
                return self.age
data=[]
def find(val):
    for i in data:
        if(i.get_age()==val):
            return i
def retirve():
    for i in data:
        i.printprofile()
def delete(val):
    for i in data:
        if(i.get_age()==val):
            data.remove(i)
def modify(val):
    print("----------------MENU---------------")
    print("1.age")
    print("2.username")
    print("3.mail")
    print("4.password")
    print("5.gender")
    n=int(input("enter your choice to modify :"))
    for i in data:
         if(i.get_age()==val):
            new=input("enter new value : ")
            if(n==1):
                i.age=int(new)
            elif(n==2):
                i.username=new
            elif(n==3):
                i.mail=new
            elif(n==4):
                i.password=new
            elif(n==5):
                i.gender=new
            break
while(True):
    a=int(input("enter the choice:-"))
    T1=twitter()           
    if a==1:
        T1.gettwitterDetails()
        data.append(T1)
    elif a==2:
            retirve()
    elif a==3:
        val=int(input("enter user age to modify :"))
        modify(val)
    elif a==4:
        val=int(input('enter user age : '))
        st=find(val)
        st.printprofile()
    elif a==5:
        val=int(input("enter user age to delete details :"))
        delete(val)
    else:
        break