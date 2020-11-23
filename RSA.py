import random
import textwrap


table_criptage = {
                    'a': '001', 'b': '002', 'c': '003', 'd': '004', 'e': '005', 'f': '006', 'g': '007', 'h': '008',
                    'i': '009', 'j': '010', 'k': '011', 'l': '012', 'm': '013', 'n': '014', 'o': '015', 'p': '016',
                    'q': '017', 'r': '018', 's': '019', 't': '020', 'u': '021', 'v': '022', 'w': '023', 'x': '024',
                    'y': '025', 'z': '026', 'A': '027', 'B': '028', 'C': '029', 'D': '030', 'E': '031', 'F': '032',
                    'G': '033', 'H': '034', 'I': '035', 'J': '036', 'K': '037', 'L': '038', 'M': '039', 'N': '040',
                    'O': '041', 'P': '042', 'Q': '043', 'R': '044', 'S': '045', 'T': '046', 'U': '047', 'V': '048',
                    'W': '049', 'X': '050', 'Y': '051', 'Z': '052', '0': '053', '1': '054', '2': '055', '3': '056',
                    '4': '057', '5': '058', '6': '059', '7': '060', '8': '061', '9': '062', ' ': '063', "'": '064',
                    ':': '065', ';': '066', '.': '067', '<': '068', '>': '069', '«': '070', '»': '071', '%': '072',
                    '=': '073', '-': '074', '+': '075', '/': '076', '\\': '077', '*': '078', '#': '079', '@': '080',
                    '!': '081', '?': '082', '&': '083', '(': '084', ')': '085', '_': '086', '{': '087', '}': '088',
                    '"': '089', ',': '090', '$': '091', '[': '092', ']': '093', 'é': '094', 'è': '095', 'ê': '096',
                    'É': '097', 'È': '098', 'Ê': '099', 'à': '100', 'À': '101', 'ç': '102', 'Ç': '103', 'ù': '104',
                    'Ù': '105', 'î': '106', 'Î': '107'
                }


def inverse_dico(dico):
    """
    Fonction inverse la clé avec sa valeur dans un dictionnaire.
        ex: {'A':1} => {'1':'A'}.
    Prend en agrument un dictionnaire.
    Retourne un dictionnaire.
    """
    inv_dico = {}
    for keys in dico:
        inv_dico[dico[keys]] = keys
    return inv_dico


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
        gcd(91, 126) = reste5
    Prend en agrument un nombre.
        1-Associe un nombre arbitraire sans importance, mais > 0.
        2-Boucle tant que remainder != 0.
        3-remaider = num1*mod(num2).
        4-num2 devient num1 et remainder devient num2.
    Retourne un num.
    """
    remainder = 1   #1-
    while remainder > 0:    #2-
        remainder = number1 % number2   #3-
        number1, number2 = number2, remainder
    return number1


def period(arg, n):
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
    remainder = 0
    laps = 0
    exponent = 1
    while remainder != 1:
        remainder = (arg ** exponent) % n
        exponent += 1
        laps += 1
    return laps


def three_digit(number):
    """
    Fonction rend un nombre sur trois digits.
    Prend en agrument un nombre.
    Retourne un string.
    """
    if number < 100:
        digit = '0' + str(number)
        if number < 10:
            digit = '0' + digit
    else:
        digit = str(number)
    return digit


def justify(text, width=70, sep=' ', justify_last_line=False):
    """
    Fonction de la librairie justify
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
    number_1 = input("Premier nombre : ")
    prime_1 = find_prime(number_1)
    number_2 = input("Deuxième nombre : ")
    prime_2 = find_prime(number_2)
    print_justify(f"Le couple de nombre premier (p, q) est : {prime_1}, {prime_2}", len_text, True)
    N = prime_1*prime_2
    print_justify(f"Produit des deux nombres premiers nommés N = {N}", len_text, True)
    phi_n = ((prime_1 - 1)*(prime_2 - 1))
    print_justify(f"Phi_n = (prime1-1)(prime2-1) = {phi_n}", len_text, True)
    e_choices = []
    for i in range(3, phi_n):
        if gcd(i, phi_n) == 1:
            e_choices.append(i)
    if len(e_choices) < 2:
        e = e_choices[0]
    e = e_choices[0] # random.randint(0, len(e_choices)-1)
    # d*e(mod(phi_n))=1 => d=k*(phi_n)-1
    # (ici k soit 2 ou 3 pour éviter trop grand nombre)
    d_choise = []
    k = 0
    while len(d_choise) < 3:
        k += 1
        d_intermediate = int(((k * phi_n) + 1)/e)
        if ((d_intermediate*e) % phi_n) == 1:
            d_choise.append(d_intermediate)

    d = d_choise[random.randint(0, 2)]
    print_justify(f"Choix de d => d*e % phi_n = 1 : {d_choise}", len_text)
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
        cyber_text.append(int(table_criptage[i]))

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
        mod_decrypt = ((int(number)**d) % N)
        if mod_decrypt > 107:
            mod_decrypt %= 107
        message_decrypt += table_decriptage[three_digit(mod_decrypt)]

    print_justify(f'Le message reçu : {message_decrypt}', len_text)
