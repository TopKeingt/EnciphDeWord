from core.Config import alphabet

class Additive_Cipher:

    """
        Name: The Additive Cipher
        Description: An encryption and decryption technique that use key provide (1-26) and adding it to each number that represent letter in alphabet.
        Possibility: 26
        Author: @Khiem Nguyen

        [+] Please only use digits as key
        HINT:
            Your key: 999
    """

    def __init__(self, msg, key):
        self.msg = msg
        if key == None:
            try:
                self.key = int(input('Your key: '))
            except ValueError as e:
                raise ValueError() 

    def encrypt(self): 
        encrypt_num_list = []
        result = []
        for letter in self.msg.lower():
            if not letter.isalpha():
                encrypt_num_list.append(letter)
            else:
                encrypted_number = (alphabet.get(letter) + self.key)
                if encrypted_number > 26:
                    encrypt_num_list.append(encrypted_number - 26)
                else:
                    encrypt_num_list.append(encrypted_number)

        for number in encrypt_num_list:
            if type(number) != int:
                result.append(number)
            else:
                for letter, index in alphabet.items():
                    if number == index:
                        result.append(letter.upper())

        return ''.join(result)

    def decrypt(self):
        decrypt_num_list = []
        result = []

        for letter in self.msg.lower():
            if not letter.isalpha():
                decrypt_num_list.append(letter)
            else:
                decrypt_number = alphabet.get(letter)
                if (self.key - decrypt_number) < 0:
                    decrypt_num_list.append(decrypt_number - self.key)
                else:
                    decrypt_number = decrypt_number - self.key + 26
                    decrypt_num_list.append(decrypt_number)
                    
        for number in decrypt_num_list:
            if type(number) != int:
                result.append(number)
            else:
                for letter, index in alphabet.items():
                    if number == index:
                        result.append(letter)

        return ''.join(result)