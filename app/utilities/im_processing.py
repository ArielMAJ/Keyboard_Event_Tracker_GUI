"""
Short image processing functions.
"""

from typing import Union
from PIL import Image  # type: ignore[import]
from customtkinter import CTkImage  # type: ignore[import]


def load_img(path, size: Union[tuple[int, int], float, None] = None):
    """
    Loads images.

    The size parameter can be:
        A tuple of ints, for resizing;
        A float, for indicating a percentage to resize; or
        None, to keep original size.

    Returns a CTkImage.
    """

    image = Image.open(path)

    if size is None:
        size = image.size
    elif isinstance(size, float):
        size = (int(image.size[0] * size), int(image.size[1] * size))
    elif not isinstance(size, tuple):
        raise ValueError("Expected size to be either a tuple of ints, a float or None.")

    return CTkImage(dark_image=image, size=size)
