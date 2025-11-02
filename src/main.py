import pyautogui
import keyboard 
import time

# Cria uma função que sera chamamado quando a função for chamado
def tarefa():
    print('Iniciando tarefa...')
#Associar essa essa função a uma combinação de teclas 
keyboard.add_hotkey('ctrl+shift+t', tarefa)

keyboard.wait('esc')  # Mantém o programa rodando até que 'esc' seja pressionado
print('Programa encerrado.')