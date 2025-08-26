# my_module/second.py

def greet(name):
    return f"Hello, {name}! I am creating my own module"


def reverse_string(string):
    return string[::-1]


def count_characters(string):
    return len(string)


def count_words(string):
    return len(string.split())

def count_sentences(string):
    return len(string.split("."))