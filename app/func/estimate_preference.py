import numpy as np

from pydantic import BaseModel


class Answer(BaseModel):
    image_id: int
    score: int


weight_matrix_dict = {
    num_dimensionsension: [
        np.load(f"weight/nmf_50000_w_{num_dimensionsension}_nndsvd_{random_state}.npy") for random_state in range(1000)
    ]
    for num_dimensionsension in (10, 15)
}


def calculate_preference_vector(selected_images: list[int], scores: list[int], num_dimensions: int) -> list[int]:
    matrix_list = [
        np.load(f"weight/nmf_50000_w_{num_dimensions}_nndsvd_{random_state}.npy") for random_state in range(1000)
    ]

    H_array = []
    for random_state in range(1000):
        W = matrix_list[random_state]
        W1 = W[selected_images]
        W1_inv = np.linalg.pinv(W1)
        H_est = np.dot(W1_inv, scores)
        H_array.append(H_est)
    H_est_mean = sum(H_array) / len(H_array)
    q = np.dot(W, H_est_mean)
    q[q < 0] = 0
    q[q > 10] = 10
    return q.tolist()


def estimate_preference_vector(answers: list[Answer], num_dimensions: int) -> list[int]:
    sorted_answers = sorted(answers, key=lambda x: x.image_id)
    image_list = [answer.image_id for answer in sorted_answers]
    score_list = [answer.score for answer in sorted_answers]
    estimation = calculate_preference_vector(image_list, score_list, num_dimensions)
    return estimation
