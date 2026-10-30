import random

data_quotes = [
("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt"),
("To be or not to be, that is the question.", "William Shakespeare"),
("In the world of words, the imagination is one's value.", "Wallace Stevens"),
("I think, therefore I am.", "René Descartes"),
("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
("The only true wisdom is in knowing you know nothing.", "Socrates"),
("That which does not kill us makes us stronger.", "Friedrich Nietzsche"),
("Live as if you were to die tomorrow. Learn as if you were to live forever.", "Mahatma Gandhi"),
("The purpose of our lives is to be happy.", "Dalai Lama"),
("Life is what happens when you're busy making other plans.", "John Lennon"),
("Strive not to be a success, but rather to be of value.", "Albert Einstein"),
("The greatest glory in living lies not in never falling, but in rising every time we fall.", "Nelson Mandela")
]


#take 10 random numbers data_quotes
#choices(): allows you to ensure that the 10 chosen numbers can have repetitions.
books = random.choices(data_quotes, k=10)

print("================== QUOTES==============")
for quote, author in books:
    print(f' "{quote}" — {author}')
