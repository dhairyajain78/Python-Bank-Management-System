import random
import string
import json
from datetime import datetime 
from pathlib import Path
class Bank:
    database='accounts.json'
    transactions='transaction.json'
    data = []
    logs=[]

    try:
        if Path(database).exists():
            with open (database) as fs , open (transactions) as ts:
                data= json.loads(fs.read())
                logs= json.loads(ts.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"ERROR OCCURED: {err}")
    
    @classmethod
    def __updatedatabase(cls):
        with open (cls.database,"w") as fs:
            json.dump(cls.data, fs , indent=4)


    @classmethod
    def __updatetransaction(cls):
        with open (cls.transactions,"w") as fs:
            json.dump(cls.logs, fs, indent=4)


    @classmethod
    def __generateAC(cls):
        while True:
            id="".join(
                random.choices(string.ascii_uppercase,k=4)+
                random.choices(string.digits,k=10)
            )
            exists = any(acc['accountNo']==id for acc in Bank.data)
            if not exists:
                return id
    @classmethod
    def __ifscgenerate(cls):
        id="".join(
             random.choices(string.ascii_uppercase,k=4)+
             random.choices(string.digits,k=8)
        )
     
        exists = any(i['ifsc']==id for i in Bank.data)
        if not exists :
            return id
        
    @classmethod
    def __Transactionid(cls):
        id="T"+"".join(
            random.choices(string.digits,k=10)
        )
        exists= any(i['T_ID']==id for i in Bank.logs)
        if not exists:
            return id

    def createAccount(self):
        print("Enter your Details:")
        ifscno=Bank.__ifscgenerate()
        accno=Bank.__generateAC()
        info={
            'name':input("Name: "),
            'age':int(input("Age: ")),
            'email':input("Email: "),
            'pin':int(input("enter 4 digit pin: ")),
            'balance':int(input("Enter initial Balance: ")),
            'accountNo':accno,
            'ifsc':ifscno
        }

        if info['age'] < 18 or len(str(info['pin'])) !=4 or info['balance'] <0 :
            print("Can't create account")
        else:
            print("account created succesfully\n")
            print("Your details are:\n")
            for i in info:
                print(f"{i} : {info[i]}")
            print(f"Note your A/C Number :{accno} and IFSC Code :{ifscno}")
            Bank.data.append(info)
            Bank.__updatedatabase()



    def viewAccount(self):
        n=3
        found=False
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin
                ]

            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")
        else:
            print("Your Details are:\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}\n")
            

    def searchAcc(self):
        n=3
        found=False
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")
        else:
            print ("Account found ")
            print("Your Details are:\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}\n")
        
        
    def deposit(self):
        n=3
        found=False
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        if found==True:
            oldbal=userdata[0]['balance']
            amount=int(input("enter amount to deposit: "))
            if amount >10000 or amount < 0:
                print("enter amount within range of 0-10000")
            else:
                userdata[0]['balance']+=amount
                Bank.__updatedatabase()
                print("Balance Updated")
                newbal=userdata[0]['balance']
                print(newbal)
                print( self.statement(accno,oldbal,newbal))
           
        
        

    def withdraw(self):
        n=3
        found=False
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        if found==True:

            oldbal=userdata[0]['balance']
            amount=int(input("enter amount to withdraw: "))
            if amount > userdata[0]['balance']:
                print("Insufficient Balance !")
            else:
                userdata[0]['balance']-=amount
                Bank.__updatedatabase()
                print("Amount Withdrawn \nBalance updated")
                newbal=userdata[0]['balance']
                print(self.statement(accno,oldbal,newbal))
                            
            # n-=1

    def transfer(self):
        userdata=[]
        n=3
        found=True
        while  n>0:
            D_accno=input("Enter Debit A/C no: ")
            pin=int(input("Enter Debit A/C pin: "))
          
            for i in Bank.data:
                if i['accountNo']==D_accno and i['pin']==pin :
                    userdata.append(i)            
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        else:
            C_accno=input("Enter Credit A/C no: ")
            
            for i in Bank.data:
                if i['accountNo']==C_accno :
                    userdata.append(i)

            
            if not userdata:
                print("Data not found!")
            else:
                C_oldbal=userdata[0]['balance']
                D_oldbal=userdata[1]['balance']

                amt=int(input("Enter Debit Amount"))
                if amt>userdata[0]['balance']:
                    print("Insufficiant Balance\n Transaction Failed!!!!")
                else:
                    userdata[0]['balance']-=amt
                    userdata[1]['balance']+=amt
                    
                    Bank.__updatedatabase()
                    print("Transaction Successfull !")
                D_newbal=userdata[0]['balance']
                C_newbal=userdata[1]['balance']
                print(self.statement(D_accno,D_oldbal,D_newbal))
                self.statement(C_accno,C_oldbal,C_newbal)
        

    def checkBalance(self):
       
        n=3
        found=True
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        else:
            print(f"Available Balance : {userdata[0]['balance']}")
          

    def update(self):
        n=3
        found=True
        while n >0 :
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        else:
            print("You can Update:\n" 
            "1.Account Holder Name\n"
            "2.Pin\n" 
            "3.Email\n")
            print("Enter Details to Update:")
            new={
                'name':input("Enter new name or press enter to skip "),
                'pin': input("Enter new 4 digit pin or press enter to skip "),
                'email':input("Enter new Email or press enter to skip ")
            }
            if new['name']!="":
                userdata[0]['name']=new['name']
            if new['pin']!="":
                userdata[0]['pin']=new['pin']
            if new['email']!="":
                userdata[0]['email']=new['email']
            Bank.__updatedatabase()
            print("Updated succesfully!")
            
    
    def delete(self):
        n=3
        found=True
        while n>0:
            accno=input("Enter your A/C no: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data 
                if i['accountNo']==accno and i['pin']==pin 
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")

        else:
            choice=input(" Press Y to Delete Account\n"
                        " Press N to Exit")
            if choice.lower()=='y':
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)

                Bank.__updatedatabase()
                print("Deleted Successfully!")
        

    def statement(self,accno,old,new):
        print("___Transaction Statement___")
        T_id= Bank.__Transactionid()
        now=datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        log={
            'accountNo':accno,
            'Old Balance': old,
            'New Balance':new,
            'Date': date,
            'Time': time,
            'T_ID':T_id
            }
        Bank.logs.append(log)
        Bank.__updatetransaction()
        if old > new:
            return(f"{old - new} amount debited from your account {accno} on {date} at {time} \n"
                   f"Transaction ID : {T_id}")
        else:
            return(f"{new - old} amount credited into your account {accno} on {date} at {time} \n"
                   f"Transaction ID : {T_id}")
     

    def richestAcc(self):
        highest=0
      
        for i in Bank.data:
            if i['balance']>highest:
                highest=i['balance']
                name=i['name']
        print(f"Richest Account Balance:{highest}")
        print(f"Account Holder Name: {name}")


    def lowBalance(self):
        print("Low Balnce Accounts:")
        for i in Bank.data:
            if i['balance']<=10000:
                print(f"Account Holder Name:{i['name']}\n"
                      f"Account Number:{i['accountNo']}")
                

    def totalBankBalance(self):
        total=0
        for i in Bank.data:
            total+=i['balance']
        print(f"Total Bank Balance : {total}")

    def interest(self):
        n=3
        found=True
        while n>0:
            accno=input("Enter your A/C Number: ")
            pin=int(input("Enter your pin: "))
            userdata=[
                i for i in Bank.data
                if i['accountNo']==accno and i['pin']==pin
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")
        else:
            Interest = userdata[0]['balance']*0.075
            print(f"Interest on Balance:{userdata[0]['balance']} = {Interest}")
  

    def Transaction(self):
        n=3
        found=True
        while n>0:
            accno=input("Enter your A/C no: ")
            userdata=[
                i for i in Bank.logs 
                if i['accountNo']==accno
            ]
            if userdata:
                found=True
                break
            else:
                n-=1
                print(f"Wrong Credentials . Attempts left :{n}")
        if not found:
            print("Account Locked!!")
        else:
            print ("\nYour Transaction History is :\n")
            for i in Bank.logs:
                if i['accountNo']==accno:  
                    print( f"{i}\n" )


    def fetchTransaction(self):
        tid=input("Enter Transaction Id : ")
        for i in Bank.logs:
            if tid==i['T_ID']:
                print("Transaction Details : \n" , i )
                break
        else:
            print ("No Record Found !")            

