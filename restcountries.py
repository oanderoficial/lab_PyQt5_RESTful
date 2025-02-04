import sys
import requests
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox
import urllib3

URL_API = "https://restcountries.com/v3.1/all"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  #Ignorar avisos SSL

class AplicativoPaises(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicativo de Países")
        self.setGeometry(200, 200, 800, 600)

        # Layout e widgets
        layout = QVBoxLayout()
        self.input_busca = QLineEdit(placeholderText="Digite para buscar...")
        self.input_busca.textChanged.connect(self.atualizar_tabela)
        self.tabela = QTableWidget()

        layout.addWidget(self.input_busca)
        layout.addWidget(self.tabela)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Carregar dados
        self.dados_paises = self.carregar_dados()
        self.atualizar_tabela()

    def carregar_dados(self):
        try:
            resposta = requests.get(URL_API, timeout=10, verify=False)
            resposta.raise_for_status()
            return resposta.json()
        except requests.exceptions.RequestException as erro:
            QMessageBox.critical(self, "Erro na API", f"Não foi possível carregar os dados:\n{erro}")
            return []

    def atualizar_tabela(self):
        texto = self.input_busca.text().lower()
        dados_filtrados = [
            pais for pais in self.dados_paises
            if texto in pais.get("name", {}).get("common", "").lower()
        ]

        self.tabela.setRowCount(len(dados_filtrados))
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["Nome", "Capital", "Região", "População"])

        for linha, pais in enumerate(dados_filtrados):
            self.tabela.setItem(linha, 0, QTableWidgetItem(pais.get("name", {}).get("common", "N/A")))
            self.tabela.setItem(linha, 1, QTableWidgetItem(", ".join(pais.get("capital", ["N/A"]))))
            self.tabela.setItem(linha, 2, QTableWidgetItem(pais.get("region", "N/A")))
            self.tabela.setItem(linha, 3, QTableWidgetItem(str(pais.get("population", "N/A"))))

        self.tabela.resizeColumnsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AplicativoPaises()
    janela.show()
    sys.exit(app.exec_())
