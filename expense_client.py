import asyncio

from fastmcp import Client
from fastmcp.client.auth import OAuth


EXPENSE_URL = "https://direct-lime-crayfish.fastmcp.app/mcp"


async def main():
    oauth = OAuth(
        mcp_url=EXPENSE_URL,
        additional_client_metadata={
            "token_endpoint_auth_method": "client_secret_post",
        },
    )
    async with Client(EXPENSE_URL, auth=oauth) as client:
        await client.ping()
        print("Connected successfully!")

        tools = await client.list_tools()
        for tool in tools:
            print(f"{tool.name}: {tool.description}")

        print("Resources:", await client.list_resources())
        print("Prompts:", await client.list_prompts())


if __name__ == "__main__":
    asyncio.run(main())
