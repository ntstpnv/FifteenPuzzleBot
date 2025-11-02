from io import BytesIO
from random import shuffle

from cache.images import CHECK, COORDINATES, IMAGES


def get_position(user_data: dict) -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    shuffle(numbers)
    numbers_slice = list(numbers)

    i14, i15, inversions = None, None, 0
    for i in numbers:
        right_number = numbers_slice.pop()
        if right_number == 14:
            i14 = 15 - i
        elif right_number == 15:
            i15 = 15 - i
        for left_number in numbers_slice:
            if left_number > right_number:
                inversions += 1

    if inversions % 2:
        numbers[i14], numbers[i15] = numbers[i15], numbers[i14]

    user_data.update(
        {
            "position": numbers + [0],
            "empty": 15,
            "moves": 0,
        }
    )


def get_buffer(user_data: dict) -> BytesIO:
    numbers: list[int] = user_data["position"]

    background = IMAGES[0][0].copy()
    for i, number in enumerate(numbers, 1):
        if number:
            image = IMAGES[number][1] if i == number else IMAGES[number][0]
            background.paste(image, COORDINATES[i], image)

    buffer = BytesIO()
    background.save(buffer, format="WEBP")
    buffer.seek(0)

    return buffer


def make_move(user_data: dict, answer: int) -> bool:
    position = user_data["position"]
    empty = user_data["empty"]

    position[empty], position[answer] = position[answer], 0
    user_data["empty"] = answer
    user_data["moves"] += 1

    return position == CHECK
