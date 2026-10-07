
import csv
from datetime import datetime

class Account:

    def __init__(
            self,
            accountId,
            customerName,
            accountType,
            status,
            balance,
            dailyLimit,
            currency,
            openedDate):
        self.accountId = accountId
        self.customerName = customerName
        self.accountType = accountType
        self.status = status
        self.balance = float(balance)
        self.dailyLimit = float(dailyLimit)
        self.currency = currency
        self.openedDate = openedDate

    def decrease_balance(self, amount):
         self.balance -= amount
         #self.dailyLimit -= amount
    def increase_balance(self, amount):
        self.balance += amount

if __name__ == '__main__':
        #set up collection of accounts
        account_list = []
        account_ids_that_exist = set()
        with open('accounts (1).csv', 'rt') as acct_file:
            datareader = csv.reader(acct_file)
            for line_num, line in enumerate(datareader):
                if line_num == 0: continue #skip first line, which is column names
                accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate = line
                account_to_add = Account(accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate)
                account_ids_that_exist.add(accountId)
                account_list.append(account_to_add)

        approved = 0
        rejected = 0
        flagged = 0
        
        #begin processing transactions
        list_of_transaction = []
        list_of_flags = []
        previous_datetime = None

        with open('transactions (1).csv', 'rt') as trx_file:
            datareader = csv.reader(trx_file)
            transactions_processed = set()
            for line_num, line in enumerate(datareader):
                if line_num == 0: continue #skip column names line
                transactionId,timestamp,type,fromAccount,toAccount,amount,channel,description = line
                amount = amount.replace('O', '0')
                amount = float(amount)
                if fromAccount != '':
                    from_account_array_index = int(fromAccount[4:7])-1
                else:
                     from_account_array_index = None
                if toAccount != '':
                    to_account_array_index = int(toAccount[4:7])-1
                else:
                    to_account_array_index = None
                #print(fromAccount,from_account_array_index)
                valid = True

                #print(fromAccount, from_account_array_index, toAccount, to_account_array_index)                
                #have if statements for the various cases here
                #if (from_account_array_index == None or to_account_array_index == None or from_account_array_index < 0 or from_account_array_index >= len(account_list) or to_account_array_index < 0 or to_account_array_index >= len(account_list)):
                if from_account_array_index != None and fromAccount not in account_ids_that_exist:
                    valid = False
                    reason = 'From account does not exist'
                if to_account_array_index != None and toAccount not in account_ids_that_exist:
                    valid = False
                    reason = 'To account does not exist'
                if to_account_array_index == None and from_account_array_index == None:
                    valid = False
                    reason = "No accounts given for transaction"
                if valid and ((from_account_array_index != None and (account_list[from_account_array_index].status == 'FROZEN' or account_list[from_account_array_index].status == 'CLOSED')) or (to_account_array_index != None and (account_list[to_account_array_index].status == 'FROZEN' or account_list[to_account_array_index].status == 'CLOSED'))):
                    valid = False
                    reason = 'Account is inactive'
                if float(amount) <= 0:
                    valid = False
                    reason = 'Amount <= 0'
                if transactionId in transactions_processed:
                    valid = False
                    reason = 'Transaction ID already processed'
                if valid and (from_account_array_index != None and account_list[from_account_array_index].balance < float(amount)):
                    valid = False
                    reason = 'Insufficient balance'


                if valid:
                    if float(amount) > 10000:
                        #print (transactionId, " Approved but flagged")
                        list_of_flags.append(f'{transactionId} Large amount')
                        flagged += 1
                    #current_time = datetime(timestamp)
                    
                    #print (transactionId, " Approved")
                    approved += 1
                    #process the transactions
                    #deposit, purchase, transfer, reversal withrawl
                    if type == 'DEPOSIT':
                       account_list[to_account_array_index].increase_balance(float(amount))
                    if type == 'PURCHASE':
                        account_list[from_account_array_index].decrease_balance(float(amount))
                        if amount > account_list[from_account_array_index].dailyLimit:
                            flagged += 1
                            list_of_flags.append(f'{transactionId} Amount larger than daily limit')
                    if type == 'TRANSFER':
                        account_list[to_account_array_index].increase_balance(float(amount))
                        account_list[from_account_array_index].decrease_balance(float(amount))
                        if amount > account_list[from_account_array_index].dailyLimit:
                            flagged += 1
                            list_of_flags.append(f'{transactionId} Amount larger than daily limit')
                    if type == 'REVERSAL':
                        account_list[from_account_array_index].increase_balance(float(amount))
                    if type == 'WITHDRAWAL':
                        account_list[from_account_array_index].decrease_balance(float(amount))
                        if amount > account_list[from_account_array_index].dailyLimit:
                            flagged += 1
                            list_of_flags.append(f'{transactionId} Amount larger than daily limit')
                    list_of_transaction.append(f'{transactionId} APPROVED')

                else:
                    #print (transactionId, " Rejected")
                    rejected += 1
                    list_of_transaction.append(f'{transactionId} REJECTED - {reason}')
                transactions_processed.add(transactionId)
                #previous_datetime = datetime(timestamp)
            print("Approved: " + str(approved), "\nRejected: " + str(rejected), "\nApproved but flagged: " + str(flagged))
        with open("transaction_approval.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list_of_transaction) + "\n")
        with open("transaction_flags.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(list_of_transaction) + "\n")
        
