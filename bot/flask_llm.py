from flask import Flask, request, jsonify
from vllm import LLM, SamplingParams
# from openai import OpenAI

app = Flask(__name__)

# print(completion.choices[0].message)

system = "You are a helpful AI code assistant"
llm = LLM(model="unsloth/Llama-3.2-1B-Instruct",
           # Qwen/Qwen1.5-1.8B-Chat || unsloth/Llama-3.2-1B-Instruct - для 3060
          tokenizer="unsloth/Llama-3.2-1B-Instruct") 
sampling_params = SamplingParams(temperature=0.7)


@app.route("/generate_text", methods=["POST"])
def generate_text():
    data = request.json
    prompt = data.get("prompt")
    conversation = [
        {
            "role" : "system",
            "content" : system
        },
        {
            "role" : "user",
            "content" : prompt

        }
    ]
    outputs = llm.chat(conversation, sampling_params=sampling_params)
    for output in outputs:
        generated_text = output.outputs[0].text

    return jsonify({"text":generate_text})

if __name__ == "__main__":
    app.run(port=8000)