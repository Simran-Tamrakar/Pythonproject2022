
MYDB= mysql.connector.connect(host='localhost',user='root',password='1234',database='Bank_Management_System')

def OpenAccount():
    name = input("Enter your name: ")
    account = input("Enter your Bank mandated account number: ")
    age = input("Enter your date of birth: ")
    address = input("Enter your residential address: ")
    contact = input("Enter your contact information: ")
    OBalance = input("Enter your starting balance: ") 
    Data_A = (name,account,age,address,contact,OBalance)
    Data_A1 = (name,account,OBalance)
    sql_A = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql_A1 = ('insert into account values (%s,%s,%s)')
    x = MYDB.cursor()
    x.execute(sql_A,Data_A)
    x.execute(sql_A1,Data_A1)
    MYDB.commit()
    print("Data Entered Successfully!") 
    main()

def DepositMoney():
    amount = input("Enter the amount of money you wish you deposit: ")
    account = input("Enter your account number: ")
    a = 'select balance from amount where AccNo = %s'
    data = (account,) 
    x = MYDB.cursor()
    x.execute(a,data)
    Result = x.fetchone()
    T_variable = Result[0] + amount
    sql = ('update amount set balance where AccNo = %s')
    D = (T_variable, account)
    x.execute(sql,D)
    MYDB.commit()
    main()

def WithdrawMoney():
    amount = input("Enter the amount of money you wish you deposit: ")
    account = input("Enter your account number: ")
    a = 'select balance from amount where AccNo = %s'
    data = (account,) 
    x = MYDB.cursor()
    x.execute(a,data)
    Result = x.fetchone()
    T_variable = Result[0] - amount
    sql = ('update amount set balance where AccNo = %s')
    D = (T_variable, account)
    x.execute(sql,D)
    MYDB.commit()
    main()

def Inquire():
    account = input("Enter your account number: ")
    a = 'select * from amount where AccNo = %s'
    data = (account,)
    x = MYDB.cursor()
    x.execute(a,data)
    Result = x.fetchone()
    print("The balance remaining in account number: ", account,"is", Result[-1])
    main()
    
def DisplayInfo():
    account = input("Enter your account number: ")
    a = 'select * from amount where AccNo = %s'
    data = (account,)
    x = MYDB.cursor()
    x.execute(a,data)
    Result = x.fetchone()
    for i in Result:
        print(i)
    main()
    
def DeleteAcc():
    account = input("Enter your account number: ")
    sql_A = 'delete from account where AccNo = %s'
    sql_A1 = 'delete from account where AccNo = %s'
    data = (account,)
    x = MYDB.cursor()
    x.execute(sql_A, data)
    x.execute(sql_A1,data)
    MYDB.commit()
    main()


def main():
    print( '''
Hello! Welcome to XYZ Bank. How may we be of service today?
          
            1. Open a New Bank Account
            2. Deposit Money
            3. Withdraw Money
            4. Inquire Bank Balance
            5. Display Personal Information
            6. Delete Bank Account''')
    
    choice = input("Enter the number corresponding to the task you wish to perform: ")
    if(choice == 1):
        OpenAccount();
    elif(choice == 2):
        DepositMoney();
    elif(choice == 3):
        WithdrawMoney();
    elif(choice == 4):
        Inquire();
    elif(choice == 5):
        DisplayInfo();
    elif(choice == 6):
        DeleteAcc();
    else:
        print('No Task corresponds to that number')
        main()

main()