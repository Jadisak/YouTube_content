import wikipedia
wikipedia.set_lang("en")
query = str(input('Enter what you wanna search:\t'))
print(wikipedia.summary(query))