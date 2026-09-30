import threading

balance = 1000
balance_lock = threading.Lock()


def withdraw(amount):
    global balance

    with balance_lock:
        if amount <= balance:
            balance -= amount

            print(
                f"Withdrawn: {amount}"
            )

        else:
            print("Insufficient balance")

withdraw(300)


