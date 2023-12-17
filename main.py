# Importando os modúlos PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import sys

# Funções

def abrir_janela_nova_tarefa():
    janela_nova_tarefa.show()



# Instanciamento

app = QApplication(sys.argv)

loader = QUiLoader()

# Carregando arquivos de interface Qt Designer .ui

kanban_app = loader.load("ui_main.ui")
janela_nova_tarefa = loader.load("ui_nova_tarefa.ui")

# Comandos

kanban_app.btn_a_fazer.clicked.connect(abrir_janela_nova_tarefa)

# Setando título
'''
titulo_main_window = "Kanban Board System"
kanban_app.setWindowTitle(titulo_main_window)
titulo_add_nova_tarefa = "Nova Tarefa"
add_nova_tarefa.setWindowTitle(titulo_add_nova_tarefa)
'''
# Outra maneira de setar título
kanban_app.setWindowTitle("Kanban Board System")
janela_nova_tarefa.setWindowTitle("Nova Tarefa")

# Chamando janelas para execução
kanban_app.show()

sys.exit(app.exec())