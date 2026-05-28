📄 PDF Table Extractor + Data Pipeline (ANS)

Projeto em Python para extração automática de tabelas de arquivos PDF, transformação de dados com pandas e exportação final em arquivo .zip.

📌 Sobre

Este projeto lê um arquivo PDF contendo tabelas, extrai os dados automaticamente, realiza limpeza e padronização e gera um arquivo final em CSV compactado em ZIP.

🧰 Tecnologias
Python 3.x
pandas
pdfplumber
zipfile (nativo)
os (nativo)
datetime (nativo)
⚙️ Fluxo do Processo
Leitura do PDF
Extração de tabelas por página
Conversão para DataFrame (pandas)
Transformação e limpeza dos dados
Geração de CSV temporário
Compactação em ZIP
Remoção do CSV
🚀 Instalação
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
pip install pandas pdfplumber
▶️ Como Executar

Coloque o arquivo PDF na raiz do projeto:

anexo1.pdf

Execute o script:

python main.py
📥 Entrada e Saída
Entrada
anexo1.pdf
Saída
Teste_{timestamp}.zip

Conteúdo do ZIP:

Rol_Procedimentos_ANS.csv
🔧 Transformações Aplicadas
OD → Seg. Odontológica
AMB → Seg. Ambulatorial
Remoção de linhas vazias
Reset do índice
Junção de tabelas de múltiplas páginas
🗂 Estrutura do Projeto
.
├── main.py
├── anexo1.pdf
└── README.md
✨ Funcionalidades
Extração de tabelas de PDF sem Java
Processamento de múltiplas páginas
Limpeza automática dos dados
Exportação para CSV
Compactação em ZIP com timestamp
