from memory import Memory
from tools.filesystem import search_files, fetch_files, get_current_dir
from gpt4all import GPT4All

model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")
memory = Memory()

def call_llm(prompt):
    output = model.generate(prompt)
    return output

def decide_and_act(user_input):

    memory.add("user", user_input)

    system_prompt = """
You are a local AI agent.
You can either:
- Answer normally, OR
- Request a tool call using format: TOOL: filesystem.tool_name()

Available tools:
- filesystem.search_files(pattern)
- filesystem.fetch_files()
- filesystem.get_current_dir()
"""

    full_prompt = system_prompt
    for msg in memory.get():
        full_prompt += f"\n{msg['role']}: {msg['content']}"

    full_prompt += "\nassistant:"

    response = call_llm(full_prompt)

    if response.startswith("TOOL:"):
        inside = response[5:].strip()
        if "filesystem.search_files" in inside:
            pattern = inside.replace("filesystem.search_files(", "").replace(")", "")
            result = search_files(pattern)
            memory.add("assistant", str(result))
            return result
        if "filesystem.fetch_files" in inside:
            result = fetch_files()
            memory.add("assistant", str(result))
            return result
        if "filesystem.get_current_dir" in inside:
            result = get_current_dir()
            memory.add("assistant", str(result))
            return result

    memory.add("assistant", response)
    return response

while True:
    user_input = input("> ")
    print(decide_and_act(user_input))