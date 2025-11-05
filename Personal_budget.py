import datetime 

class Transactions:
    def __init__(self, amount, type, description):
        self.amount = amount
        self.type = type
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.description = description
        
    def __str__(self):
        return f'${self.amount} | {self.type} | {self.date} | {self.description}'    
    
    def __repr__(self):
        return self.__str__()
    
    def save_to_file(self, filename='transaction.txt'):
       with open(filename, 'a') as file:
          line = f'{self.amount} | {self.type} | {self.date} | {self.description}\n'
          file.write(line)

# Adding Transaction
def add_transaction():
   while True:
      amount_input =  input('How much is the amount?')
      try: 
         amount_input = float(amount_input)
         break
      except ValueError:
       print('Please enter a valid number for the amount.')
 
   transaction_type_list =['INCOME','EXPENSE']
   while True: 
      transaction_type = input('Is it income or expense?').upper().strip()
      if transaction_type not in transaction_type_list:
        print('❌ Please Choose the right type of transaction!')
      else: 
         break

   description = input('What is the Description?') 
   return amount_input, transaction_type, description

# Viewing Transaction History
def transaction_history(filename='transaction.txt'):
   try:
      with open(filename, 'r') as file:
         lines = file.readlines()
         if not lines:
            print('\n❌No transactions found.')
            return
         
         for line in lines: 
            amount, transaction_type, date, description = line.strip().split(' | ', 3)
            print(f'{amount} | {transaction_type} | {date} | {description} ')
   except FileNotFoundError:
      print('\n❌No transaction file found')

# Total Balanace Viewing
def total_balance(filename='transaction.txt'):
   total_income = 0
   total_expense = 0
   try:
      with open(filename, 'r') as file:
         for line in file: 
               amount, transaction_type, date, description = line.strip().split('|', 3)
               if transaction_type.upper() == 'INCOME':
                  total_income += amount
               elif transaction_type.upper() == 'EXPENSE':
                  total_expense += amount
                  
      net_balance = total_income - total_expense

      print('\n💰 Balance Summary: ')
      print(f'Total Income: ${total_income}')
      print(f'Total Expense: ${total_expense}')
      print(f'Balance : ${net_balance:}\n')

   except FileNotFoundError:
       print('\n❌No Transaction file found.')

# Transaction Deletion Feature
def delete_tranasction(filename='transaction.txt'):
   try: 
      with open(filename, 'r') as file:
         transaction_list = file.readlines()
         for index, line in enumerate(transaction_list):
            print(f'{index}: {line.strip()}')
   except FileNotFoundError:
      print('❌Transaction file not found')

   while True:
      user_choice = input('Which transaction would like to delete? Choose the Index: ')
      
      if not user_choice:
         print('\n❌ Input can not be empty. Choose the number before the transaction.')
      try: 
         user_choice = int(user_choice)
         if 0 <= user_choice < len(transaction_list):
          break
         else: 
            print('Invalid index! Please Choose a number form the list. ')
      except ValueError:
         print('❌Invalid Input. Only integer numbers are allowed.\n')

   del transaction_list[user_choice]

   with open(filename, 'w') as file: 
      for line in transaction_list:
         file.write(line)

   print('✅Transaction deleted succecsfully!!')
  
def main_menu():
   print('\n WELCOME TO THE PERSONAL BUDGET MANAGER!')
   while True:
      
      choices = ['1 : Add a Transaction', 
                 '2 : View all transactions', 
                 '3 : Total Balance',
                 '4 : Delete a transaction',
                 '5 : Exit']
      for choice in choices: 
         print(f'\n{choice}')

      user_choice = input('\nEnter Your Choice: ').strip()

      try: 
         user_choice = int(user_choice)
      except ValueError:
         print('Please Enter a number (1, 2, or 3).')
         continue

      if user_choice == 1:
         amount, type_, description = add_transaction()
         t = Transactions(amount, type_, description)
         t.save_to_file()
         print('\n✅Transaction Added!')

      elif user_choice == 2:
         transaction_history()

      elif user_choice == 3:
         total_balance()
      
      elif user_choice == 4:
         delete_tranasction()
         
      elif user_choice == 5:
         print('Exiting... Goodbye!')
         break
      else: 
         print('❌Invalid choice. (1, 2, 3, 4 or 5).')

if __name__ == '__main__': 
   main_menu()


 
 



