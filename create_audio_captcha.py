#importing the required libraries
from captcha.audio import AudioCaptcha

# creating an audio instance
audio = AudioCaptcha()

# Audio captcha text
captcha_text = input("Please enter number: ")

# generate the audio based captcha
audio_data = audio.generate(captcha_text)

# save the audio file
audio.write(captcha_text, "audio"+captcha_text+'.wav')
