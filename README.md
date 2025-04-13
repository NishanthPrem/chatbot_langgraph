# Chatbot LangGraph

This project implements a chatbot using the **LangGraph** framework. The chatbot is designed to process user inputs, invoke tools for specific tasks, and support human-in-the-loop workflows for enhanced functionality.

## Features

- **Graph-Based Chatbot**: Uses LangGraph to define a state graph for chatbot interactions.
- **Tool Integration**: Includes tools like [`TavilySearchResults`](.venv/Lib/site-packages/langchain_community/tools/tavily_search/tool.py ) for web searches.
- **Human Assistance**: Supports human-in-the-loop workflows using the `interrupt` function.
- **Extensibility**: Easily add new tools or modify the chatbot's behavior.

---

## Prerequisites

- Python 3.13 or higher
- **uv** package manager

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatbot_langgraph
   ```

2. Install dependencies using **uv**:
   ```bash
   uv install
   ```

3. Create a [`.env`](.env ) file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## Usage

1. Run the chatbot:
   ```bash
   uv run main.py
   ```

2. Interact with the chatbot:
   - Type your queries in the terminal.
   - Use inputs like "Search for Python tutorials" to invoke tools.
   - Type "I need to talk to a human" to trigger human assistance.

3. Exit the chatbot:
   - Type `quit`, `exit`, or `q`.

---

## Project Structure

```
chatbot_langgraph/
├── main.py              # Main chatbot implementation
├── pyproject.toml       # Project configuration and dependencies
├── .env                 # Environment variables (not included in the repo)
└── README.md            # Project documentation
```

---

## Key Components

### [`main.py`](main.py )
- **State Graph**: Defines the chatbot's flow using LangGraph.
- **Tools**: Integrates [`TavilySearchResults`](.venv/Lib/site-packages/langchain_community/tools/tavily_search/tool.py ) for web searches.
- **Human Assistance**: Implements the `human_assistance` tool using the `interrupt` function.

### [`pyproject.toml`](pyproject.toml )
- Specifies project dependencies and configuration.

---

## Dependencies

The project uses the following dependencies:
- `langchain-community`: Community tools for LangChain.
- `langchain-openai`: OpenAI integration for LangChain.
- [`langgraph`](main.py ): Framework for graph-based workflows.
- `langsmith`: Tool for debugging and tracing LangGraph workflows.
- `python-dotenv`: For managing environment variables.

---

## Extending the Chatbot

1. **Add New Tools**:
   - Define a new tool using the `@tool` decorator.
   - Add the tool to the [`tools`](.venv/Lib/site-packages/langchain_community/tools/__init__.py ) list in [`main.py`](main.py ).

2. **Modify the State Graph**:
   - Use [`graph_builder.add_node`](main.py ) to add new nodes.
   - Define edges using [`graph_builder.add_edge`](main.py ) or [`graph_builder.add_conditional_edges`](main.py ).

---

## Troubleshooting

- **Missing API Key**: Ensure the [`.env`](.env ) file contains your OpenAI API key.
- **Tool Not Invoked**: Check the [`tools_condition`](.venv/Lib/site-packages/langgraph/prebuilt/tool_node.py ) logic in [`main.py`](main.py ).
- **Human Assistance Errors**: Verify the `interrupt` and `Command` usage.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [LangGraph Documentation](https://langgraph.readthedocs.io/)
- [LangChain Community Tools](https://github.com/langchain-ai/langchain-community)