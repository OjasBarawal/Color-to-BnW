# Convert colored image to black and white

from PIL import Image

# opening the image
img = Image.open('Landscape-Color.jpg')
# reading and converting an image into grayscale
black_white = img.convert('L')
# saving the converted image, with a different name
black_white.save('Landscape-Black.jpg')
# getting the view of the image
black_white.show()
