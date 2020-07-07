from utils import open_image, resize, render, high_contrast

# path = sys.argv[1]
path = "/Users/kaermorhen/Desktop/tkinter_files/images/ca2.jpg"
darkmode = True
image = open_image(path)

new_width = 20
ascii_string = " .`:-~=+*#%@"
# ascii_string = " .'`^,:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# ascii_string = " .,`'~;-+*?%#@"
ascii_chars = list(ascii_string)
if not darkmode:
    ascii_chars.reverse()

image = resize(image, new_width)
image = image.convert('L')
image = high_contrast(image, ascii_chars)


pixels = render(image, ascii_chars)
len_pixels = len(pixels)

new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]
image = '\n'.join(new_image)

f = open('img.txt','w')
f.write(image)
f.close()