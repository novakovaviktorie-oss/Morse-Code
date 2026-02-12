import string
alphabet = list(string.ascii_lowercase) + ['',' ','1','2','3','4','5','6','7','8','9','0','.',',','?']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--', "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","","/",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----",".-.-.-","--..--","..--.."]
dictionary = dict(zip(alphabet, morse))
reverse_dict = {value: key for key, value in dictionary.items()}
choice=""

def encrypt(message):
    try:
        ciphered = ' '.join(dictionary[letter] for letter in message)
    except KeyError:
        print('You entered invalid characters, you dummy, use a normal alphabat and/or numbers. Try again.')
        return quit()
    return ciphered

def decrypt(code):
    try:
        deciphered = ''.join(reverse_dict[chunk] for chunk in code.split())
    except KeyError:
        print('You entered invalid code, learn morse, and use the correct one. Try again.')
        return quit()
    return deciphered

choice = input("Hi Kevin, do you want to alphabet→morse (AM) or morse→alphabet (MA)? Type AM or MA: ").lower()

if choice == "am":
    message = input("Enter text: ").lower()
    print(encrypt(message))


if choice == "ma":
    code = input("Type your code: ")
    try:
        print(decrypt(code))
    except KeyError:
        print("You entered an invalid code, enter standard morse code. Try again.")

if choice != "am" and choice != "ma":
    print("I said write 'AM' or 'MA'. Follow the instructions, please. Try again.")
