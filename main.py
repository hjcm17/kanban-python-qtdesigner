# Importando os modúlos PySide6
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import sys

# Funções

def a_fazer():
    pass












# Instanciamento

app = QApplication(sys.argv)

loader = QUiLoader()

# Carregando arquivos de interface Qt Designer .ui

kanban_app = loader.load("ui_main.ui")
add_nova_tarefa = loader.load("ui_add_nova_tarefa.ui")

# Comandos

# Setando título
'''
titulo_main_window = "Kanban Board System"
kanban_app.setWindowTitle(titulo_main_window)
titulo_add_nova_tarefa = "Nova Tarefa"
add_nova_tarefa.setWindowTitle(titulo_add_nova_tarefa)
'''
# Outra maneira de setar título
kanban_app.setWindowTitle("Kanban Board System")
add_nova_tarefa.setWindowTitle("Nova Tarefa")

# Chamando janelas para execução
kanban_app.show()

sys.exit(app.exec())