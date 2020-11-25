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
    if number >= 500:
        message.append("Nombre trop grand")
    if number < 2:
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


def mod_inverse(e, phi):
    """
    Fonction détermine l'inverse modulaire.
    Prend en agrument e, phi.
        trouve le multiple d pour que (e*d)%phi =1
    Retourne d.
    """
    for d in range(1, phi):
        if (e*d) % phi == 1:
            return d
    return -1


def gen_phi(p, q):
    """
    Génère phi_n = (p - 1)*(q - 1)
    phi est le nombre de facteurs co-premier avec N
    """
    return (p - 1)*(q - 1)


def coprime(e, phi):
    if gcd(e, phi_n) == 1:
        return True
    return False


def gen_pseudo_e(phi, e = 2, bit_lenght = 1):
    """
    Fonction génaire un e temporaire.
    Prend en agrument e, phi et une longeure min en nombre de bit pour e.
    La convertion bit_lenght(b) et digit(n) : b = log_2(n + 1)
                                                n = 2**b - 1
    Retourne e.
    """
    if e < (2**bit_lenght - 1):
        e = 2**bit_lenght
    if e > phi:
        return -1
    if gcd(e, phi) == 1 and e < phi:
        return e

    return gen_pseudo_e(phi, e+1, bit_lenght)


def gen_e_d(phi, bit_lenght = 1, e = 2):
    """
    Fonction génaire un e et d.
    Prend en agrument e, phi et une longeure min en nombre de bit pour e.
        génaire un d puis un e et regarde les conditions
        si incapable de générer e et d lève une erreur 
    Retourne tuple (e, d).
    """
    d = mod_inverse(e, phi)
    e = gen_pseudo_e(phi, bit_lenght, e)
    if gcd(e, phi) == 1 and e != d and d != -1 and e != -1:
        return e, d
    if d == -1 and e == -1:
        raise Exception("La création de e et d est imposible, choisisez d'autres p et q")
    return gen_e_d(phi, bit_lenght, e+1)


def gen_keys(p, q, bit_lenght = 1):
    """
    Fonction génaire les clés.
    Prend en agrument p, q et un longeur min en nb de bit.
        trouve n
        trouve phi
        trouve e et d
    Retourne tuple ((e, n), (d, n)).
    """
    n = p*q
    phi = gen_phi(p, q)
    try:
        e, d = gen_e_d(phi, bit_lenght)
    except:
        print("La création de e et d est imposible, choisisez d'autres p et q")
    return ((e, n), (d, n))


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
    retourne [pow(ord(lettre), e, n) for lettre in message]


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
    return [char(pow(crypt, d, n) for crypt in msg_crypt)]


def show_encrypt(liste):
    """
    Fonction regroupe le message crypté.
    Prend en agrument le message crypter (list, voir fonc encrypt).
        chr retourne le str d'une valeur numérique(unicode)  
            ex : char(97) = a
    Retourne le message crypter.
        ex: 'Hello'
    """
    message = ''
    for number in liste:
        message += char(liste[number])
    return message


def show_decrypt(liste):
    """
    Fonction regroupe le message décrypté.
    Prend en agrument le message décrypter (list, voir fonc encrypt).
    Retourne le message décrypter.
        ex: 'Hello'
    """
    return (''.join(liste))


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


def print_justify(text, width=70, close=False, sep=' ', justify_last_line=False):
    """
    Fonction imprime dans le terminale.
    Prend en agrument une liste.
        Si l'argument close == False, ajoute une ligne vide 
    Retourne Rien.
    """
    new_text = justify(text, width, sep, justify_last_line)
    if not close:
        new_text += " "
    for line in new_text:
        print(line)




def alice_create_clef(len_text=70):
    context = "Bob veut envoyer un message d\'amour à Alice sans que personne " \
                "ne puisse intercepter leurs ferveurs. Alice doit donc créer " \
                "une clé privée, pour lire les messages cryptés de Bob, et une " \
                "clé publique qu\'elle laissera sur son casier. Bob utilisera la " \
                "clé publique pour crypter son message. Pour créer les clés, Alice " \
                "doit choisir deux grands nombres premiers."

    prime_context = "Choisissez deux nombres (entier entre 2 et 500) le programme " \
                    "trouvera le prochain nombre qui est premier."

    print_justify(context, len_text)
    print_justify(prime_context, len_text)
    text_number_1 = input("Premier nombre : ")
    prime_1 = find_prime(number_1)
    text_number_2 = input("Deuxième nombre : ")
    prime_2 = find_prime(number_2)
    print_justify(f"Le couple de nombre premier (p, q) est : {prime_1}, {prime_2}", len_text, True)
    
    print_justify(f"Produit des deux nombres premiers nommés N = {N}", len_text, True)
    print_justify(f"Phi_n = (prime1-1)(prime2-1) = {phi_n}", len_text, True)

    print_justify(f"Choix de d => d*e % phi_n = 1 : {d_choises}", len_text, True)
    print_justify(f"Choix de e => copremier avec N et phi_n dans ]1, phi_n[ : {e_choices}", len_text)
    print_justify(f"La clé publique (e, N) = ({e}, {N})", len_text, True)
    print_justify(f"La clé privée est (d, N) = ({d}, {N})", len_text)

    return [[e, N], [d, N]]


def bob_message(len_text=70):
    clef = alice_create_clef(len_text)
    N = clef[0][1]
    e = clef[0][0]
    d = clef[1][0]

    context_salutation = 'Bonjour Bob,'
    context_instruction = 'Écrivez votre message à envoyer à Alice. Je me chargerai de le crypter.'
    print_justify(context_salutation, len_text, True)
    print_justify(context_instruction, len_text)
    message = input('Message d\'amour : ')

    cyber_text = []
    crypted_text = []

    for i in message:
        cyber_text.append(int(table_cryptage[i]))

    print('cyber_text : ', cyber_text)
    for k in cyber_text:
        mod_crypt = (k**e) % N
        if not mod_crypt:
            mod_crypt = 82
            if not (82 % N):
                mod_crypt = 79
        crypted_text.append(mod_crypt)

    print('crypted_text : ', crypted_text)

    return (crypted_text, d, N)


def alice_decrypt(len_text=70):
    crypted_message, d, N = bob_message(len_text)

    message_decrypt = ""
    context = 'Alice a reçu un message dans sa case. ' \
              'Elle le passe dans son programme de décryption'

    print_justify(context, len_text)

    for number in crypted_message:
        mod_decrypt = base107(((int(number)**d) % N))
        if mod_decrypt == 0:
            mod_decrypt = 1
        message_decrypt += table_decryptage[three_digit(mod_decrypt)]

    print_justify(f'Le message reçu : {message_decrypt}', len_text)


