import asyncio
import time

# Simulated asynchronous microservice calls
async def fetch_product_details():
    await asyncio.sleep(1.0)
    return {"product_id": 101, "name": "Cloud Server Plan"}

async def fetch_inventory_status():
    await asyncio.sleep(1.5)
    return {"stock": 42, "warehouse": "US-East"}

async def fetch_user_reviews():
    await asyncio.sleep(0.8)
    return [{"rating": 5, "comment": "Excellent service!"}]

async def main():
    start_time = time.time()
    print("Fetching dashboard data concurrently...")

    # Non-blocking concurrent execution of all 3 API requests
    results = await asyncio.gather(
        fetch_product_details(),
        fetch_inventory_status(),
        fetch_user_reviews()
    )

    product, inventory, reviews = results

    print("\n--- Dashboard Payload Received ---")
    print("Product:", product)
    print("Inventory:", inventory)
    print("Reviews:", reviews)
    print(f"Total Fetch Time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
