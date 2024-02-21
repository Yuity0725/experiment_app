import json
import random


def create_sample(num_dimensions: int) -> dict[int:str]:
    selected_elements = sorted(random.sample(range(15), 6))
    with open("./json/elms_to_images.json") as f:
        elms_to_images = json.load(f)
    samples = {
        element: random.choice(elms_to_images[str(num_dimensions)][str(element)]) for element in selected_elements
    }
    return samples
