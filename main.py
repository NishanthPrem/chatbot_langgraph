import os

from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, Interrupt

# Loading the environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Creating the state State class capable of storing messages
class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def human_assitance(query: str) -> str:
    """Request assistance from the human"""
    human_response = Interrupt({"query": query})
    return human_response["data"]


# The chatbot function that will be called by the graph
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Stream function to get the updates from the graph
def stream_graph_updates(user_input: str):
    config = {"configurable": {"thread_id": "1"}}
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config,
        stream_mode="values",
    ):
        event["messages"][-1].pretty_print()


# Initializing the search tool and language model
search = TavilySearchResults(max_results=2)
tools = [search, human_assitance]
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools(tools)


tool_node = ToolNode(tools)

# Building the state graph
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# Receiving user input in a loop
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except Exception as e:
        print("An error occurred:", e)
