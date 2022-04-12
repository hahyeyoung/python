n = int(input())
def recursive_function(n):
    print(n)
    if (n!=1):
        recursive_function(n-1)
recursive_function(n)