def count_steps(n):
    if n <= 0:
        return 0
    
    return count_steps(n-3)+count_steps(n-2)+count_steps(n-1)

print(count_steps(3))