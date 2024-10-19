import random
import string

def generate_captcha(length=5):
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha
print(generate_captcha())
