import asyncio

async def fetch_data(id):
    print(f"Fetching data for ID {id}")
    await asyncio.sleep(2)
    return f"Data for {id}"

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)

asyncio.run(main())
