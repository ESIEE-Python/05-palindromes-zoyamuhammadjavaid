#### Fonction secondaire
"""Fonction secondaire qui vérifie si le mot donné est palindrome, il élimine ainsi toutes les chaines avec des tirets etc"""

def ispalindrome(p):
    accents = str.maketrans("éèêëàâäôöùûüîïç","eeeeaaaoouuuiic"," ")
    p = p.lower().translate(accents)
    s = ''
    for i in p :
        if ('a' <= i <= 'z') or ('0'<= i <= '9'):
            s += i
    if s == s[::-1]:
        return True
    else:
        return False

#### Fonction principale


def main():

    """Ici on va appliquer le focntion à ces cas"""

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()