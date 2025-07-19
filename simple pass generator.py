import random
import string
def gen_pass (length = 14):
    lowercase= string.ascii_lowercase
    uppercase= string.ascii_uppercase
    digits= string.digits
    spl_char = string.punctuation

    all_char = lowercase + uppercase + digits + spl_char
    
    password = [ random.choice(lowercase), 
                random.choice(uppercase),
                random.choice(digits), 
                random.choice(spl_char)]
    password += random.choices(all_char, k=length-4)
    random.shuffle(password)
    return ''.join(password)
print('New password generated:', gen_pass())