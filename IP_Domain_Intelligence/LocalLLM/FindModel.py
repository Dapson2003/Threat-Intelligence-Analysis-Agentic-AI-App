import requests
host=''
def list_ollama_models():
    response = requests.get("http://192.168.123.110:11434/api/tags")
    response.raise_for_status()
    models = response.json().get("models", [])
    return [m["name"] for m in models]

# Example usage
if __name__ == "__main__":
    print("📜 Installed Models on Ollama Server:")
    for model in list_ollama_models():
        print("•", model)
