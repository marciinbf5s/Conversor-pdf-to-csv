# 📄 PDF Table Extractor + Data Pipeline (ANS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/PDFPlumber-PDF%20Extraction-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CSV-Export-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ZIP-Compression-orange?style=for-the-badge" />
</p>

<p align="center">
  Pipeline automatizado para extração, transformação e exportação de tabelas de arquivos PDF da ANS.
</p>

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido em **Python** para automatizar a extração de tabelas contidas em arquivos PDF da **ANS (Agência Nacional de Saúde Suplementar)**.

O sistema realiza:

- 📥 Leitura automática do PDF
- 📊 Extração de tabelas em múltiplas páginas
- 🧹 Limpeza e padronização dos dados
- 🗃 Conversão para CSV
- 📦 Compactação automática em `.zip`

Tudo isso sem necessidade de Java ou ferramentas externas complexas.

---

# 🧰 Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="18"/> **Python 3.x** | Linguagem principal |
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="18"/> **Pandas** | Manipulação e transformação dos dados |
| 📄 **pdfplumber** | Extração de tabelas do PDF |
| 🗜 **zipfile** | Compactação do arquivo final |
| 📁 **os** | Manipulação de arquivos |
| ⏰ **datetime** | Geração de timestamp |

---

# ⚙️ Fluxo do Processo

```mermaid
flowchart TD
    A[📄 Leitura do PDF] --> B[📊 Extração das tabelas]
    B --> C[🧹 Limpeza e transformação]
    C --> D[📁 Conversão para CSV]
    D --> E[📦 Compactação ZIP]
    E --> F[🗑 Remoção do CSV temporário]
