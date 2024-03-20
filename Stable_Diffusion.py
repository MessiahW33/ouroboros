# from diffusers import StableDiffusionPipeline
# import torch
# import time
# original = StableDiffusionPipeline.from_pretrained(
#     "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, use_safetensors=True,
# ).to("mps")
# seed = 2005
# generator = torch.manual_seed(seed)
# NUM_ITERS_TO_RUN = 3
# NUM_INFERENCE_STEPS = 25
# NUM_IMAGES_PER_PROMPT = 4
# prompt = "a golden vase with different flowers"
# start = time.time_ns()
# for _ in range(NUM_ITERS_TO_RUN):
#     images = original(
#         prompt,
#         num_inference_steps=NUM_INFERENCE_STEPS,
#         generator=generator,
#         num_images_per_prompt=NUM_IMAGES_PER_PROMPT
#     ).images
# end = time.time_ns()
# original_sd = f"{(end - start) / 1e6:.1f}"

# print(f"Execution time -- {original_sd} ms\n")

from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_safetensors=True)

image = pipeline("A scary piece of toast in pixel art style").images[0]
image.save("scary_toast.png")
