# This is the practice playground for python

sentence = ['hi', 'no'] # Unpack Tuple
X, x = sentence

print(X, x)

w = 55

def display():
    global w        # this make w become global
    w = 60j          # will overwrite the value of w (inside function)
    print(w + 4)

display()

print(type(w))            