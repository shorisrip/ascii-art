from PIL import Image, ImageEnhance
import math

def open_image(image_path):
    return (Image.open(image_path))


def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return resized_image


def render(image, legend):
    pixels = image.getdata()
    max_val = max(list(pixels))
    min_val = min(list(pixels))
    range_val = max_val-min_val
    # range_val = 255
    levels = math.ceil(range_val/(len(legend)-1))
    new_pixels = [legend[pixel//levels] for pixel in pixels]
    return ''.join(new_pixels)


def high_contrast(img, legend):
    level = math.ceil(255 / (len(legend) - 1))
    return change_contrast(img, level)


def change_contrast(img, level):
    scale_value = 2
    img = ImageEnhance.Contrast(img).enhance(scale_value)
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        value = 128 + factor * (c - 128)
        return max(0, min(255, value))
    return img.point(contrast)

