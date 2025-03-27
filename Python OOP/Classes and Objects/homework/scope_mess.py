"""
# current output
global
outer: local
inner: nonlocal
outer: local
global

# expected output
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
"""

x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x # this row was added
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x # this row was added
        x = "global: changed!"

    print("outer:", x) # outer: x = local
    inner() # inner: x = nonlocal
    print("outer:", x) # outer: x = local , changed to `nonlocal x`
    change_global()

print(x) # x = global
outer()
print(x) # x = global, changed to `global x`