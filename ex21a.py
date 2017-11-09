# These lines are an attempt to work out how the
# 'return' function works.
def foo (a, b):
    print(f"foo is {a} + {b}")
    return a + b

def bar(a):
    print("bar is foo * 2")
    return a * 2

f = foo(1, 2)
print("foo = ", f)

b = bar(f)
print("bar = ", b)
