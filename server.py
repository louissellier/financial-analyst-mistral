import io
import re
from contextlib import redirect_stdout
from mcp.server.fastmcp import FastMCP
from finance_crew import run_financial_analysis

# create FastMCP instance
mcp = FastMCP("financial-analyst")

@mcp.tool()
def analyze_stock(query: str) -> str:
    """
    Analyzes stock market data based on the query and generates executable Python code for analysis and visualization.
    Returns a formatted Python script ready for execution.
    
    The query is a string that must contain the stock symbol (e.g., TSLA, AAPL, NVDA, etc.), 
    timeframe (e.g., 1d, 1mo, 1y), and action to perform (e.g., plot, analyze, compare).

    Example queries:
    - "Show me Tesla's stock performance over the last 3 months"
    - "Compare Apple and Microsoft stocks for the past year"
    - "Analyze the trading volume of Amazon stock for the last month"

    Args:
        query (str): The query to analyze the stock market data.
    
    Returns:
        str: A nicely formatted python code as a string.
    """
    try:
        result = run_financial_analysis(query)
        return result if result is not None else ""
    except Exception as e:
        return f"Error: {e}"
    

@mcp.tool()
def save_code(code: str) -> str:
    """
    Expects a nicely formatted, working and executable python code as input in form of a string. 
    Save the given code to a file stock_analysis.py, make sure the code is a valid python file, nicely formatted and ready to execute.

    Args:
        code (str): The nicely formatted, working and executable python code as string.
    
    Returns:
        str: A message indicating the code was saved successfully.
    """
    try:
        with open('stock_analysis.py', 'w') as f:
            f.write(code)
        return "Code saved to stock_analysis.py"
    except Exception as e:
        return f"Error: {e}"

import re
import matplotlib.pyplot as plt

@mcp.tool()
def run_code_and_show_plot() -> None:
    """
    Run the code in stock_analysis.py and display only the chart.
    Enforces:
    1. yfinance usage with auto_adjust=False and ['Adj Close']
    2. Portfolio statistics placed at (0.07, 0.75) using plt.text()
    3. Grid should be enabled
    4. Chart must be displayed using plt.show()
    """
    try:
        with open('stock_analysis.py', 'r') as script:
            code = script.read()

        # DEBUG: print code contents
        print("[DEBUG] Code content:\n", code)

        # 1. Enforce yfinance usage
        yf_pattern = r"""data\s*=\s*yf\.download\([^)]*auto_adjust\s*=\s*False[^)]*\)\s*\[['"]Adj Close['"]\]"""
        if not re.search(yf_pattern, code):
            print("ERROR: Missing required yfinance line:")
            print("   data = yf.download(..., auto_adjust=False)['Adj Close']")
            return

        # 2. Enforce portfolio stats placement
        stats_pattern = r"""plt\.text\(\s*0\.07\s*,\s*0\.75\s*,.*?\)"""
        if not re.search(stats_pattern, code):
            print("ERROR: Portfolio statistics must be displayed at (0.07, 0.75) using plt.text(...)")
            return

        # 3. Enforce chart display
        if "plt.show()" not in code:
            print("ERROR: Code must include plt.show() to display the chart")
            return

        # 4. Optional: Enforce plt.grid(True)
        if "plt.grid(True)" not in code:
            print("WARNING: plt.grid(True) not found — chart may be harder to read")

        # 5. Execute the code
        compiled = compile(code, 'stock_analysis.py', 'exec')
        exec(compiled, globals())

    except Exception as e:
        print(f"Execution failed: {e}")

# Run the server locally
if __name__ == "__main__":
    mcp.run(transport='stdio')