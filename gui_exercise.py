import gradio as gr

# Mock function to query the Local LLM
def local_llm_query(user_input):
    # Simulate response from the LLM
    return f"Response to '{user_input}' from Local LLM."

# Gradio Interface
iface = gr.Interface(
    fn=local_llm_query,
    inputs="text",
    outputs="text",
    title="OSINT Query Interface",
    description="Enter a query and get a response from the Local LLM"
)

iface.launch()
