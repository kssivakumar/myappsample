def most_common_letters(s):
    frequencies = count_freqs(s)
    return best_key(frequencies)

def count_freqs(st):
    d = {}
    for c in st:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    return d

def best_key(dictionary):
    ks = dictionary.keys()
    best_key_so_far = list(ks)[0]
    for k in ks:
        if dictionary[k] > dictionary[best_key_so_far]:
            best_key_so_far = k
    return best_key_so_far

print(most_common_letters("ccccccccbbbbbbbbbbbbbbbbbbdddddddddddddeeeeeeeee"))

#Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5.
#mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(x):
    y = int(x) + 5
    return y
result = addit(input())

def mult(s):
    z = int(s) * result
    return z
result1 = mult(input())

print(result1)


def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)
