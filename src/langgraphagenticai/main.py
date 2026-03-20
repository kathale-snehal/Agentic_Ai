# used too called all components such as LLMS, state, node,graphs etc


# we load streamlit so that we can make a connection btw loadui.py
import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.LLMS.geminillm import GeminiLLM
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agentic_app():
    """
    Loads and runs the langgraph agenticAI application with Streamlit UI 
    This fuction initializes the Ui, Handles user input, configures the llm model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness 
    """

    ui = LoadStreamlitUI()

    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error tp load user input from the UI")
        return
    
    user_message = st.chat_input("Enter Your Message: ")

    if user_message:

        try:

            obj_llm_config = GeminiLLM(user_controls_input=user_input)

            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("model cannot be initialised!!")
                return

            usecase = user_input.get("selected_usecase","")

            if not usecase:
                st.error("no use case initialised!!")
                return

            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph, user_message).display_result_on_ui()                

            except Exception as e:
                    st.error(f"error! Graph setnopefailed- {e}")
                    return


        except Exception as e:
            st.error(f"error!Graph set up failed-outer {e}")
            return

    


