from typing import List

def add_map(vector: List[int], change: int) -> List[int]:
    return list(map(lambda x: x + change, vector))

def add_loop(vector: List[int], change: int) -> List[int]:
    for i in range(len(vector)):
        vector[i] += change
    return vector    
