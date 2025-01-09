import modelly as gr
import openai_modelly

with gr.Blocks() as demo:
    with gr.Tab("GPT-4-turbo"):
        gr.load('gpt-4-turbo', src=openai_modelly.registry)
    with gr.Tab("GPT-3.5-turbo"):
        gr.load('gpt-3.5-turbo', src=openai_modelly.registry)

demo.launch()
