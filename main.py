from pathlib import Path
import json
import string
import random
from bank import Bank


bank=Bank()
while True:
    print("\n___________BANK MANAGEMENT SYSTEM___________")
    print("1. Create Account \n"   #done
    "2. View Accounts \n"   
    "3. Search Account \n"   
    "4. Deposit Money \n"    
    "5. Withdraw Money \n"   
    "6. Transfer Money \n"   
    "7. Check Balance \n"    
    "8. Update Account \n"   
    "9. Delete Account \n"   
    "10. Richest Account \n"    
    "11. Low Balance Accounts \n"    
    "12. Total Bank Balance  \n"   
    "13. Add Interest \n"  #done
    "14. Get Account Trasaction History (Statement)\n"   
    "15. Get Particular Transaction Details\n"
    "16. Exit\n") 
    ch=int(input("Enter choice:"))

    if ch==1:
        bank.createAccount()
    elif ch==2:
        bank.viewAccount()
    elif ch==3:
        bank.searchAcc()
    elif ch==4:
        bank.deposit()
    elif ch==5:
        bank.withdraw()
    elif ch==6:
        bank.transfer()
    elif ch==7:
        bank.checkBalance()
    elif ch==8:
        bank.update()
    elif ch==9:
        bank.delete()
    elif ch==10:
        bank.richestAcc()
    elif ch==11:
        bank.lowBalance()
    elif ch==12:
        bank.totalBankBalance()
    elif ch==13:
        bank.interest()
    elif ch==14:
        bank.Transaction()    
    elif ch==15:
        bank.fetchTransaction()
    elif ch==16:
        print("Terminating !!!")
        break
    else:
        print("Invalid choice")


