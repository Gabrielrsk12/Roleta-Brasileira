import random
import time

def pausa(valor):
    return time.sleep(valor)
def status(points):
    print(f"Seus pontos: {points}")
def main():
    points = 0
    is_running = True
    values = ("vermelho","preto")
    while is_running:
        print("Escolha entre (VERMELHO | PRETO) / press (q) to quit")

        cor = input("> ").lower()

        num = random.randint(1,100)
        pausa(1)
        if cor == "q":
            print("Saindo do jogo...")
            is_running = False

        if not cor in values:
            print("ENTRADA INVÁLIDA!!!")
            continue

        elif (num % 2 == 0 and cor == "vermelho") or (num % 2 != 0 and cor == "preto"):
            points += 1
            print(f"O numero era: {num}")
            print("YOU WIN!!!")
            status()
        
        else:
            print("YOU LOSE, FATALITY!!!")

        
            
if __name__ == "__main__":
    main()

        
  
