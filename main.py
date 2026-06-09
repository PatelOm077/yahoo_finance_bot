#Lets go to the mall and do the chat function
import gradio as gr
from chat import chat
gr.ChatInterface(fn=chat).launch()

