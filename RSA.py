import textwrap
from random import randint as rand


def num_condition(number):
    """
    Fonction détermine si 
        le nombre respecte des conditions.
    Prend en agrument un nombre.
        1-Essaie de rendre le nombre entier.
        2-Regarde la borne supérieure.
        3-Regarde la borne inférieure.
    Retourne une liste avec un booléen et un message.
    """
    condition = False
    message = []
    try:
        number = int(number)
    except ValueError:
        message.append("Ce n'est pas un nombre")
        return [condition, message]
    if number >= 5000:
        message.append("Nombre trop grand")
    if number < 20:
        message.append("Nombre trop petit")
    else:
        condition = True
    return [condition, message]


def even(number):
    """
    Fonction détermine si le nombre est paire.
    Prend en agrument un nombre.
    Retourne un booléen.
    """
    if number % 2 == 0:
        return True
    else:
        return False


def find_prime(number):
    """
    Fonction détermine le prochain nombre premier.
    Prend en agrument un nombre.
        1-Regarde si num_condition == True.
        2-Regarde si le num est 2. Si oui retourne 2.
        3-Tant qu'un num n'est pas premier la boucle while recommence.
        4-Regarde si le num est paire. Si oui il n'est pas premier.
            et on augmente num de 1 pour qu'il soit impaire(sauf 2).
        5-Itération de k sur lintervale [3, racine(num)+1] en sautant les paire.
        6-Regarde si num%k = 0. Si oui le num n'est pas premier.
        7-Augmente num de deux et recommence la boucle while à 3-.
        8-Si le num n'est pas paire,
            ni divisible par tous nombre impaire entre [3, racine(num)+1],
            alors le num est premier et la fonction le retourne.

    Retourne un nombre premier ou un message.
        si num_conditions == False
    """
    if num_condition(number)[0]:    #1-
        prime = False
        number = int(number)
        if number == 2:             #2-
            return 2
        while not prime:            #3-
            prime = True
            if even(number):        #4-
                number += 1
            for k in range(3, int(number**0.5) + 2, 2):     #5-
                if number % k == 0: #6-
                    prime = False
                    number += 2     #7-
            if prime:               #8-
                return number
    return f'Votre saisie : {number}\nest invalide : {", ".join(num_condition(number)[1])}'


def gcd(number1, number2):
    """
    Fonction détermine le gcd de deux nombre avec l'algorithme d'Euclide.
        gcd(a, b) = gcd(b, a*mod(b))
        la fonction prend le reste et divise l'ancien reste par ce dernier.
        ex: 91%126 = 91 = reste1
        126%reste1 = 126%91 = 35 = reste2
        reste1%reste2 = 91%35 = 21 = reste3
        reste2%reste3 = 35%21 = 14 = reste4
        reste3%reste4 = 21%14 = 7 = reste5
        reste4%reste5 = 14%7 = 0 = reste6
        gcd(91, 126) = reste5 = 7
    Prend en agrument un nombre.
        1-Associe un nombre arbitraire sans importance, mais > 0.
        2-Boucle tant que remainder != 0.
        3-remaider = num1*mod(num2).
        4-num2 devient num1 et remainder devient num2.
    Retourne un num.

    Si gcd(i, j) = 1, alors i et j sont co-premier
    """
    if number2 == 0:
        return number1
    else:
        return gcd(number2, number1%number2)


def period(arg, n, exponent = 1,count = 1):
    """
    Fonction détermine la période pour que (arg**k)mod(n) = 1.
        ex: (2**k)mod(7)
        (2**1)mod(7) = 2
        (2**2)mod(7) = 4
        (2**3)mod(7) = 1
        période = k = 3
    Prend en agrument deux nombres.
    Retourne un numbre.
    """
    if (arg**exponent)%n == 1:
        return count
    exponent += 1
    count += 1
    return period(arg, n, exponent, count)


def mod_inverse(e, phi, n):
    """
    Fonction détermine l'inverse modulaire.
    Prend en agrument e, phi, n.
        trouve le multiple d pour que (e*d)%phi =1
    Retourne d.
    """
    for d in range(n):
        if (((e*d) % phi) == 1 and d != e):
            return d
    return -1



def find_coprime(e, phi):
    """
    Fonction retourne un nombre e co-premier à phi.
    Prend en argument e, phi.
        retourne -1 si e > phi
    Retourne e
    """
    if e >= phi:
        return -1
    if gcd(e, phi) == 1:
        return e
    return find_coprime(e+1, phi)


def gen_e_d(n, phi, bit_lenght = 2, e = 4):
    """
    Fonction génère un e et d.
    Prend en agrument n, phi, bit_leght, e où bit_lenght
                est une longeure min en nombre de bit pour e.
        génère un e puis un d et regarde les conditions
        si incapable de générer e et d lève une erreur 
    Retourne tuple (e, d).
    """
    if e <= (2**bit_lenght - 1):
        e = 2**bit_lenght

    e = find_coprime(e, phi)
    d = mod_inverse(e, phi, n)
    if  d != -1 and e != -1:
        return (e, d)
    if d == -1 and e == -1:
        raise Exception("La création de e et d est imposible, choisisez d'autres p et q")
    return gen_e_d(phi, bit_lenght, e+1)


def gen_keys(p, q, bit_lenght = 2):
    """
    Fonction génère les clés.
    Prend en agrument p, q et un longeur min en nb de bit.
        trouve n
        trouve phi
        trouve e et d
    Retourne tuple ((e, n), (d, n)).
    """
    n = p*q
    phi = (p - 1)*(q - 1)
    try:
        e, d = gen_e_d(n, phi, bit_lenght)
        return ((e, n), (d, n), phi)
    except:
        raise Exception("La création de e et d est imposible, choisisez d'autres p et q")


def encrypt(message, public_key):
    """
    Fonction encrypt le message.
    Prend en agrument le message (str) et la clé publique.
        ord retourne la valeur numérique(unicode) d'un str 
            ex : ord(a) = 97
        pow(a, b, c) retourne (a**b)%c
    Retourne une liste de la valeur num de chaque lettre du message.
        ex: ['32', '103', '98']
    """
    e, n = public_key
    return list([pow(ord(lettre), e, n) for lettre in message])


def decrypt(msg_crypt, private_key):
    """
    Fonction décrypt le message crypter.
    Prend en agrument le message crypter (list, voir fonc encrypt) et la clé privé.
        chr retourne le str d'une valeur numérique(unicode)  
            ex : char(97) = a
        pow(a, b, c) retourne (a**b)%c
    Retourne une liste de lettre du message décrypter.
        ex: ['H', 'e', 'l', 'l', 'o']
    """
    d, n = private_key
    return [chr(pow(crypt, d, n)) for crypt in msg_crypt]


def justify(text, width=70, sep=' ', justify_last_line=False):
    """
    Fonction de la librairie Textwrap
    Justifie un texte pour l'imprimer dans le terminal
    retourne une liste
    """
    # Initial wrap with Textwrapper - this will
    # chunk/approximate our lines, but return will
    # have ragged right side...like this comment does
    wrapper = textwrap.TextWrapper(width=width)
    new_text = wrapper.wrap(text)

    # Handle optional justify_last_line argument
    if not justify_last_line:
        our_range = len(new_text) - 1
    else:
        our_range = len(new_text)

    # Algorithm for actual justifying
    for word in range(our_range):
        # Break the current textwrapped line further down into words only.
        # (!== ASSUMES WORDS HAVE ' ' BETWEEN THEM ==!)
        line = new_text[word].split(' ')

        # This counter helps us start at the second to the last word; IOW, the word before the last space.
        # We will use it to walk backward through the line, adding a space between words until our line
        # is exactly n characters long
        counter = -2

        # Test whether line is exactly n characters long
        while len(new_text[word]) < width:

            # Test/handle for one word line.
            if len(line) < 2:
                new_text[word] += sep
                continue

            # If it's short...
            try:

                # ...add our seperator character to the end of the word before the last space...
                line[counter] += sep

                # ..then increase counter by one to walk back to the next previous word...
                counter += -1

                # ...put the line back together to be evaluated by while statement above.
                # Joining on the sep ensures there's at least a single space between the words.
                # we just borrowed it above b/c it was there.  ;D
                new_text[word] = sep.join(line)

            except IndexError:
                # Resets counter to start at word before final space, if we've stepped through the list once
                counter = -2
    return new_text


pp = 100000
ppp = 100000
nn = pp*ppp
ll = len(str(184787))
print(ll)
print(2**ll - 1)
print(find_coprime(64, 180240))