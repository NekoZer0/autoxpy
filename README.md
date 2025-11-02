# Projeto de Automação com PyAutoGUI e Keyboard

Este projeto é um exemplo simples de **automação com teclado e interface gráfica (GUI)** em Python.  
Ele demonstra como criar **atalhos de teclado personalizados** e **executar tarefas automaticamente**.

O projeto foi inicializado com o comando `uv init` e o ficheiro principal está localizado em `srv/main.py`.


## 1. Pré-requisitos

Antes de começar, verifique se o **Python** está instalado e disponível no terminal.

```bash
python --version
```

> Recomendado: Python 3.8 ou superior  
> Certifique-se de marcar a opção **“Add Python to PATH”** durante a instalação.

## 2. Instalar o gerenciador de pacotes `uv`

O `uv` é um gerenciador moderno e rápido para dependências Python, que substitui ferramentas como `pip` e `poetry`.

 - **Instalação no Windows**
        - Baixe e execute o instalador autônomo do uv com o comando:
            `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
        - *Este comando faz o download e executa o script de instalação do uv diretamente no seu terminal.*

    - **Atualizar o uv**
        - Após a instalação, execute:
            `uv self update`
        - *Este comando garante que você está utilizando a versão mais recente do uv, prevenindo problemas de compatibilidade e trazendo melhorias de performance.*

## 3. Criar o projeto

Para iniciar um novo projeto, execute:

```bash
uv init nome-do-projeto
```

Estrutura inicial do projeto:
```
nome-do-projeto/
├─ srv/
│  └─ main.py
├─ uv.lock
├─ pyproject.toml
```

> Neste projeto, o arquivo principal (`main.py`) foi colocado dentro da pasta `srv`.

---

## 4. Instalar as dependências

As bibliotecas **`pyautogui`** e **`keyboard`** não vêm por padrão com o Python, por isso precisam ser instaladas.

```bash
uv add pyautogui keyboard
```

>  **Não adicione `time`** — é um módulo interno do Python e já vem instalado.

Se ocorrer timeout ou falha de rede, use:
```bash
uv add pyautogui keyboard --frozen
```

Ou instale com o `pip`:
```bash
python -m pip install pyautogui keyboard
```

## 5. Estrutura final do projeto

```
.
├─ srv/
│  └─ main.py
├─ pyproject.toml
└─ README.md
```

## 6. Código principal (`srv/main.py`)

```python
import pyautogui
import keyboard 
import time

# Cria uma função que será chamada quando a combinação de teclas for pressionada
def tarefa():
    print('Iniciando tarefa...')

# Associa a função à combinação de teclas Ctrl + Shift + T
keyboard.add_hotkey('ctrl+shift+t', tarefa)

# Mantém o programa em execução até que a tecla Esc seja pressionada
keyboard.wait('esc')

print('Programa encerrado.')
```
##  7. Executar o projeto

Para rodar o programa:

```bash
python srv/main.py
```

Durante a execução:
- Pressione **Ctrl + Shift + T** → imprime “Iniciando tarefa...”
- Pressione **Esc** → encerra o programa com a mensagem “Programa encerrado.”

## 8. Melhoria sugerida (com tratamento de exceções)

```python
import keyboard

def tarefa():
    print('Iniciando tarefa...')

try:
    keyboard.add_hotkey('ctrl+shift+t', tarefa)
    keyboard.wait('esc')
finally:
    print('Programa encerrado.')
```

Isso garante que o programa finalize corretamente mesmo em caso de erro.

## 9. Personalizando a automação

Podes substituir o conteúdo da função `tarefa()` por qualquer ação, por exemplo:

```python
def tarefa():
    pyautogui.alert('A automação foi iniciada!')
    pyautogui.moveTo(500, 300, duration=1)
    pyautogui.click()
    print('Tarefa executada com sucesso!')
```

## 10. Licença

Este projeto é de uso livre para fins educativos e demonstração.  
Sinta-se à vontade para adaptar, melhorar e publicar as suas próprias automações!

**Autor:** José de Almeida  
**Empresa/Organização:** UNIK UK – COMÉRCIO E SERVIÇOS, LDA  
**Tecnologias:** Python, PyAutoGUI, Keyboard, UV  
**Sistema Operativo:** Windows 10/11 ou Linux

