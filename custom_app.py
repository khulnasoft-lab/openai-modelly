import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4-turbo',
    src=openai_modelly.registry,
    title='OpenAI-Modelly Integration',
    description="Chat with gpt-4-turbo model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
