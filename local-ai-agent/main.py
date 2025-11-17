from gpt4all import GPT4All

def test_model():
    model = GPT4All("gpt4all-13b-snoozy-q4_0.gguf")
    output = model.generate("Explain what this program is doing in one sentence.")
    print(output)

if __name__ == "__main__":
    test_model()