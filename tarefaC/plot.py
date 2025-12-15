#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import statistics
import os

# Criar diretório para gráficos
os.makedirs('results/plots', exist_ok=True)

# Lê o CSV
data = defaultdict(list)

with open('results/resultados.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        key = (row['versao'], int(row['n']), int(row['threads']))
        data[key].append(float(row['tempo_ms']))

# Calcula estatísticas
stats = {}
for key, tempos in data.items():
    stats[key] = {
        'mean': statistics.mean(tempos),
        'stdev': statistics.stdev(tempos) if len(tempos) > 1 else 0
    }

# Configuração visual
plt.style.use('seaborn-v0_8-darkgrid')
colors = {'seq': '#e74c3c', 'simd': '#3498db', 'parallel_simd': '#2ecc71'}

# ========== GRÁFICO 1: Tempo vs Tamanho (todas versões) ==========
fig, ax = plt.subplots(figsize=(12, 7))

sizes = sorted(set(k[1] for k in stats.keys()))

# Sequencial
seq_times = [stats[('seq', n, 1)]['mean'] for n in sizes]
seq_stdev = [stats[('seq', n, 1)]['stdev'] for n in sizes]
ax.errorbar(sizes, seq_times, yerr=seq_stdev, marker='o', linewidth=2,
            label='Sequencial', color=colors['seq'], capsize=5)

# SIMD
simd_times = [stats[('simd', n, 1)]['mean'] for n in sizes]
simd_stdev = [stats[('simd', n, 1)]['stdev'] for n in sizes]
ax.errorbar(sizes, simd_times, yerr=simd_stdev, marker='s', linewidth=2,
            label='SIMD', color=colors['simd'], capsize=5)

# Parallel + SIMD (8 threads)
par_times = [stats[('parallel_simd', n, 8)]['mean'] for n in sizes]
par_stdev = [stats[('parallel_simd', n, 8)]['stdev'] for n in sizes]
ax.errorbar(sizes, par_times, yerr=par_stdev, marker='^', linewidth=2,
            label='Parallel+SIMD (8 threads)', color=colors['parallel_simd'], capsize=5)

ax.set_xlabel('Tamanho do Array (N)', fontsize=12)
ax.set_ylabel('Tempo (ms)', fontsize=12)
ax.set_title('SAXPY: Tempo de Execução vs Tamanho', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('results/plots/tempo_vs_tamanho.png', dpi=300)
plt.close()

# ========== GRÁFICO 2: Speedup vs Tamanho ==========
fig, ax = plt.subplots(figsize=(12, 7))

speedup_simd = [stats[('seq', n, 1)]['mean'] / stats[('simd', n, 1)]['mean'] 
                for n in sizes]
speedup_par = [stats[('seq', n, 1)]['mean'] / stats[('parallel_simd', n, 8)]['mean'] 
               for n in sizes]

x = np.arange(len(sizes))
width = 0.35

bars1 = ax.bar(x - width/2, speedup_simd, width, label='SIMD', 
               color=colors['simd'], alpha=0.8)
bars2 = ax.bar(x + width/2, speedup_par, width, label='Parallel+SIMD (8T)', 
               color=colors['parallel_simd'], alpha=0.8)

ax.axhline(y=1, color='red', linestyle='--', linewidth=2, label='Baseline (1x)')
ax.set_xlabel('Tamanho do Array (N)', fontsize=12)
ax.set_ylabel('Speedup (vs Sequencial)', fontsize=12)
ax.set_title('SAXPY: Speedup Relativo ao Sequencial', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([f'{n:,}' for n in sizes])
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Adiciona valores nas barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}x', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('results/plots/speedup_vs_tamanho.png', dpi=300)
plt.close()

# ========== GRÁFICO 3: Escalabilidade (Parallel+SIMD) ==========
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for idx, n in enumerate(sizes):
    ax = axes[idx]
    
    threads_list = sorted(set(k[2] for k in stats.keys() 
                             if k[0] == 'parallel_simd' and k[1] == n))
    
    times = [stats[('parallel_simd', n, t)]['mean'] for t in threads_list]
    stdevs = [stats[('parallel_simd', n, t)]['stdev'] for t in threads_list]
    speedups = [stats[('seq', n, 1)]['mean'] / t for t in times]
    
    ax.errorbar(threads_list, speedups, marker='o', linewidth=2,
                color=colors['parallel_simd'], capsize=5)
    ax.plot(threads_list, threads_list, 'r--', linewidth=2, label='Ideal (linear)')
    
    ax.set_xlabel('Número de Threads', fontsize=11)
    ax.set_ylabel('Speedup (vs Sequencial)', fontsize=11)
    ax.set_title(f'N = {n:,}', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xticks(threads_list)

plt.suptitle('SAXPY: Escalabilidade da Versão Parallel+SIMD', 
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('results/plots/escalabilidade.png', dpi=300)
plt.close()

# ========== GRÁFICO 4: Eficiência Paralela ==========
fig, ax = plt.subplots(figsize=(12, 7))

for n in sizes:
    threads_list = sorted(set(k[2] for k in stats.keys() 
                             if k[0] == 'parallel_simd' and k[1] == n))
    
    times = [stats[('parallel_simd', n, t)]['mean'] for t in threads_list]
    speedups = [stats[('seq', n, 1)]['mean'] / t for t in times]
    eficiencias = [(s / t) * 100 for s, t in zip(speedups, threads_list)]
    
    ax.plot(threads_list, eficiencias, marker='o', linewidth=2, 
            label=f'N = {n:,}')

ax.axhline(y=100, color='red', linestyle='--', linewidth=2, label='Ideal (100%)')
ax.set_xlabel('Número de Threads', fontsize=12)
ax.set_ylabel('Eficiência Paralela (%)', fontsize=12)
ax.set_title('SAXPY: Eficiência da Paralelização', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 110)
plt.tight_layout()
plt.savefig('results/plots/eficiencia.png', dpi=300)
plt.close()

# ========== GRÁFICO 5: Variância (Desvio Padrão) ==========
fig, ax = plt.subplots(figsize=(12, 7))

# Compara variância entre as versões para N=1M
n = 1000000
versions = ['seq', 'simd', 'parallel_simd']
labels = ['Sequencial', 'SIMD', 'Parallel+SIMD (8T)']
threads_map = {'seq': 1, 'simd': 1, 'parallel_simd': 8}

means = [stats[(v, n, threads_map[v])]['mean'] for v in versions]
stdevs = [stats[(v, n, threads_map[v])]['stdev'] for v in versions]
cv = [(s/m)*100 for s, m in zip(stdevs, means)]  # Coeficiente de variação

x = np.arange(len(versions))
bars = ax.bar(x, cv, color=[colors[v] for v in versions], alpha=0.8)

ax.set_xlabel('Versão', fontsize=12)
ax.set_ylabel('Coeficiente de Variação (%)', fontsize=12)
ax.set_title(f'SAXPY: Variabilidade das Medições (N = {n:,})', 
             fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.grid(True, alpha=0.3, axis='y')

# Adiciona valores nas barras
for i, (bar, mean, std) in enumerate(zip(bars, means, stdevs)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}%\n({std:.2f}ms)', 
            ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig('results/plots/variancia.png', dpi=300)
plt.close()

print("="*80)
print("GRÁFICOS GERADOS COM SUCESSO")
print("="*80)
print("\nArquivos criados em results/plots/:")
print("  1. tempo_vs_tamanho.png    - Comparação de tempos entre versões")
print("  2. speedup_vs_tamanho.png  - Speedup relativo ao sequencial")
print("  3. escalabilidade.png      - Escalabilidade por número de threads")
print("  4. eficiencia.png          - Eficiência paralela")
print("  5. variancia.png           - Análise de variabilidade das medições")
print("="*80)