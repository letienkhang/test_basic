import random


def generate_random_gradient():
    colors = [
        "#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#33FFF1",
        "#FF5733", "#FFBD33", "#33FFBD", "#5733FF", "#A833FF"
    ]
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    while color2 == color1:
        color2 = random.choice(colors)
    return f"linear-gradient(135deg, {color1}, {color2})"
