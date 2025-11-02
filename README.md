# 🧠 Projeto de Automação com PyAutoGUI e Keyboard

Este projeto é um exemplo simples de **automação com teclado e interface gráfica (GUI)** em Python.  
Ele demonstra como criar **atalhos de teclado personalizados** e **executar tarefas automaticamente**.

O projeto foi inicializado com o comando `uv init` e o ficheiro principal está localizado em `srv/main.py`.

---

## ⚙️ 1. Pré-requisitos

Antes de começar, verifique se o **Python** está instalado e disponível no terminal.

```bash
python --version
```

> ✅ Recomendado: Python 3.8 ou superior  
> ⚠️ Certifique-se de marcar a opção **“Add Python to PATH”** durante a instalação.

---

## 📦 2. Instalar o gerenciador de pacotes `uv`

O `uv` é um gerenciador moderno e rápido para dependências Python, que substitui ferramentas como `pip` e `poetry`.

### Instalação via `pip`
```bash
python -m pip install --user uv
```

### (Opcional) Instalação isolada via `pipx`
```bash
python -m pip install --user pipx
python -m pipx ensurepath
pipx install uv
```

---

## 🏗️ 3. Criar o projeto

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

## 📥 4. Instalar as dependências

As bibliotecas **`pyautogui`** e **`keyboard`** não vêm por padrão com o Python, por isso precisam ser instaladas.

```bash
uv add pyautogui keyboard
```

> ⚠️ **Não adicione `time`** — é um módulo interno do Python e já vem instalado.

Se ocorrer timeout ou falha de rede, use:
```bash
uv add pyautogui keyboard --frozen
```

Ou instale com o `pip`:
```bash
python -m pip install pyautogui keyboard
```

---

## 🧩 5. Estrutura final do projeto

```
.
├─ srv/
│  └─ main.py
├─ pyproject.toml
└─ README.md
```

---

## 💻 6. Código principal (`srv/main.py`)

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

---

## 🧠 7. Explicação passo a passo do código

| Linha | Descrição |
|-------|------------|
| `import pyautogui` | Biblioteca usada para automação da interface gráfica (clicar, escrever, mover o rato, etc.). |
| `import keyboard` | Biblioteca para capturar e reagir a eventos do teclado. |
| `import time` | Módulo nativo do Python para manipulação de tempo (ex: `sleep`, `time`). |
| `def tarefa():` | Define uma função chamada `tarefa`, que executa ações quando chamada. |
| `keyboard.add_hotkey('ctrl+shift+t', tarefa)` | Cria um atalho de teclado (hotkey). Ao pressionar `Ctrl + Shift + T`, a função `tarefa` é executada. |
| `keyboard.wait('esc')` | Mantém o programa em execução até que o utilizador pressione `Esc`. |
| `print('Programa encerrado.')` | Exibe mensagem quando o programa termina. |

---

## ▶️ 8. Executar o projeto

Para rodar o programa:

```bash
python srv/main.py
```

Durante a execução:
- Pressione **Ctrl + Shift + T** → imprime “Iniciando tarefa...”
- Pressione **Esc** → encerra o programa com a mensagem “Programa encerrado.”

---

## 🔍 9. Melhoria sugerida (com tratamento de exceções)

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

---

## 💡 10. Possíveis problemas

| Problema | Causa | Solução |
|-----------|--------|----------|
| `operation timed out` | Conexão lenta ou bloqueada com o PyPI | Tente novamente com `--timeout 120` ou use `pip install` |
| `No solution found when resolving dependencies` | Tentativa de instalar o módulo interno `time` | Remova `time` da lista de dependências |
| `keyboard` não responde | Falta de permissões no Windows | Execute o terminal como **Administrador** |
| `pyautogui` não funciona (Linux) | Falta de dependências do sistema | Instale utilitários como `scrot`, `xclip` |

---

## 🚀 11. Personalizando a automação

Podes substituir o conteúdo da função `tarefa()` por qualquer ação, por exemplo:

```python
def tarefa():
    pyautogui.alert('A automação foi iniciada!')
    pyautogui.moveTo(500, 300, duration=1)
    pyautogui.click()
    print('Tarefa executada com sucesso!')
```

---

## 🧾 12. Licença

Este projeto é de uso livre para fins educativos e demonstração.  
Sinta-se à vontade para adaptar, melhorar e publicar as suas próprias automações!

---

**Autor:** José de Almeida  
**Empresa/Organização:** UNIK UK – COMÉRCIO E SERVIÇOS, LDA  
**Tecnologias:** Python, PyAutoGUI, Keyboard, UV  
**Sistema Operativo:** Windows 10/11 ou Linux

---
