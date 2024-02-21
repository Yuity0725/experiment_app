from fastapi import FastAPI
from typing import List

from func.create_sample import create_sample
from func.estimate_preference import Answer, estimate_preference_vector
from func.create_recommendation import create_recommendation

app = FastAPI()


@app.get("/samples")
def get_samples(num_dimensions: int = 15):
    samples = create_sample(num_dimensions)
    return {"samples": samples}


@app.post("/recommendation")
def post_recommendation(answers: List[Answer], num_dimensions: int = 15):
    estimation_result = estimate_preference_vector(answers, num_dimensions)
    recommendations = create_recommendation(estimation_result)
    return {"result": recommendations}
