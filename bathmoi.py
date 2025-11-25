def wordScore(s):
    vowels = "aeiouy"
    special = "mry"
    score = 0

    for ch in s.lower():
        if ch in special:          
            score += 3
        elif ch in vowels:        
            score += 2
        else:
            score += 1             
    return score



def main():
    s = input("Δdwse leksh h frash: ")
    print("Score:", wordScore(s))



main()
