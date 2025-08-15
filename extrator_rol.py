import pandas as pd
import pdfplumber
import zipfile
import os
from datetime import datetime

def extrair_tabelas_pdf(pdf_path):
    """Extrai tabelas de PDF usando pdfplumber (sem dependência de Java)"""
    print(f"Processando arquivo PDF: {pdf_path}")
    
    todas_tabelas = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            tabelas = page.extract_tables()
            for tabela in tabelas:
                if tabela: 
                    df = pd.DataFrame(tabela[1:], columns=tabela[0])
                    todas_tabelas.append(df)
            
            print(f"Página {i+1} processada - {len(tabelas)} tabelas encontradas")
    
    if not todas_tabelas:
        raise ValueError("Nenhuma tabela encontrada no PDF")
    
    return pd.concat(todas_tabelas, ignore_index=True)

def transformar_dados(df):
    """Realiza as transformações necessárias nos dados"""
    print("Aplicando transformações nos dados...")
    
    # Substitui as abreviações 
    df = df.applymap(lambda x: "Seg. Odontológica" if str(x).strip() == "OD" else x)
    df = df.applymap(lambda x: "Seg. Ambulatorial" if str(x).strip() == "AMB" else x)
    df = df.dropna(how='all')
    df = df.reset_index(drop=True)
    
    return df

def salvar_zip(df, output_zip):
    raiz = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = output_zip.replace("{raiz}", raiz)
    csv_filename = "Rol_Procedimentos_ANS.csv"
    
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"CSV temporário gerado: {csv_filename}")
    
    # Cria arquivo ZIP
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))
    os.remove(csv_filename)
    
    print(f"Arquivo ZIP criado: {zip_filename}")
    return zip_filename

def main():
    PDF_PATH = "anexo1.pdf"
    OUTPUT_ZIP = "Teste_{Márcio}.zip"
    
    try:
        df = extrair_tabelas_pdf(PDF_PATH)   
        df_transformado = transformar_dados(df)       
        arquivo_zip = salvar_zip(df_transformado, OUTPUT_ZIP)
        
        print("\nProcesso concluído com sucesso!")
        print(f"Arquivo final: {os.path.abspath(arquivo_zip)}")
        print(df_transformado.head())
        
    except Exception as e:
        print(f"\nErro durante o processamento: {str(e)}")

if __name__ == "__main__":
    # Instale as dependências necessárias (se ainda não tiver)
    try:
        import pdfplumber
        import pandas
    except ImportError:
        print("Instalando dependências necessárias...")
        os.system("pip install pdfplumber pandas")
    
    main()