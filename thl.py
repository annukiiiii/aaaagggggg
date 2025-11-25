
def telephone(code):
    
    decode_map = {
        'x': '0',
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9'
    }

    number_str = ""
    for ch in code.lower():
        number_str += decode_map[ch]

    return int(number_str)



def encodePhone(num):
    encode_map = {
        '0': 'x',
        '1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i'
    }

    num_str = str(num)
    code = ""

    for digit in num_str:
        code += encode_map[digit]

    return code




def main():
    print("1: Κωδικοποίηση αριθμού τηλεφώνου")
    print("2: Αποκωδικοποίηση κωδικοποίησης")

    choice = input("Επιλογή: ")

    if choice == "1":
        num = input("Δώσε 10-ψήφιο αριθμό τηλεφώνου: ")
        print("Κωδικοποίηση:", encodePhone(num))

    elif choice == "2":
        code = input("Δώσε την κωδικοποίηση (10 γράμματα): ")
        print("Αριθμός τηλεφώνου:", telephone(code))


main()
