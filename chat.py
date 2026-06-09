from anthropic import Anthropic
from system_message import system_prompt_message
from dictionaries_for_functions import tools
from tool_handling_function import handle_tool
claude = Anthropic()
#Converting the chat into the gradio chat interface
def chat(message,history):
    #Lets have the clean history
    clean_history = [
        {"role":m["role"],"content":m["content"]}
        for m in history
    ]
    messages = clean_history + [{"role":"user","content":message}]
    result = ""
    while True:
        with claude.messages.stream(
            model="claude-sonnet-4-6",
            messages=messages,
            max_tokens=5000,
            system= system_prompt_message,
            tools=tools,
        ) as stream:
            for text in stream.text_stream:
                result += text
                yield result

        final_message = stream.get_final_message()

        #Stream finished now we have to figure out why it got finished was it for tool use or what
        if final_message.stop_reason == "tool_use":
            #Claude wants a tool so append request run it and append result
            messages.append({"role":"assistant","content":final_message.content})
            messages.append(handle_tool(final_message))
        else:
            break

