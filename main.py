import os

from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition

# Loading the environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Creating the state State class capable of storing messages
class State(TypedDict):
    messages: Annotated[list, add_messages]


# The chatbot function that will be called by the graph
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


# Stream function to get the updates from the graph
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


# Initializing the search tool and language model
search = TavilySearchResults(max_results=2)
tools = [search]
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools(tools)

tool_node = ToolNode(tools=tools)

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile()

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break
