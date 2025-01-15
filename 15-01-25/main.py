# Try - Except
import time
from xml.sax.handler import property_interning_dict

'''
try:
    f = open("demo.txt")
    try:
        f.write("Corso Python")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong!")


try:
    while True:
        numb1 = int(input("Inserisci il primo nr.: "))
        numb2 = int(input("Inserisci il secondo nr.: "))
        print(numb1 / numb2)
except ValueError:
    print("Inserisci un intero")
except ZeroDivisionError:
    print("Errore divisione per 0")
finally:
    print("Programma terminato.")


try:
    while True:
        user_input = input("Type some test text (command + c): ")
        print(f"You entered: {user_input}")
except KeyboardInterrupt:
    print("\nProgramma interrotto dall'utente")


def long_running_process():
    try:
        print("Performing a long-process. Press (command + c) to interrupt.")
        for i in range(1000):
            time.sleep(1)
            print(f"Processing step {i + 1}")

    except KeyboardInterrupt:
        print(f"\n Interrupted! Cleaning up before exiting.")
    finally:
        print("Exiting the program.")

long_running_process()
'''










