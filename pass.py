
#Validating conditions for creating a password
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z] 
#3. At least 1 character from [$#@] 
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12

#create a valid password
password = input("Enter your password: ")

# function to check for valid password
def check_passwd(password): 
      
    spl_chr =['$', '@', '#'] 
    val = True

# checks minimum length of password  
    if len(password) < 6 : 
        print('Password length should be larger than 6') 
        val = False

# checks maximum length of password          
    if len(password) > 12: 
        print('Password length exceeds 12 characters') 
        val = False

# checks atleast one digit in password        
    if not any(x.isdigit() for x in password): 
        print('Password must have one number') 
        val = False

# checks atleast one capital character in password        
    if not any(x.isupper() for x in password): 
        print('Password must have one capital character') 
        val = False
        
# checks atleast one small character in password        
    if not any(x.islower() for x in password): 
        print('Password must have one small character') 
        val = False

# checks atleast one special character in password        
    if not any(x in spl_chr for x in password): 
        print('Password must have one of the symbols $@#') 
        val = False
    
    
    return val


# function to encrypt the password if valid
def encrypt_password(password,key): 
    encrypted = "" 
  
    # traverse text 
    for i in range(len(password)): 
        character = password[i] 
  
        # Encrypt uppercase characters 
        if (character.isupper()): 
            encrypted = encrypted+chr((ord(character) + key-65) % 26 + 65) 
  
        # Encrypt lowercase characters
        elif (character.islower()):   
            encrypted = encrypted+chr((ord(character) + key - 97) % 26 + 97) 

        # do not encrypt digit and special characters    
        else:
            encrypted = encrypted+character
  
    return encrypted 
 
# function to decrypt the password if valid 
def decrypt_password(encrypted, key):
    translated = ""

    # traverse text
    for letter in encrypted:

        # Decrypt uppercase characters
        if (letter.isupper()):
            translated = translated+chr(65 + ((ord(letter)-65) - key)%26)

        # Decrypt lowercase characters
        elif (letter.islower()):
            translated = translated+chr(97 + ((ord(letter)-97) - key)%26)

        # Do not decrypt digits and special characters
        else:
            translated = translated+letter
            
    return translated
    
    
# DOB = 04/07/1996 and key=(sum_of_digits(DOB)%26)
key = 36%26

# If password is valid then encrypt it   
if (check_passwd(password)): 
    print("You have successfully created a valid Password") 
    print ("Password  : " + password) 
    print ("Shift : ",key) 
    code = encrypt_password(password,key)
    print ("Cipher: " + code)

    # if wants to decrypt the password   
    var = input("Do you want to decrypt the code (y/n): ")

    if var=="y":
        #Enter the key to decrypt the password
        key = int(input("Enter the key for decryption: "))
        print("Your decrypted password is: ",decrypt_password(code, key))
else: 
    print("Invalid Password! Try Again")
