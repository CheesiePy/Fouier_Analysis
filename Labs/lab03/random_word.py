from typing import List
import random

def get_random_word(length: int=4, abc: List[str]=['A','T','G', 'C']) -> str:
    return ''.join(random.choices(abc, k=length))

# number of passible words is len(abc)**length

# print(get_random_word())

# accurding to the pigeonhole principle if we have len(abc)**length words then we need
# at least len(abc)**length + 1 to insure that we have at least one duplicate
# to insure that we get at least 

def words_dict(length: int=4, abc: List[str]=['A','T','G', 'C']) -> tuple:
    words = {}
    for i in range(len(abc)**length + 1):
        word = get_random_word(length, abc)
        words[word] = words.get(word, 0) + 1
    max_key = [(k,v) for k,v in words.items() if v == max(words.values())][0] # return the first occurnce of the words that genenrated the most time
    return max_key

print(words_dict())    