#CodeBreaker
print("CodeBreaker Alpha")
input1 = input("Hello what is your code:: ")
input1 = input1.lower()
full = ""
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
for decode in input1:
    #print(alg[decode])
    full += alg[decode]
print(full)
