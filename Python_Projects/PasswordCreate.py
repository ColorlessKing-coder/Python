import random

CharactersUpper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
ChraracterLower = "abcçdefgğhıijklmnoöprsştuüvyz"
CharacterNumber = "0123456789"
CharcterSpacial = "/!':^&%()=?_-{}"
CharacterAll = CharactersUpper + ChraracterLower + CharacterNumber + CharcterSpacial

try:
    PasswordLength = int(input("Please Enter Length Of The Password: "))
    Password = ''.join(random.sample(CharacterAll, PasswordLength))
    print("Your Password:", Password)
except ValueError:
    print("Invalid input. Please enter a valid integer for password length.")
