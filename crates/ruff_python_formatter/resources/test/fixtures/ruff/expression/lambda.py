# Leading
lambda x: x  # Trailing
# Trailing

# Leading
lambda x, y: x  # Trailing
# Trailing

# Leading
lambda x, y: x, y  # Trailing
# Trailing

# Leading
lambda x, /, y: x  # Trailing
# Trailing

# Leading
lambda x: lambda y: lambda z: x  # Trailing
# Trailing

# Leading
lambda x: lambda y: lambda z: (x, y, z)  # Trailing
# Trailing

# Leading
lambda x: lambda y: lambda z: (
    x,
    y,
z)  # Trailing
# Trailing

# Leading
lambda x: lambda y: lambda z: (
    x,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
    y,
z)  # Trailing
# Trailing

a = (
    lambda  # Dangling
           : 1
)

a = (
    lambda x # Dangling
    , y: 1
)

# Regression test: lambda empty arguments ranges were too long, leading to unstable
# formatting
(lambda:(#
),)

# lambda arguments don't have parentheses, so we never add a magic trailing comma ...
def f(
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb = lambda x: y,
):
    pass

# ...but we do preserve a trailing comma after the arguments
a = lambda b,: 0

lambda a,: 0
lambda *args,: 0
lambda **kwds,: 0
lambda a, *args,: 0
lambda a, **kwds,: 0
lambda *args, b,: 0
lambda *, b,: 0
lambda *args, **kwds,: 0
lambda a, *args, b,: 0
lambda a, *, b,: 0
lambda a, *args, **kwds,: 0
lambda *args, b, **kwds,: 0
lambda *, b, **kwds,: 0
lambda a, *args, b, **kwds,: 0
lambda a, *, b, **kwds,: 0
lambda a, /: a
lambda a, /, c: a

# Dangling comments without parameters.
(
    lambda
    : # 3
     None
)

(
    lambda
    # 3
    : None
)

(
    lambda  # 1
    # 2
    : # 3
    # 4
    None # 5
)
