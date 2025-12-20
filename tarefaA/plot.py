import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- Configurações Visuais ---
sns.set_theme(style="whitegrid")

def carregar_dados():
    INPUT_FILE = "results/experimentos.csv"
    if not os.path.exists(INPUT_FILE):
        print(f"Erro: {INPUT_FILE} não encontrado. Rode 'make run' antes.")
        exit(1)
    return pd.read_csv(INPUT_FILE)

# --- Gráfico 1: Variante 1 (Static) - Agrupado por K ---
# (O gráfico que fizemos anteriormente: 3 gráficos lado a lado)
def plotar_variante1_static(df):
    print("Gerando gráfico para Variante 1 (Static)...")
    df_var = df[df['variante'] == 1].copy()
    df_var['K'] = df_var['K'].astype(str) # Para legenda categórica
    
    Ns = [100000, 500000, 1000000]
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=False)
    
    for i, n in enumerate(Ns):
        ax = axes[i]
        subset = df_var[df_var['N'] == n]
        
        if subset.empty: continue
            
        sns.barplot(
            data=subset, x='numero_threads', y='tempo', hue='K',
            ax=ax, palette='viridis', edgecolor='black', errorbar='sd', capsize=0.05
        )
        
        ax.set_title(f"N = {n}", fontweight='bold')
        ax.set_xlabel("Threads")
        ax.set_ylabel("Tempo (s)" if i == 0 else "")
        if i != 2: ax.get_legend().remove() # Legenda só no último
        else: ax.legend(title='Fator K')

    plt.suptitle("Variante 1 (Static): Impacto do Desbalanceamento (K)", fontsize=16, y=1.05)
    plt.tight_layout()
    plt.savefig("results/analise_v1_static.png", bbox_inches='tight')
    plt.close()

# --- Gráfico 2: Variante 2 (Dynamic) - Grade 3x3 com Chunk Size ---
# (O NOVO gráfico solicitado)
def plotar_variante2_dynamic(df):
    print("Gerando grade 3x3 para Variante 2 (Dynamic)...")
    
    # Filtra Variante 2
    df_var = df[df['variante'] == 2].copy()
    
    # Converte chunk para string para garantir cores discretas (não gradiente)
    df_var['tamanho_chunk'] = df_var['tamanho_chunk'].astype(str)
    
    # Parâmetros da Grade
    Ns = [100000, 500000, 1000000] # Linhas
    Ks = [20, 24, 28]              # Colunas
    
    fig, axes = plt.subplots(3, 3, figsize=(18, 12), sharex=True)
    
    for i, n in enumerate(Ns):
        for j, k in enumerate(Ks):
            ax = axes[i, j]
            subset = df_var[(df_var['N'] == n) & (df_var['K'] == k)]
            
            if subset.empty:
                ax.text(0.5, 0.5, "Sem Dados", ha='center')
                continue

            # Plot: X=Threads, Y=Tempo, Hue=Chunk
            sns.barplot(
                data=subset,
                x='numero_threads',
                y='tempo',
                hue='tamanho_chunk', # <--- O segredo: barras coloridas por chunk
                ax=ax,
                palette='rocket',    # Paleta diferente para diferenciar do Static
                edgecolor='black',
                errorbar='sd',
                capsize=0.05
            )
            
            # Formatação
            ax.set_title(f"N={n} | K={k}", fontsize=10, fontweight='bold')
            
            # Labels Eixos (apenas nas bordas para limpar o visual)
            if j == 0: ax.set_ylabel("Tempo (s)")
            else: ax.set_ylabel("")
            
            if i == 2: ax.set_xlabel("Threads")
            else: ax.set_xlabel("")
            
            # Grid e Legenda
            ax.grid(axis='y', linestyle='--', alpha=0.5)
            
            # Remove legendas internas para não poluir
            # Vamos colocar a legenda apenas no gráfico superior direito
            if i == 0 and j == 2:
                ax.legend(title='Chunk Size', loc='upper right', fontsize='small')
            else:
                if ax.get_legend(): ax.get_legend().remove()

    plt.suptitle("Variante 2 (Dynamic): Impacto do Tamanho do Chunk", fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig("results/analise_v2_dynamic.png", bbox_inches='tight')
    plt.close()

# --- Gráfico 3: Variante 3 (Guided) - Grade 3x3 com Chunk Size ---
def plotar_variante3_guided(df):
    print("Gerando grade 3x3 para Variante 3 (Guided)...")
    
    # Filtra Variante 3
    df_var = df[df['variante'] == 3].copy()
    
    # Converte chunk para string para garantir cores discretas
    df_var['tamanho_chunk'] = df_var['tamanho_chunk'].astype(str)
    
    # Parâmetros da Grade
    Ns = [100000, 500000, 1000000] # Linhas
    Ks = [20, 24, 28]              # Colunas
    
    fig, axes = plt.subplots(3, 3, figsize=(18, 12), sharex=True)
    
    for i, n in enumerate(Ns):
        for j, k in enumerate(Ks):
            ax = axes[i, j]
            subset = df_var[(df_var['N'] == n) & (df_var['K'] == k)]
            
            if subset.empty:
                ax.text(0.5, 0.5, "Sem Dados", ha='center')
                continue

            # Plot: X=Threads, Y=Tempo, Hue=Chunk
            sns.barplot(
                data=subset,
                x='numero_threads',
                y='tempo',
                hue='tamanho_chunk', 
                ax=ax,
                palette='crest',     # Paleta 'crest' (azul/verde) para diferenciar das outras variantes
                edgecolor='black',
                errorbar='sd',
                capsize=0.05
            )
            
            # Formatação
            ax.set_title(f"N={n} | K={k}", fontsize=10, fontweight='bold')
            
            # Labels Eixos (limpeza visual)
            if j == 0: ax.set_ylabel("Tempo (s)")
            else: ax.set_ylabel("")
            
            if i == 2: ax.set_xlabel("Threads")
            else: ax.set_xlabel("")
            
            ax.grid(axis='y', linestyle='--', alpha=0.5)
            
            # Legenda apenas no gráfico superior direito
            if i == 0 and j == 2:
                ax.legend(title='Chunk Size', loc='upper right', fontsize='small')
            else:
                if ax.get_legend(): ax.get_legend().remove()

    plt.suptitle("Variante 3 (Guided): Impacto do Tamanho do Chunk", fontsize=16, y=1.02)
    plt.tight_layout()
    plt.savefig("results/analise_v3_guided.png", bbox_inches='tight')
    plt.close()

# --- Main ---
if __name__ == "__main__":
    df = carregar_dados()
    
    # Gera os gráficos
    plotar_variante1_static(df)
    plotar_variante2_dynamic(df)
    plotar_variante3_guided(df)
    
    print("Sucesso! Gráficos salvos na pasta 'results/'.")