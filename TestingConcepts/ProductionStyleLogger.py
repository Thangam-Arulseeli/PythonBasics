### Custom Exceptions
### For larger applications, define meaningful exceptions.
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    return balance - amount

# User
try:
    balance = withdraw(5000, 10000)

except InsufficientBalanceError as ex:
    print(ex)

# Output:
# Insufficient account balance
# ===============================

### Logging an Exception with Context

### A production-style example:
import logging

logger = logging.getLogger(__name__)

class InsufficientBalanceError(Exception):
    pass

def withdraw(account_id, balance, amount):

    logger.info(
        "Withdrawal requested account_id=%s amount=%s",
        account_id,
        amount
    )

    if amount > balance:

        logger.warning(
            "Insufficient balance account_id=%s balance=%s amount=%s",
            account_id,
            balance,
            amount
        )

        raise InsufficientBalanceError(
            "Insufficient balance"
        )

    balance -= amount

    logger.info(
        "Withdrawal successful account_id=%s remaining_balance=%s",
        account_id,
        balance
    )

    return balance

amount = withdraw(1001, 5000, 10000)
print("Remaining Balance:", amount)


###This gives useful business context without needing to attach a debugger to the running application.



