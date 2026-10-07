
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