n = int(input())
def recursive_function(n):
    if (n!=1):
        recursive_function(n-1)
    print(n)
recursive_function(n)