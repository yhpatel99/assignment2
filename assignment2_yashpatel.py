import random
import string
import os
import time

class PasswordGenerator:
    def __init__(self, words_file):
        with open(words_file, 'r') as file:
            self.words = [line.strip() for line in file.readlines()]

    def generate_memorable_password(self, num_words, cases):
        selected_words = random.sample(self.words, num_words)
        if cases == 'upper':
            selected_words = [word.upper() for word in selected_words]
        elif cases == 'title':
            selected_words = [word.title() for word in selected_words]
        elif cases == 'lower':
            selected_words = [word.lower() for word in selected_words]
        
        memorable_password = '-'.join(word + str(random.randint(0, 9)) for word in selected_words)
        return memorable_password

    def generate_random_password(self, length, include_punctuation, disallowed_chars):
        char_set = string.ascii_letters + string.digits
        if include_punctuation:
            char_set += string.punctuation
        
        char_set = ''.join(ch for ch in char_set if ch not in disallowed_chars)
        random_password = ''.join(random.choice(char_set) for _ in range(length))
        return random_password

    def log_password(self, password, password_type):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        directory = password_type.capitalize()
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, "Generated_Passwords.txt")
        with open(file_path, 'a') as file:
            file.write(f"{timestamp}: {password}\n")

    def generate_password(self):
        password_type = input("Enter password type (memorable/random): ").strip().lower()
        if password_type == 'memorable':
            num_words = int(input("Enter number of words: "))
            cases = input("Enter case (lower/upper/title): ").strip().lower()
            password = self.generate_memorable_password(num_words, cases)
            self.log_password(password, 'memorable')
            return password
        elif password_type == 'random':
            length = int(input("Enter password length: "))
            include_punctuation = input("Include punctuation (yes/no): ").strip().lower() == 'yes'
            disallowed_chars = input("Enter disallowed characters (leave blank if none): ").strip()
            password = self.generate_random_password(length, include_punctuation, disallowed_chars)
            self.log_password(password, 'random')
            return password
        else:
            return "Invalid password type."

# Example usage:
generator = PasswordGenerator('top_english_nouns_lower_100000.txt')

# Generate 1000 passwords randomly choosing between memorable and random
for _ in range(1000):
    password_type = random.choice(['memorable', 'random'])
    if password_type == 'memorable':
        num_words = random.randint(2, 5)  # Random number of words between 2 and 5
        cases = random.choice(['lower', 'upper', 'title'])
        password = generator.generate_memorable_password(num_words, cases)
        generator.log_password(password, 'memorable')
    else:
        length = random.randint(8, 16)  # Random length between 8 and 16
        include_punctuation = random.choice([True, False])
        disallowed_chars = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(0, 5)))
        password = generator.generate_random_password(length, include_punctuation, disallowed_chars)
        generator.log_password(password, 'random')