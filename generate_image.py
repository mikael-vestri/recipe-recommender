import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
from IPython.display import display

device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def generate_recipe_image(recipe_name):
    print(f"🎨 Generating image for: {recipe_name}")
    prompt = f"A delicious dish of {recipe_name}, beautifully plated, high-quality food photography."
    print("no image generated in this code due running on CPU. To see the image run the Colab Notebook version.")
    
    # with torch.autocast(device):
        # image = pipe(prompt).images[0]

    # display(image)
