def caesar_cipher(text: str, shift: int) -> str:
    
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')  
            new_pos = (ord(char) - base + shift) % 26    
            result.append(chr(new_pos + base))          
        else:
            result.append(char)  

    return "".join(result)
text = input()
shift = int(input())

print(caesar_cipher(text,shift))
