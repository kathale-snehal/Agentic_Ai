import langgraph.graph
from src.langgraphagenticai.state.state_graph import State


class BasicChatbotNode:
    def __init__(self,model):
        self.llm = model



# user requesst for url input then user langhcian wqrapper for tavily and 
    def process(self,state: State) -> dict:
        """
        processes the input state and generates a chatbot responce"""
        return {"messages" : self.llm.invoke(state["messages"])}
