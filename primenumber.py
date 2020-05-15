def countPrimes(n):
    is_prime = [True]*n
    i = 2 
    while i*i < n:
        if is_prime[i]:
            j = i * i
            while j < n:
                is_prime[j] = False
                j += i
        i = i + 1
    count = 0
    for i in range(2,n):
        if is_prime[i]:
            count += 1

    return count
                

if __name__ == '__main__':
    print(countPrimes(5))