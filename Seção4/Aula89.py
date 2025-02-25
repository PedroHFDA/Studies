# dir, hasattr e getattr em python

string = 'Pedro'
metodo = 'lower'

if hasattr(string, metodo):
    print(
         'Existe upper:\n'
         f'{getattr(string, metodo)()}'
          )

else:
    print(f'Não existe o metodo {metodo}')