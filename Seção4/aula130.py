
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        # setter
        self.password = password

    @classmethod
    def create_wit_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG', msg)

def connection_log(msg):
    print('Log:', msg)



# c1 = Connection()
c1 = Connection.create_wit_auth('PedroHFDA', "SenhaTeste")
# c1.set_user('PedroHFDA')
# c1.set_password('SenhaTeste')
print(Connection.log('Essa é a mensagem de LOG'))
print(c1.user)
print(c1.password)