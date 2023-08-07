import random, string

words = (set(string.ascii_letters) | set(string.digits) | set('!#$%&@')) - set('lI10oO')


def generate_password(length):
    password = []
    password = (random.sample(words, length))
    while check_passwords(password) == False:
        password.clear()
        password = (random.sample(words, length))

    return "".join(password)


def generate_passwords(count, length):

    return [generate_password(length) for _ in range(count)]

def check_passwords(password):
    """Функция для в обязательного присутствия в пароле :
    - цифры;
    - буквы в верхнем регистре;
    - буквы в нижнем регистре;
    - спецсимвола из набора '!#$%&@'."""
    
    s = [0, 0, 0, 0]
    for i in password: 
        if i in string.ascii_uppercase:
            s[0] = 1
        if i in string.ascii_lowercase:
            s[1] = 1
        if i in string.digits:
            s[2] = 1
        #if i in set('!#$%&@') and s[3] == 1:
        #    s[4] = 1        
        if i in set('!#$%&@'):
            s[3] = 1
                
        if sum(s) == 4:
            return True
    return False

n, m = int(input("Enter the number of passwords ")), int(input("Enter the password length "))

print(*generate_passwords(n, m), sep="\n")