from pathlib import Path
import shutil

# Caminho da pasta raiz onde a exclusão será feita
pasta_raiz = Path(r'C:\Users\Jallar\Documents\automação\teste\teste - Copia')

# Nome da pasta que NÃO será excluída
nome_pasta_excluida = 'obsoleto'

# Verificar se o caminho existe
if not pasta_raiz.exists():
    print(f"Erro: O caminho {pasta_raiz} não existe.")
else:
    # Função para verificar se uma pasta é "obsoleto" (ignora maiúsculas/minúsculas)
    def e_pasta_excluida(pasta):
        return pasta.name.lower() == nome_pasta_excluida.lower()
    
    # Apagar arquivos que não estão em pastas "obsoleto"
    for arquivo in pasta_raiz.rglob('*'):
        if arquivo.is_file() and not any(e_pasta_excluida(pasta) for pasta in arquivo.parents):
            try:
                arquivo.unlink()
                print(f"Arquivo {arquivo} apagado com sucesso!")
            except FileNotFoundError:
                print(f"Erro: O arquivo {arquivo} não foi encontrado.")
            except PermissionError:
                print(f"Erro: Sem permissão para apagar {arquivo}.")
            except Exception as e:
                print(f"Erro ao tentar apagar {arquivo}: {e}")

    # Apagar pastas que não são "obsoleto"
    for pasta in sorted(pasta_raiz.rglob('*'), key=lambda p: len(p.parts), reverse=True):
        if pasta.is_dir() and not e_pasta_excluida(pasta):
            try:
                shutil.rmtree(pasta)  # Remove a pasta e todos os conteúdos
                print(f"Pasta {pasta} apagada com sucesso!")
            except PermissionError:
                print(f"Erro: Sem permissão para apagar a pasta {pasta}.")
            except Exception as e:
                print(f"Erro ao tentar apagar a pasta {pasta}: {e}")
        elif pasta.is_dir():
            print(f"Pasta '{pasta}' não foi apagada porque é ou contém uma pasta 'obsoleto'.")
