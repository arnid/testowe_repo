#def decorator(f):
#    def wrap(a, b):             # robimy dokładnie to samo, definiujemy funkcję zwracająca zwykła wartość.
#        print('we wrapperze')
#        return f(a, b)
#    return wrap                 # dekorator zwraca funkcję o tej samej sygnaturze jak tą, którą dekorujemy.
#
#@decorator
#def foo(a, b):
#    return a +b
#
#print(foo(1, 2))                # Nie wołamy funkcji `foo` tak naprawdę, tylko wrap z argumentami.
#                                # Wrap natomiast woła w środku funkcje dekorowaną (foo)

def wrapper(f):
    def dddf(argument):
        def gg(aa, dd):
            print("no i co")
            print(f)
            return argument(aa, dd + '!!!!!!!!!!')
        return gg
    return dddf


class TestClass():
    def __init__(self):
        print("Konstruktor")

    @wrapper('argument_dekoratora')
    def costam(self, argument):
        print("ostateczna")
        print(argument)


if __name__ == '__main__':
    nnn = TestClass()
    nnn.costam('Nie dziala nie wiadomo dlaczego')





