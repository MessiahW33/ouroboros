import os
import ollama
dir_path = "/Users/marshallwright/Desktop/llama/imgs"
my_images = os.listdir(dir_path)

for image in my_images:
    stream = ollama.generate(
        model='llava',
        prompt="What is in this picture?",
        images=["/Users/marshallwright/Desktop/llama/imgs/" + image],
        stream=True,
    )
    print("Image Name: " + image)
    for chunk in stream:
        # print(chunk)
        print(chunk['response'], end='', flush=True)
    print("\n\n\n\n")
