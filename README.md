📄 PDF Table Extractor + Data Pipeline (ANS)

Projeto em Python para extração automatizada de tabelas de arquivos PDF, tratamento de dados com pandas e geração de arquivo final compactado em .zip.

📌 Sumário
Sobre
Tecnologias
Arquitetura do Processo
Instalação
Como Executar
Entrada e Saída
Transformações Aplicadas
Estrutura do Projeto
Melhorias Futuras
Licença
📖 Sobre

Este projeto realiza a leitura de um arquivo PDF contendo tabelas estruturadas, extrai os dados automaticamente, aplica transformações de limpeza e padronização e gera um arquivo final em CSV compactado em ZIP.

O objetivo principal é automatizar o processamento de dados tabulares presentes em documentos PDF.

🧰 Tecnologias
Python 3.x
pandas
pdfplumber
zipfile (built-in)
os (built-in)
datetime (built-in)
⚙️ Arquitetura do Processo

O pipeline segue as etapas abaixo:

📥 Leitura do PDF (pdfplumber)
📊 Extração de tabelas por página
🧹 Transformação e limpeza dos dados (pandas)
📄 Geração de CSV temporário
🗜️ Compactação em arquivo ZIP
🗑️ Remoção do CSV temporário
🚀 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências:

pip install pandas pdfplumber
▶️ Como Executar

Coloque o arquivo PDF na raiz do projeto com o nome:

anexo1.pdf

Execute o script:

python main.py
📥 Entrada e Saída
Entrada
Arquivo: anexo1.pdf
Formato: PDF contendo tabelas estruturadas
Saída
Arquivo final:
Teste_{timestamp}.zip
Conteúdo do ZIP:
Rol_Procedimentos_ANS.csv
🔧 Transformações Aplicadas

Durante o processamento, os dados passam por:

Substituição de valores:
OD → "Seg. Odontológica"
AMB → "Seg. Ambulatorial"
Remoção de linhas completamente vazias
Reset do índice do DataFrame
Concatenação de tabelas de múltiplas páginas
🗂 Estrutura do Projeto
.
├── main.py
├── anexo1.pdf
├── requirements.txt (opcional)
└── README.md
📌 Funcionalidades
✔️ Extração de tabelas de PDF sem Java
✔️ Processamento multi-página
✔️ Transformação e limpeza de dados
✔️ Exportação para CSV
✔️ Compactação automática em ZIP
✔️ Nome de arquivo com timestamp dinâmico
🚧 Melhorias Futuras
 Suporte a múltiplos PDFs
 Logs estruturados (logging module)
 Interface CLI (argparse)
 Exportação para banco de dados
 Validação de schema das tabelas
 Dockerização do pipeline
