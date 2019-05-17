def lone_sum(a, b, c):
    if a == b and a == c and b == c: #Adjusted the "and" statement to the top
        return 0
    elif a == c:
        return b
    elif b == c:
        return a
    elif a >= b:
        return c
    else:
        return a+b+c

print(lone_sum(1,1,1)) #(1,1,1) will now return 0. Before it would return 1.

# original code
#    if a >= b:
#        return c
#    elif a == c:
#        return b
#    elif b == c:
#        return a
#    elif a == b and a == c and b == c:
#        return 0
#    else:
#        return a+b+c
# If you print(love_sum(1,1,1)) it would return 1 instead of 0.
