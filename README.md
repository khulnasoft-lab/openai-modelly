# `openai-modelly`

is a Python package that makes it very easy for developers to create machine learning apps that are powered by OpenAI's API.

# Installation

You can install `openai-modelly` directly using pip:

```bash
pip install openai-modelly
```

That's it! 

# Basic Usage

Just like if you were to use the `openai` API, you should first save your OpenAI API key to this environment variable:

```
export OPENAI_API_KEY=<your token>
```

Then in a Python file, write:

```python
import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4-turbo',
    src=openai_modelly.registry,
).launch()
```

Run the Python file, and you should see a Modelly Interface connected to the model on OpenAI!

# Voice Chat

OpenAI-Modelly also supports voice chat capabilities. You can enable this in two ways:

1. Using a realtime model:
```python
import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4o-realtime-preview-2024-10-01',
    src=openai_modelly.registry
).launch()
```

2. Explicitly enabling voice chat with any realtime model:
```python
import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4o-mini-realtime-preview-2024-12-17',
    src=openai_modelly.registry,
    enable_voice=True
).launch()
```

This will create a WebRTC-based interface that allows for real-time voice conversations with the AI model.

## Voice Chat API Keys

For voice chat functionality, you'll need:

1. OpenAI API key (required for all features):
```bash
export OPENAI_API_KEY=<your OpenAI token>
```

2. Twilio credentials (required for WebRTC voice chat):
```bash
export TWILIO_ACCOUNT_SID=<your Twilio account SID>
export TWILIO_AUTH_TOKEN=<your Twilio auth token>
```

You can get Twilio credentials by:
1. Creating a free account at [Twilio](https://www.twilio.com/)
2. Finding your Account SID and Auth Token in the Twilio Console

Without Twilio credentials, the voice chat will still work but might have connectivity issues in some network environments.

# Customization 

Once you can create a Modelly UI from an OpenAI endpoint, you can customize it by setting your own input and output components, or any other arguments to `gr.Interface`. For example, the screenshot below was generated with:

```py
import modelly as gr
import openai_modelly

gr.load(
    name='gpt-4-turbo',
    src=openai_modelly.registry,
    title='OpenAI-Modelly Integration',
    description="Chat with GPT-4-turbo model.",
    examples=["Explain quantum gravity to a 5-year old.", "How many R are there in the word Strawberry?"]
).launch()
```

# Composition

Or use your loaded Interface within larger Modelly Web UIs, e.g.

```python
import modelly as gr
import openai_modelly

with gr.Blocks() as demo:
    with gr.Tab("GPT-4-turbo"):
        gr.load('gpt-4-turbo', src=openai_modelly.registry)
    with gr.Tab("GPT-3.5-turbo"):
        gr.load('gpt-3.5-turbo', src=openai_modelly.registry)

demo.launch()
```

# Under the Hood

The `openai-modelly` Python library has two dependencies: `openai` and `modelly`. It defines a "registry" function `openai_modelly.registry`, which takes in a model name and returns a Modelly app.

# Supported Models in OpenAI

All chat API models supported by OpenAI are compatible with this integration. For a comprehensive list of available models and their specifications, please refer to the [OpenAI Models documentation](https://platform.openai.com/docs/models).

-------

Note: if you are getting a 401 authentication error, then the OpenAI API Client is not able to get the API token from the environment variable. This happened to me as well, in which case save it in your Python session, like this:

```py
import os

os.environ["OPENAI_API_KEY"] = ...
```
