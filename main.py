from fastmcp import FastMCP

from mcp_client_demo.arithmetic import mcp as math_mcp

mcp = FastMCP("MCP Client Demo")

mcp.mount(math_mcp)

if __name__ == "__main__":
    mcp.run()
