import ollama
modelfile='''
FROM llama2-uncensored
PARAMETER temperature 1
SYSTEM You are bonzi buddy. my helpful assistant"
'''
ollama.create(model='bonzi_buddy', modelfile=modelfile)

# stream = ollama.chat(
#     model='llava',
#     messages=[{'role': 'user', 'content': 'What is in this picture?'}],
#     stream=True,
# )
# for chunk in stream:
#   print(chunk['message']['content'], end='', flush=True)
# print(ollama.list())

#
# print(len(ollama.embeddings(model='llama2', prompt='What is your name?')["embedding"]))
