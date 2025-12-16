
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Nome do arquivo CSV gerado pelo run.sh
CSV_FILE = 'resultados_D.csv'
OUTPUT_DIR = 'plots_D/'

# 1. Cria o diretório de saída se não existir
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 2. Carregar e Limpar Dados
try:
    # Leitura, usando ';' como separador
    df = pd.read_csv(CSV_FILE, sep=';')
except FileNotFoundError:
    print(f"Erro: Arquivo {CSV_FILE} não encontrado. Execute o run.sh primeiro.")
    exit()

# 3. Calcular a Média e o Desvio Padrão
# Agrupamos por N e Threads e calculamos as estatísticas
df_grouped = df.groupby(['N', 'Threads']).agg(
    Tempo_Ingenua_Mean=('Tempo_Ingenua', 'mean'),
    Tempo_Ingenua_Std=('Tempo_Ingenua', 'std'),
    Tempo_Arrumada_Mean=('Tempo_Arrumada', 'mean'),
    Tempo_Arrumada_Std=('Tempo_Arrumada', 'std')
).reset_index()

# 4. Geração dos Gráficos (Um gráfico para cada valor de N)

for N_value in df_grouped['N'].unique():
    # Filtra os dados apenas para o N atual
    df_n = df_grouped[df_grouped['N'] == N_value]

    # Inicia o plot
    plt.figure(figsize=(10, 6))

    threads = df_n['Threads']

    # Plota a Variante Ingênua
    plt.errorbar(
        threads,
        df_n['Tempo_Ingenua_Mean'],
        yerr=df_n['Tempo_Ingenua_Std'],
        label='Variante Ingênua (2x FORK/JOIN)',
        marker='o',
        capsize=5
    )

    # Plota a Variante Arrumada
    plt.errorbar(
        threads,
        df_n['Tempo_Arrumada_Mean'],
        yerr=df_n['Tempo_Arrumada_Std'],
        label='Variante Arrumada (1x FORK/JOIN)',
        marker='s',
        capsize=5
    )

    # Títulos e rótulos
    plt.title(f'Tarefa D: Overhead vs. Threads (N = {N_value})', fontsize=14)
    plt.xlabel('Número de Threads', fontsize=12)
    plt.ylabel('Tempo de Execução Médio (s)', fontsize=12)
    plt.xticks(threads)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Salva o gráfico
    filename = f'{OUTPUT_DIR}tempo_vs_threads_N_{N_value}.png'
    plt.savefig(filename)
    plt.close()

print(f"Geração de gráficos concluída. Arquivos salvos em /{OUTPUT_DIR}")

# --- Gráfico de Speedup Adicional (Opcional, mas recomendado) ---
# Você também deve plotar o Speedup (Tempo Sequencial / Tempo Paralelo)
# O tempo sequencial (1 thread) é o Tempo_Arrumada_Mean quando Threads=1
df_1_thread = df_grouped[df_grouped['Threads'] == 1]

for N_value in df_grouped['N'].unique():
    df_n = df_grouped[df_grouped['N'] == N_value]

    # Encontra o tempo sequencial (tempo da versão arrumada com 1 thread)
    T1_arru = df_1_thread[df_1_thread['N'] == N_value]['Tempo_Arrumada_Mean'].iloc[0]

    # Calcula o Speedup
    speedup_ing = T1_arru / df_n['Tempo_Ingenua_Mean']
    speedup_arru = T1_arru / df_n['Tempo_Arrumada_Mean']

    plt.figure(figsize=(10, 6))

    plt.plot(threads, speedup_ing, label='Speedup - Variante Ingênua', marker='o')
    plt.plot(threads, speedup_arru, label='Speedup - Variante Arrumada', marker='s')

    plt.title(f'Speedup (Base T1 Arrumada) vs. Threads (N = {N_value})', fontsize=14)
    plt.xlabel('Número de Threads', fontsize=12)
    plt.ylabel('Speedup', fontsize=12)
    plt.xticks(threads)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.axhline(y=1.0, color='r', linestyle='--')

    filename = f'{OUTPUT_DIR}speedup_vs_threads_N_{N_value}.png'
    plt.savefig(filename)
    plt.close()

print("Geração dos gráficos de Speedup concluída.")
