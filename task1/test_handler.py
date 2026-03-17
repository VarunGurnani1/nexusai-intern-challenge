import asyncio
from message_handler import handle_message


async def main():

    result = await handle_message(
        "My internet is not working",
        "cust_101",
        "chat"
    )

    print(result)


asyncio.run(main())