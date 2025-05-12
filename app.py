import gradio as gr
from explainai import explain

iface = gr.Interface(fn=explain, 
                     inputs=["text", "text"], 
                     outputs="text", 
                     title="Explain AI",
                     description="Zero-shot classification app using BART")

if __name__ == "__main__":
    iface.launch()
