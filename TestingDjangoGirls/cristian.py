import random

def sayHello():
    participantes = ['Alison', 'Edith',
                    'Fabian', 'Carlos', 
                    'Marisabel', 'Diana',
                    'Veronica', 'Tatiana']
    print("Hola ", random.choice(participantes))


def main():
    print("Hola soy Cristian :D")
    sayHello()    


if __name__ == "__main__":
    main()
