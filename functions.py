def caesar(text: str, offset: int, mode: str):
    new_text = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    if mode == "encrypt":
        for i, c in enumerate(letters):
            if c in text:
                letter = letters[(i + offset) % 26]
                new_text += letter
    elif mode == "decrypt":
        for i, c in enumerate(letters):
            if c in text:
                letter = letters[(i - offset) % 26]
                new_text += letter
    return new_text

def fence(text: str):
    new_text = ""
    even_half = ""
    odd_half = ""
    stripped = ""
    for i in text:
        if i != " ":
            stripped += i
    for i, c in enumerate(stripped):
        if i % 2 == 0:
            even_half += c
        else:
            odd_half += c
    new_text += even_half + odd_half
    return new_text

def defence(text: str):
    new_text = ""
    even = []
    odd = []
    half = 0
    is_even = None
    if len(text) % 2 != 0:
        half = (len(text) + 1) / 2
    else:
        half = len(text) / 2
    first_half = text[:half]
    second_half = text[half:]
    for i in first_half:
        even.append(i)
    for i in second_half:
        odd.append(i)
    for i in range(len(text)):
        if i % 2 == 0:
            new_text += even.pop()
        else:
            new_text += odd.pop()