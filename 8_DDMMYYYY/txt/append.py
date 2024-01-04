# test.txt:
# Hello World

with open("test.txt", "a") as file:
    file.write('\nGoodbye World')

# test.txt:
# Hello World
# Goodbye World
