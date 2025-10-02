import os

def renomear_questoes_simples():
    pasta = "questoes-paginas-29a31"
    
    if not os.path.exists(pasta):
        print(f"Pasta {pasta} não encontrada!")
        return
    
    # Mapeamento direto dos nomes antigos para os novos
    mapeamento = {}
        
    # Questões normais: parte_002 a parte_032 -> questao-46 a questao-76
    for i in range(1, 12):
        antigo = f"parte_{i:03d}.png"
        novo = f"questao-{i+78}.png"
        mapeamento[antigo] = novo
    
    # Aplicar o renomeamento
    for antigo, novo in mapeamento.items():
        caminho_antigo = os.path.join(pasta, antigo)
        caminho_novo = os.path.join(pasta, novo)
        
        if os.path.exists(caminho_antigo):
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {antigo} -> {novo}")
        else:
            print(f"Arquivo não encontrado: {antigo}")
    
    print("Renomeação concluída!")

# Executar
if __name__ == "__main__":
    renomear_questoes_simples()