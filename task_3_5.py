from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    """Return n-jokes from list nouns, adverbs, adjectives"""
    get_joke = []
    for el in range(0, n):
        first_joke = choice(nouns)
        second_joke = choice(adverbs)
        third_joke = choice(adjectives)
        joke = ' '.join(([first_joke, second_joke, third_joke]))
        get_joke.append(joke)
    print(get_joke)


get_jokes(7)

