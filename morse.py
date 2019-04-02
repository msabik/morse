class Morse:
    ALPHABET = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    def decode(self, message):
        if message == "":
            return ""

        words = message.split(" / ")
        decoded_words = [self.decode_word(word) for word in words]
        return ' '.join(decoded_words)

    def decode_word(self, word):
        symbols = word.split(" ")
        letters = [self.ALPHABET[s] for s in symbols]
        return ''.join(letters)
