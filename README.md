# kanban-python-qtdesigner

## Projeto feito com Qt para Python - pyside6 e Qt Designer.

#### Observação:

Ambiente usado: linux - Ubuntu 22.04.3;

#### Primeiros passos - preparando o ambiente (linux).

- Preparando e criando ambiente virtual

Visual Studio Code -> Terminal -> New Terminal

$ sudo apt install python3.10-venv
$ python3 -m venv env
$ source env/bin/activate

Saída: (env) nome_uario@nome_do_pc:~... 

Nota-se na saída acima que o nome "env" no inicio do terminal, isso significa que o ambiente virtual venv foi criado, assim todos os comandos seram realizados dentro desta virtualização, garantindo que o ambiente externo não seja afetado/modificado.

- Instalando Pyside6

$ pip install pyside6

- Testando sua instalação

Crie um novo arquivo com o nome teste.py

Digite o código abaixo no arquivo e em seguida execute-o

import PySide6.QtCore

print(PySide6.__version__)

Saída: /teste.py"
6.6.1

- Abrindo o Qt Designer

Percorra o caminho do diretorio -> pasta_do_projeto -> env -> lib -> python3.10 -> site-packages -> PySide6 -> designer

#### Estrutura de pastas e arquivos no Visual Studio Code

Dentro da pasta do projeto crie um arquivo chamado main.py
### Outras informações 

- Verfificar versão do Python

$ python3 --version

saída: Python 3.10.12



### Bibliográfia

- https://doc-qt-io.translate.goog/qtforpython-6/quickstart.html?_x_tr_sl=en&_x_tr_tl=pt-PT&_x_tr_hl=pt-PT&_x_tr_pto=tc

- https://www.pythonguis.com/installation/install-qt-designer-standalone/