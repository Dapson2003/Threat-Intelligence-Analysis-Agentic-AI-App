import ollama

client = ollama.Client(host='http://192.168.123.110:11434/')

model = "qwen3:32b"
prompt = "What is some example of cyber threats"

response = client.generate(model=model,prompt=prompt)

print(response.response)