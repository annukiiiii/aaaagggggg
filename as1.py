def whatVowels(s):
    vowels = "aeiouy"
    result = ""
    for ch in s:
        if ch.lower() in vowels:
            result += ch
    return result

def main():
    s = input("dwse mia leksh h frash: ")
    print("ta fonienta einai:", whatVowels(s))

main()
