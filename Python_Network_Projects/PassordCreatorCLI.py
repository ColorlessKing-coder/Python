import argparse
from rich import pretty,print
import random



def ArgParserCreate():  
    Parser = argparse.ArgumentParser(description='PasswordCreator' ,add_help=True)
    Parser.add_argument('-v','--version',version='PasswordCreater 1.0',action='version')
    Parser.add_argument('-u','--UpperCase',help='Your Password Will Contains Upper Case Alfabet' ,dest='uppercase',action='store_true')
    Parser.add_argument('-l','--LowerCase',help='Your Password Will Contains Lower Case Alfabet' ,dest='lowercase',action='store_true')
    Parser.add_argument('-n','--Numbers',help='Your Password Will Contains Numbers' ,dest='numeric',action='store_true')
    Parser.add_argument('-s','--SpecialCharacter',help='Your Password Will Contains Specials Character',dest="specialchar",action='store_true')
    Parser.add_argument('--Password_length',help="Enter Password Length",dest="passwordlength",type=int,default=11)
    Parser.add_argument('-c','--Count',help='How many time Do You Will Create Password',dest='count',default=1 ,type=int)
    Parser.add_argument('--UserValue',help='Please Enter Specify Your Wordlist',dest='uservalue')
    Parser.add_argument('--Noexist',help='Please Exclude Words On Your Password',dest='noexist',default="")
    Parser.add_argument('-f','--fileName',help='Save The Password List', default="Passwordlist.txt",dest='newfile')
    Arguments = Parser.parse_args()
    return Arguments
    
Wordlist = []

def PasswordCreateAllIn(Password_length:int,UpperCase:bool,LowerCase:bool,NumericCase:bool,SpecialCharCase:bool,UserValue,Exist):
    ValueCharactersUpper = "ABCDEFGHIIJKLMNOPRSTUVYZX"
    ValueChraracterLower = "abcdefghijklmnoprstuvyzx"
    ValueCharacterNumber = "0123456789"
    ValueCharcterSpacial = "/!':^&%()=?_-{}"
    CharacterAll = ""
     
    if UserValue:
        CharacterAll += UserValue
    
    if UpperCase:
        CharacterAll += ValueCharactersUpper
    
    if LowerCase:
        CharacterAll += ValueChraracterLower

    if NumericCase:
        CharacterAll += ValueCharacterNumber
    
    if SpecialCharCase:
        CharacterAll += ValueCharcterSpacial
    

    for x in Exist:
        CharacterAll = CharacterAll.replace(x,"")        

    if not CharacterAll:
        print("Please specify at least one character set to include in the password.")
        return
    
    try:
        password = ''.join(random.choices( CharacterAll, k=Password_length))
        print("[bold red]Your Password:[/bold red]", password)
        Wordlist.append(password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

def CreateNewFile(FileName:str,Text:str):
    try:
        with open(FileName,'w+',encoding='utf-8') as file:
            for line in Text:
                file.write(line + "\n")
    except Exception as e:
        pretty("Bir Hata İle Karşılaşıldı ")   

if __name__ == '__main__':
    args = ArgParserCreate()#Burada Değerlerin Varlığını Kontrol Etmek İçin Çağırdık 
    
    

    for _ in range(args.count):
        PasswordCreateAllIn(args.passwordlength, args.uppercase, args.lowercase, args.numeric, args.specialchar,args.uservalue,args.noexist)

    for y in Wordlist:
        CreateNewFile(args.newfile,Wordlist)  


#if '-c' or '--count' and '-u' or '--UpperCase' and '-l' or '--LowerCase' and '-n' or '--Numbers' and '-s' or '--SpecialCharacter' and '-pl' or '--password_length'in Args.input: #Sadece Bir Örnek
    #PasswordCreateAllIn(Args.passwordlength,Args.uppercase,Args.lowercase,Args.specialchar,Args.numeric)

