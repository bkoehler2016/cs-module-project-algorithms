'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    #base case
    if n < 0:
        return 0
    if n == 0:
        return 1
    #moving closer to the base case and setting up cache
    if cache is None:
        cache = {}
    elif isinstance(cache, list):
        cache = dict.fromkeys(cache)
    if n in cache:
        return cache[n]
    one_cookie = eating_cookies(n - 1, cache)
    two_cookies = eating_cookies(n - 2, cache)
    three_cookies = eating_cookies(n - 3, cache)
    
    cache[n] = one_cookie + two_cookies + three_cookies
    
    return cache[n]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to eat {num_cookies} cookies")
