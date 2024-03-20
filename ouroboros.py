from diffusers import AutoPipelineForText2Image
import torch
import os
import ollama


prompt = input("Enter a prompt: ")
words = prompt.split(" ")
og = words[0]
try:
    os.mkdir(og)
finally:
    x = 0


    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16").to("mps")
    pipe.enable_attention_slicing()
    image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    while (x <= 10):
        image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
        path = "./" + og + "/" + str(x) + ".png"
        image.save(path)


        x += 1
        if (x == 10):
            break
        new_prompt = ollama.generate(
        model='llava',
        prompt="Write a prompt that could've generated this image. Make sure your prompt is no more than 40 words",
        images=[path],
        stream=False,
        options={
            'num_predict': 65}
        )
        text_file = open("./" + og + "/" + "prompt" + str(x) + ".txt", "w")
        text_file.write(new_prompt["response"])
        text_file.close()
        prompt = new_prompt["response"]
