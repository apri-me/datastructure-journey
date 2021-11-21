import string
from random import choice, randint

# We needed this to generate ascii character strings for testing radix_sort
def generate_test(ln):
    characters = string.ascii_lowercase
    test_str =  "".join(choice(characters) for _ in range(ln))
    return test_str


out = []
for i in range(100):
    out.append(generate_test(randint(1, 10)))

print(out)