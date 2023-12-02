import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, \
    QScrollArea, QMessageBox
import sqlite3

class CrudApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('CRUD App')
        self.setGeometry(300, 300, 300, 300)

        # Widgets
        self.name_label = QLabel('Nome:')
        self.name_entry = QLineEdit()

        self.dob_label = QLabel('Data de Nascimento:')
        self.dob_entry = QLineEdit()

        self.phone_label = QLabel('Telefone:')
        self.phone_entry = QLineEdit()

        self.cpf_label = QLabel('CPF:')
        self.cpf_entry = QLineEdit()

        self.rg_label = QLabel('RG:')
        self.rg_entry = QLineEdit()

        self.nacionalidade_label = QLabel('Nacionalidade:')
        self.nacionalidade_entry = QLineEdit()

        self.naturalidade_label = QLabel('Naturalidade:')
        self.naturalidade_entry = QLineEdit()

        self.estado_civil_label = QLabel('Estado Civil:')
        self.estado_civil_entry = QLineEdit()

        self.profissao_label = QLabel('Profissão:')
        self.profissao_entry = QLineEdit()

        self.filiacao1_label = QLabel('Filiação 1:')
        self.filiacao1_entry = QLineEdit()

        self.filiacao2_label = QLabel('Filiação 2:')
        self.filiacao2_entry = QLineEdit()

        self.residencia_label = QLabel('Residência:')
        self.residencia_entry = QLineEdit()

        self.endereco_label = QLabel('Endereço:')
        self.endereco_entry = QLineEdit()

        self.rua_label = QLabel('Rua:')
        self.rua_entry = QLineEdit()

        self.numero_label = QLabel('Número:')
        self.numero_entry = QLineEdit()

        self.cep_label = QLabel('CEP:')
        self.cep_entry = QLineEdit()

        self.bairro_label = QLabel('Bairro:')
        self.bairro_entry = QLineEdit()

        self.email_label = QLabel('Email:')
        self.email_entry = QLineEdit()

        self.categoria_label = QLabel('Categoria Pretendida:')
        self.categoria_entry = QLineEdit()

        self.valores_label = QLabel('Valores:')
        self.valores_entry = QLineEdit()

        self.forma_pagamento_label = QLabel('Forma de Pagamento:')
        self.forma_pagamento_entry = QLineEdit()

        self.observacao_label = QLabel('Observação:')
        self.observacao_entry = QLineEdit()

        self.add_button = QPushButton('Adicionar')
        self.show_button = QPushButton('Mostrar Dados')

        # Widget para exibir dados
        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)

        # Adicionando a barra de rolagem
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.data_display)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)

        layout.addWidget(self.dob_label)
        layout.addWidget(self.dob_entry)

        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)

        layout.addWidget(self.cpf_label)
        layout.addWidget(self.cpf_entry)

        layout.addWidget(self.rg_label)
        layout.addWidget(self.rg_entry)

        layout.addWidget(self.nacionalidade_label)
        layout.addWidget(self.nacionalidade_entry)

        layout.addWidget(self.naturalidade_label)
        layout.addWidget(self.naturalidade_entry)

        layout.addWidget(self.estado_civil_label)
        layout.addWidget(self.estado_civil_entry)

        layout.addWidget(self.profissao_label)
        layout.addWidget(self.profissao_entry)

        layout.addWidget(self.filiacao1_label)
        layout.addWidget(self.filiacao1_entry)

        layout.addWidget(self.filiacao2_label)
        layout.addWidget(self.filiacao2_entry)

        layout.addWidget(self.residencia_label)
        layout.addWidget(self.residencia_entry)

        layout.addWidget(self.endereco_label)
        layout.addWidget(self.endereco_entry)

        layout.addWidget(self.rua_label)
        layout.addWidget(self.rua_entry)

        layout.addWidget(self.numero_label)
        layout.addWidget(self.numero_entry)

        layout.addWidget(self.cep_label)
        layout.addWidget(self.cep_entry)

        layout.addWidget(self.bairro_label)
        layout.addWidget(self.bairro_entry)

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)

        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_entry)

        layout.addWidget(self.valores_label)
        layout.addWidget(self.valores_entry)

        layout.addWidget(self.forma_pagamento_label)
        layout.addWidget(self.forma_pagamento_entry)

        layout.addWidget(self.observacao_label)
        layout.addWidget(self.observacao_entry)

        layout.addWidget(self.add_button)
        layout.addWidget(self.show_button)
        layout.addWidget(scroll_area)  # Adicionando a barra de rolagem

        self.setLayout(layout)

        self.setStyleSheet('''
            QWidget {
                font-size: 14px;
            }

            QLineEdit {
                padding: 5px;
                margin: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }

            QPushButton {
                padding: 5px 10px;
                margin: 5px;
                border: 1px solid #007BFF;
                border-radius: 3px;
                background-color: #007BFF;
                color: white;
            }

            QTextEdit {
                padding: 5px;
                margin: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
                font-family: Courier, monospace;
            }
        ''')

        # Conectar sinais aos slots
        self.add_button.clicked.connect(self.add_data)
        self.show_button.clicked.connect(self.show_data)

        # Banco de dados
        self.conn = sqlite3.connect('dados.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                data_nascimento TEXT,
                telefone TEXT,
                cpf TEXT,
                rg TEXT,
                nacionalidade TEXT,
                naturalidade TEXT,
                estado_civil TEXT,
                profissao TEXT,
                filiacao1 TEXT,
                filiacao2 TEXT,
                residencia TEXT,
                endereco TEXT,
                rua TEXT,
                numero TEXT,
                cep TEXT,
                bairro TEXT,
                email TEXT,
                categoria_pretendida TEXT,
                valores TEXT,
                forma_pagamento TEXT,
                observacao TEXT
            )
        ''')
        self.conn.commit()

    def add_data(self):
        nome = self.name_entry.text()
        data_nascimento = self.dob_entry.text()
        telefone = self.phone_entry.text()
        cpf = self.cpf_entry.text()
        rg = self.rg_entry.text()
        nacionalidade = self.nacionalidade_entry.text()
        naturalidade = self.naturalidade_entry.text()
        estado_civil = self.estado_civil_entry.text()
        profissao = self.profissao_entry.text()
        filiacao1 = self.filiacao1_entry.text()
        filiacao2 = self.filiacao2_entry.text()
        residencia = self.residencia_entry.text()
        endereco = self.endereco_entry.text()
        rua = self.rua_entry.text()
        numero = self.numero_entry.text()
        cep = self.cep_entry.text()
        bairro = self.bairro_entry.text()
        email = self.email_entry.text()
        categoria_pretendida = self.categoria_entry.text()
        valores = self.valores_entry.text()
        forma_pagamento = self.forma_pagamento_entry.text()
        observacao = self.observacao_entry.text()

        if nome and data_nascimento and telefone and cpf and rg and nacionalidade and naturalidade \
                and estado_civil and profissao and filiacao1 and filiacao2 and residencia and endereco \
                and rua and numero and cep and bairro and email and categoria_pretendida and valores \
                and forma_pagamento and observacao:
            self.cursor.execute('''
                INSERT INTO dados (nome, data_nascimento, telefone, cpf, rg, nacionalidade, naturalidade,
                estado_civil, profissao, filiacao1, filiacao2, residencia, endereco, rua, numero, cep, bairro,
                email, categoria_pretendida, valores, forma_pagamento, observacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, data_nascimento, telefone, cpf, rg, nacionalidade, naturalidade, estado_civil, profissao,
                  filiacao1, filiacao2, residencia, endereco, rua, numero, cep, bairro, email, categoria_pretendida,
                  valores, forma_pagamento, observacao))

            self.conn.commit()
            QMessageBox.information(self, 'Sucesso', 'Dados adicionados com sucesso!')
            self.clear_entries()
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha todos os campos obrigatórios.')

    def show_data(self):
        self.cursor.execute('SELECT * FROM dados')
        data = self.cursor.fetchall()

        if data:
            data_str = ""
            for row in data:
                data_str += f"Nome: {row[1]}\n"
                data_str += f"Data de Nascimento: {row[2]}\n"
                data_str += f"Telefone: {row[3]}\n"
                data_str += f"CPF: {row[4]}\n"
                data_str += f"RG: {row[5]}\n"
                data_str += f"Nacionalidade: {row[6]}\n"
                data_str += f"Naturalidade: {row[7]}\n"
                data_str += f"Estado Civil: {row[8]}\n"
                data_str += f"Profissão: {row[9]}\n"
                data_str += f"Filiação 1: {row[10]}\n"
                data_str += f"Filiação 2: {row[11]}\n"
                data_str += f"Residência: {row[12]}\n"
                data_str += f"Endereço: {row[13]}\n"
                data_str += f"Rua: {row[14]}\n"
                data_str += f"Número: {row[15]}\n"
                data_str += f"CEP: {row[16]}\n"
                data_str += f"Bairro: {row[17]}\n"
                data_str += f"Email: {row[18]}\n"
                data_str += f"Categoria Pretendida: {row[19]}\n"
                data_str += f"Valores: {row[20]}\n"
                data_str += f"Forma de Pagamento: {row[21]}\n"
                data_str += f"Observação: {row[22]}\n\n"

            self.data_display.setPlainText(data_str)
        else:
            self.data_display.setPlainText('Nenhum dado encontrado.')

    def clear_entries(self):
        self.name_entry.clear()
        self.dob_entry.clear()
        self.phone_entry.clear()
        self.cpf_entry.clear()
        self.rg_entry.clear()
        self.nacionalidade_entry.clear()
        self.naturalidade_entry.clear()
        self.estado_civil_entry.clear()
        self.profissao_entry.clear()
        self.filiacao1_entry.clear()
        self.filiacao2_entry.clear()
        self.residencia_entry.clear()
        self.endereco_entry.clear()
        self.rua_entry.clear()
        self.numero_entry.clear()
        self.cep_entry.clear()
        self.bairro_entry.clear()
        self.email_entry.clear()
        self.categoria_entry.clear()
        self.valores_entry.clear()
        self.forma_pagamento_entry.clear()
        self.observacao_entry.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CrudApp()
    window.show()
    sys.exit(app.exec_())
