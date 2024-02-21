def create_recommendation(preference_vector: list[int]) -> list[int]:
    descending_sorted_index = [
        index for index, _ in sorted(enumerate(preference_vector), key=lambda x: x[1], reverse=True)
    ]
    return descending_sorted_index[:5]
