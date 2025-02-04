
# LAB - PyQt5 Restful
<p> Desenvolvendo um app que vai consumir os dados da API REST Countries e organizar esses dados. </p>

# API 

```python
URL_API = "https://restcountries.com/v3.1/all"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  #Ignorar avisos SSL
```

<strong> Link: </strong> https://restcountries.com
</br>
<strong> Repositório: </strong> https://github.com/apilayer/restcountries


# Componentes do PyQt5 necessários para o Projeto:

Abaixo estão descritos os principais componentes utilizados no PyQt5 mencionados no código:

## `QApplication`
- Representa o aplicativo em si.
- É a base de qualquer programa PyQt5 e gerencia recursos, eventos e a execução principal do aplicativo.
- Todo programa PyQt5 precisa de uma instância única de `QApplication`.

### Exemplo de Uso:
```python
app = QApplication(sys.argv)
app.exec_()
```

---

## `QMainWindow`
- Representa a janela principal de um aplicativo PyQt5.
- Oferece uma estrutura predefinida para adicionar menus, barras de ferramentas, barras de status e widgets centrais.
- Frequentemente usada como a base para a interface principal do programa.

### Exemplo de Uso:
```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Principal")
```

---

## `QWidget`
- É o bloco básico de construção para criar elementos da interface gráfica.
- Pode ser usado diretamente como uma janela simples ou como um contêiner para outros widgets.

### Exemplo de Uso:
```python
widget = QWidget()
widget.setWindowTitle("Meu Widget")
```

---

## `QVBoxLayout`
- Um gerenciador de layout que organiza widgets em uma coluna vertical.
- Garante que os widgets sejam redimensionados e reposicionados adequadamente quando a janela é ajustada.

### Exemplo de Uso:
```python
layout = QVBoxLayout()
layout.addWidget(QLineEdit())
layout.addWidget(QTableWidget())
```

---

## `QTableWidget`
- Um widget para exibir e manipular tabelas (linhas e colunas).
- Permite adicionar itens em células, ajustar a aparência e interagir com os dados.

### Exemplo de Uso:
```python
table = QTableWidget(5, 3)  # 5 linhas e 3 colunas
table.setItem(0, 0, QTableWidgetItem("Dado 1"))
```

---

## `QTableWidgetItem`
- Representa um item em uma célula de um `QTableWidget`.
- Pode conter texto, imagens, ou outros tipos de dados.

### Exemplo de Uso:
```python
item = QTableWidgetItem("Texto na célula")
table.setItem(0, 0, item)
```

---

## `QLineEdit`
- Um campo de entrada de texto de linha única.
- Usado para permitir que os usuários insiram texto no aplicativo.

### Exemplo de Uso:
```python
line_edit = QLineEdit()
line_edit.setPlaceholderText("Digite algo aqui")
```

---

## `QMessageBox`
- Um widget usado para exibir mensagens ao usuário, como notificações, alertas ou caixas de diálogo para confirmação.

### Exemplo de Uso:
```python
QMessageBox.information(None, "Título", "Mensagem exibida ao usuário")
```

---
