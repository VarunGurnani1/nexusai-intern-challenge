import asyncio
import random


# Simulate API calls (fake delays)
async def fetch_crm(customer_id: str):
    await asyncio.sleep(random.uniform(1, 3))
    return {
        "source": "crm",
        "customer_id": customer_id,
        "name": "Varun",
        "plan": "Premium"
    }


async def fetch_billing(customer_id: str):
    await asyncio.sleep(random.uniform(1, 3))
    return {
        "source": "billing",
        "customer_id": customer_id,
        "due_amount": 0,
        "last_payment": "2026-03-01"
    }


async def fetch_network(customer_id: str):
    await asyncio.sleep(random.uniform(1, 3))
    return {
        "source": "network",
        "customer_id": customer_id,
        "status": "down",
        "last_checked": "2026-03-17"
    }


# Main function (IMPORTANT)
async def fetch_all_data(customer_id: str):
    results = await asyncio.gather(
        fetch_crm(customer_id),
        fetch_billing(customer_id),
        fetch_network(customer_id),
        return_exceptions=True
    )

    # Handle errors safely
    final_data = {}
    for result in results:
        if isinstance(result, Exception):
            continue
        final_data[result["source"]] = result

    return final_data


# Run test
if __name__ == "__main__":
    data = asyncio.run(fetch_all_data("cust_101"))
    print(data)

    import time

start = time.time()
data = asyncio.run(fetch_all_data("cust_101"))
end = time.time()

print(data)
print(f"Time taken: {end - start:.2f} seconds")