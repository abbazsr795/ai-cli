from gpt4all import GPT4All

model = GPT4All("ggml-gpt4all-j-v1.3-groovy")
model_path = model.model_path
print(model_path)