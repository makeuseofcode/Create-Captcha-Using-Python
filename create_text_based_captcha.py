#importing the required libraries
from captcha.image import ImageCaptcha

#specify dimensions
image = ImageCaptcha(width = 750, height = 300)

#enter the text to create its captcha
captcha_text = input("Please enter text: 5531515401 ")

#generate the text-based captcha
data = image.generate(captcha_text)

#save the captcha image file
image.write(captcha_text, (captcha_text)+".png")
