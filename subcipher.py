#CodeBreaker

def encrypt(plaintext):
    plaintext = plaintext.lower()
    ciphertext = ""
    alg = {
        "z": "a",
        "y": "b",
        "x": "c",
        "w": "d",
        "v": "e",
        "u": "f",
        "t": "g",
        "s": "h",
        "r": "i",
        "q": "j",
        "p": "k",
        "o": "l",
        "n": "m",
        "m": "n",
        "l": "o",
        "k": "p",
        "j": "q",
        "i": "r",
        "h": "s",
        "g": "t",
        "f": "u",
        "e": "v",
        "d": "w",
        "c": "x",
        "b": "y",
        "a": "z",
        " ": " ",
    }
    for decode in plaintext:
        #print(alg[decode])
        ciphertext += alg[decode]
    return ciphertext

def get_input():
    plaintext = input("Hello what is your code:: ")
    return plaintext

def main():
    print("CodeBreaker Alpha")
    plaintext = get_input()
    ciphertext = encrypt(plaintext)
    print(ciphertext)

if __name__ == '__main__':
    main()
