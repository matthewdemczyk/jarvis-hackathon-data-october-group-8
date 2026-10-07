
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


if __name__ == '__main__':
        #set up collection of accounts
        account_list = []
        with open('accounts (1).csv', 'rt') as acct_file:
            datareader = csv.reader(acct_file)
            for line_num, line in enumerate(datareader):
                if line_num == 0: continue
                accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate = line
                account_to_add = Account(accountId,customerName,accountType,status,balance,dailyLimit,currency,openedDate)
                account_list.append(account_to_add)