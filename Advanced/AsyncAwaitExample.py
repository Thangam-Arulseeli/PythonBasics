import asyncio
import time

# Defining a Coroutine
async def verify_payment(transaction_id: str):
    print(f"Verifying transaction {transaction_id} with remote bank...")
    # Non-blocking pause simulating network latency
    await asyncio.sleep(1.5) 
    print(f"Transaction {transaction_id} VERIFIED.")
    return True

async def main():
    print("Starting checkout flow...")
    start_time = time.time()
    
    # Executing asynchronous coroutine
    status = await verify_payment("TXN_99182")
    
    print(f"Checkout finished in {time.time() - start_time:.2f}s with status: {status}")

# Running the Event Loop
if __name__ == "__main__":
    asyncio.run(main())



