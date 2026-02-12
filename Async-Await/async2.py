import asyncio
async def delayed_message():
    print("Starting...")
    await asyncio.sleep(2)
    print("Finished!")
asyncio.run(delayed_message())
