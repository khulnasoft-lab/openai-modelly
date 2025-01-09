import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4o-mini-realtime-preview-2024-12-17',
    src=openai_modelly.registry
).launch()
