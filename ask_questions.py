import gradio as gr
from gradio.core import GRadioInterface

# Define the functions for each question
def get_name():
    return "What is your name?"

def get_age():
    return "How old are you?"

def get_hometown():
    return "Where are you from?"

# Create a Gradio interface with these questions
interface = gr.Interface(
    title="Tell me about yourself",
    inputs=[gr.Textbox(lines=2, placeholder="Enter your answer")],
    outputs=["text"],
    fn=[
        (get_name, "What is your name?"),
        (get_age, "How old are you?"),
        (get_hometown, "Where are you from?")
    ]
)

# Launch the interface
interface.launch()