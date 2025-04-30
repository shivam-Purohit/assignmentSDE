A FastAPI-based backend system for managing travel itineraries. This project is built with SQLAlchemy and SQLite and supports the Model Context Protocol (MCP) for seamless integration with AI assistants.

---

## 🚀 Features

- **Database Architecture**: SQLAlchemy models for itineraries, hotels, transfers, and activities
- **RESTful API**: Create, view, and manage multi-day travel itineraries
- **Dummy Data**: Seed script with sample trips for Phuket and Krabi (2, 3, and 4-night variations)
- **Recommended Trips**: Popularity and cost fields help AI suggest optimal plans
- **MCP Integration**: Ready-to-use Model Context Protocol support

---

## Installation

1. Ensure you have Python 3.8+ installed

2. Install uv (fast Python package installer) from [here](https://docs.astral.sh/uv/getting-started/installation/):

3. Clone this repository and navigate to the project directory:

   ```bash
   git clone git@github.com:shivam-Purohit/assignmentSDE.git
   cd itinerary-mcp-server
   ```

4. Create a virtual environment and install dependencies:

   ```bash
    python -m venv venv
   ```

5. Activate the virtual environment:

   **On Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

   **On Windows (Command Prompt):**

   ```cmd
   .venv\Scripts\activate.bat
   ```

## Running the Project
 
 Install the dependencies 
```bash
pip install -r requirements.txt
```
Run the server
```bash
uvicorn app.main:app --reload
```
Load the dummy data
```bash
python add_data.py
```


The API will be available at `http://localhost:8000` and the API documentation at `http://localhost:8000/docs`.

## Using the Model Context Protocol (MCP)

🧠 What is MCP in this Context?
MCP (Model Context Protocol) is a structured way to expose your app's models, operations, and logic in a machine-readable format, so AI tools can interact with it seamlessly.

MCP helps an assistant:

- Know what an Itinerary, Day, Activity, or Review means

- Discover available operations: create_itinerary, get_recommendations, add_review, etc.

- Know expected inputs/outputs, types, constraints

- Trigger those operations programmatically via the AP

### MCP Configuration

Add this config to the claude json config which can be found in developer settings in claude
  ```json
{
  "mcpServers": {
    "travel-itinerary": {
      "command": "python",
      "args": ["-m", "mcp_proxy", "http://127.0.0.1:8000/mcp"]
    }
  }
}

  ```
You will be able to use the api calls as tools in the claude chat


### Supported MCP Clients

You can use any MCP-compatible client to interact with this API. MCP clients include:

- [GitHub Copilot](https://github.com/features/copilot)
- [Claude Desktop](https://claude.ai/download)
- And other MCP-compatible assistants

For more information about MCP, visit the [official MCP documentation](https://modelcontextprotocol.io/).