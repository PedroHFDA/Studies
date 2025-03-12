# Decoradores
#'Syntax Sugar'

def create_func(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'The result was {result}')
        return result
    return intern


@create_func
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parameter must be a string.')


invertida = inverte_string('123')
print(invertida)