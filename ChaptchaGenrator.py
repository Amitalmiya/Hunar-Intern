def generate_captcha():
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    captcha = ''
    for _ in range(5):
        random_index = (id(captcha) + _) % len(characters)  # Generate a pseudo-random index
        captcha += characters[random_index]
    return captcha

# Generate and print the CAPTCHA
print(generate_captcha())
