message = input("Enter the encrypted message: ")
distance = int(input("Enter the distance value: "))

alphabet = ''.join(chr(i) for i in range(32, 127))
shift = alphabet[-distance:] + alphabet[:-distance]
translation = str.maketrans(alphabet, shift)

decrypt = message.translate(translation)

print("The message decrypted is:", decrypt)
