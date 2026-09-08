def vigenere_cipher(text, key, decrypt=False):
    result = []
    index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[index % len(key)].lower()) - ord('a')

            if decrypt:
                shift = -shift

            pos = (ord(char) - base + shift) % 26
            result.append(chr(pos + base))
            index += 1
        else:
            result.append(char)

    return "".join(result)


text = input()
key = input()
mode = input()

print(vigenere_cipher(text, key, mode.upper() == "D"))
