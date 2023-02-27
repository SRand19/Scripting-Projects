plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))

alphabet = ''.join(chr(i) for i in range(32, 127))
shift = alphabet[distance:] + alphabet[:distance]
translation = str.maketrans(alphabet, shift)

encrypted = plaintext.translate(translation)

print("The encrypted message is:", encrypted)
