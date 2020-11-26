from RSA import justify, find_prime, gen_keys, encrypt, decrypt

class Terminal_display_setting:
    def __init__(self, text, width=70, close=False, sep=' ', justify_last_line=False):
        self.text = text
        self.width = width
        self.close = close
        self.sep = sep
        self.justify_last_line = justify_last_line
    def __str__(self, close = False):
        new_text = justify(self.text, self.width, self.sep, self.justify_last_line)
        if not self.close:
            new_text += " "
        return self.print_justified(new_text)

    def print_justified(self, text_list):
        for ligne in text_list:
            print(ligne)
        return ''


context = "Bob veut envoyer un message d\'amour à Alice sans que personne " \
            "ne puisse intercepter leurs ferveurs. Alice doit donc créer " \
            "une clé privée, pour lire les messages cryptés de Bob, et une " \
            "clé publique qu\'elle laissera sur son casier. Bob utilisera la " \
            "clé publique pour crypter son message. Pour créer les clés, Alice " \
            "doit choisir deux grands nombres premiers."
prime_context = "Choisissez deux nombres (entier entre 20 et 500) le programme " \
                "trouvera le prochain nombre qui est premier."
text_number_1 = 'Votre premier nombre : '
text_number_2 = 'Votre deuxième nombre : '
context_salutation = 'Bonjour Bob,'
context_instruction = 'Écrivez votre message à envoyer à Alice. '\
                    'Je me chargerai de le crypter.'
context_decrypt = 'Alice a reçu un message dans sa case. ' \
                'Elle le passe dans son programme de décryption'


if __name__ == "__main__":
    len_text = 70
    context_justified = Terminal_display_setting(context)
    prime_context_justified = Terminal_display_setting(prime_context)
    context_salutation_justified = Terminal_display_setting(context_salutation)
    context_instruction_justified = Terminal_display_setting(context_instruction)
    context_decrypt_justified = Terminal_display_setting(context_decrypt)

    print(context_justified)
    print(prime_context_justified)
    number_1 = input(text_number_1)
    number_2 = input(text_number_2)

    prime_1 = find_prime(number_1)
    prime_2 = find_prime(number_2)
    public_key, private_key, phi = gen_keys(prime_1, prime_2)
    e, n = public_key
    d = private_key[0]

    print(f"Le couple de nombre premier (p, q) est : {prime_1}, {prime_2}")
    print(f"Produit des deux nombres premiers nommés N = {n}")
    print(f"Phi_n = (prime1-1)(prime2-1) = {phi}")
    print(f"d => d*e % phi_n = 1 : {d}")
    print(f"e => copremier avec phi_n dans ]1, phi_n[ : {e}")
    print(f"La clé publique (e, N) = {public_key}")
    print(f"La clé privée est (d, N) = {private_key}\n")

    print(context_salutation_justified)
    print(context_instruction)
    message = input('Message d\'amour : ')

    message_crypté = encrypt(message, public_key)
    text_crypté = ''.join(str(message_crypté))
    message_décrypter = decrypt(message_crypté, private_key)
    text_décrypté = ''.join(message_décrypter)

    print(f'Le message envoyé : {text_crypté}')

    print(context_decrypt_justified)
    print(f'Le message reçu : {text_décrypté}')
