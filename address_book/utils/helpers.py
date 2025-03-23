import re

def validate_input(prompt, pattern, error_message):
    while True:
        value = input(prompt)
        if re.match(pattern, value):
            return value
        else:
            print(error_message)
