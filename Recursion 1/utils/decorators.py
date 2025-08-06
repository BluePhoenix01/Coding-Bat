def cache(func):
    store = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in store:
            return store[key]
        else:
            result = func(*args, **kwargs)
            store[key] = result
            return result
        
    return wrapper