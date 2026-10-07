
import csv

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
        self.balance = balance
        self.dailyLimit = dailyLimit
        self.currency = currency
        self.openedDate = openedDate

    def decrease_balance(self, amount):
         self.balance -= amount
    def increase_balance(self, amount):
        self.balance += amount

if __name__ == '__main__':
        #set up collection of accounts
        account_list = []
        with open('accounts (1).csv', 'rt') as acct_file:
            datareader = csv.reader(acct_file)
            for line_num, line in enumerate(datareader):
                if line_num == 0: continue #skip first line, which is column names
                accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate = line
                account_to_add = Account(accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate)
                account_list.append(account_to_add)

        #begin processing transactions
        with open('transactions (1).csv', 'rt') as trx_file:
            datareader = csv.reader(trx_file)
            for line_num, line in enumerate(datareader):
                if line_num == 0: continue #skip column names line
                transactionId,timestamp,type,fromAccount,toAccount,amount,channel,description = line
                if fromAccount != '':
                    from_account_array_index = int(fromAccount[4:7])-1
                else:
                     from_account_array_index = None
                if toAccount != '':
                    to_account_array_index = int(toAccount[4:7])-1
                else:
                    to_account_array_index = None
                print(fromAccount,from_account_array_index)
                valid = True
                #have if statements for the various cases here
                if valid:
                     #process the transactions
                     pass
