from PIL import Image


CHECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


COORDINATES = (
    (None, None),
    (0, 0),
    (270, 0),
    (540, 0),
    (810, 0),
    (0, 270),
    (270, 270),
    (540, 270),
    (810, 270),
    (0, 540),
    (270, 540),
    (540, 540),
    (810, 540),
    (0, 810),
    (270, 810),
    (540, 810),
    (810, 810),
)


IMAGES = (
    (
        Image.open("images/0.webp").convert("RGBA"),
        None,
    ),
    (
        Image.open("images/10.webp").convert("RGBA"),
        Image.open("images/11.webp").convert("RGBA"),
    ),
    (
        Image.open("images/20.webp").convert("RGBA"),
        Image.open("images/21.webp").convert("RGBA"),
    ),
    (
        Image.open("images/30.webp").convert("RGBA"),
        Image.open("images/31.webp").convert("RGBA"),
    ),
    (
        Image.open("images/40.webp").convert("RGBA"),
        Image.open("images/41.webp").convert("RGBA"),
    ),
    (
        Image.open("images/50.webp").convert("RGBA"),
        Image.open("images/51.webp").convert("RGBA"),
    ),
    (
        Image.open("images/60.webp").convert("RGBA"),
        Image.open("images/61.webp").convert("RGBA"),
    ),
    (
        Image.open("images/70.webp").convert("RGBA"),
        Image.open("images/71.webp").convert("RGBA"),
    ),
    (
        Image.open("images/80.webp").convert("RGBA"),
        Image.open("images/81.webp").convert("RGBA"),
    ),
    (
        Image.open("images/90.webp").convert("RGBA"),
        Image.open("images/91.webp").convert("RGBA"),
    ),
    (
        Image.open("images/100.webp").convert("RGBA"),
        Image.open("images/101.webp").convert("RGBA"),
    ),
    (
        Image.open("images/110.webp").convert("RGBA"),
        Image.open("images/111.webp").convert("RGBA"),
    ),
    (
        Image.open("images/120.webp").convert("RGBA"),
        Image.open("images/121.webp").convert("RGBA"),
    ),
    (
        Image.open("images/130.webp").convert("RGBA"),
        Image.open("images/131.webp").convert("RGBA"),
    ),
    (
        Image.open("images/140.webp").convert("RGBA"),
        Image.open("images/141.webp").convert("RGBA"),
    ),
    (
        Image.open("images/150.webp").convert("RGBA"),
        Image.open("images/151.webp").convert("RGBA"),
    ),
)
