class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalidTransactions = []
        user_transactions = collections.defaultdict(list)

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            user_transactions[name].append([int(time), city])

        def secondTransactionExist(name, time, city):
            for otherTransactions in user_transactions[name]:
                otherTransactionsTime, otherTransactionsCity = otherTransactions
                if otherTransactionsCity != city and abs(time - otherTransactionsTime) <= 60:
                    return True
            return False

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")

            if int(amount) > 1000 or secondTransactionExist(name, int(time), city):
                invalidTransactions.append(transaction)      

        return invalidTransactions

    # TC: O(N^2)
    # SC: O(N)