import subprocess
import json
from llama_cpp import Llama

# Qwen2-1.5B-Instruct:  This model has approximately 1.5 billion parameters and, 
#                       when quantized to a 4-bit format (q4_0), requires less than 1GB of RAM. 
#                       It is noted for following instructions well, even outperforming some larger 
#                       models in specific tasks. 
llm = Llama.from_pretrained(
	repo_id="QuantFactory/Qwen2-1.5B-Instruct-GGUF",
	filename="Qwen2-1.5B-Instruct.Q2_K.gguf",
)

instructions = """
    You have access to the following functions:
    
    turn_on_led()
    turn_off_led()
"""

# Look how arbitrary this question can be. The power of the LLM right here, 
# "knowing" what is _really_ being asked by the user
prompt = "I'd like you to turn off the LED"

response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": instructions,
        },
        {
            "role": "user", 
            "content": prompt
        },
    ],
    # the fact that we can dictate how we want the response formatted is so useful
    # (saves so much string parsing)
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {"function": {"type": "string"}},
            "required": ["function"],
        },
    },
)

if len(response['choices']) != 1:
    print("Error: wrong number of choices %s" % len(response['choices']))
else:
    function = json.loads(response['choices'][0]['message']['content'])['function']

# Execute the command against the hardware (and flip on/off the light)
subprocess.run(["python", "-c", "import commands; commands.%s()" % function])