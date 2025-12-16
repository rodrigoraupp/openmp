# Relatório de Reproduzibilidade

Este documento detalha as condições de hardware e software sob as quais os experimentos da Tarefa D foram conduzidos, garantindo que os resultados possam ser validados e replicados.

## 1. Ambiente de Software
- **Compilador:** `gcc (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0`
- **Flags de Compilação:** `-fopenmp -O3 -Wall`
- **Sistema Operacional:** `Ubuntu 22.04.5 LTS`
- **Ambiente de Execução:** Google Colab (Virtualizado)

## 2. Ambiente de Hardware
- **Modelo de CPU:** `Intel(R) Xeon(R) CPU @ 2.20GHz`
- **Número de vCPUs (Núcleos lógicos):** `2`
- **Threads por Núcleo:** `2`
- **Arquitetura:** `x86_64`

## 3. Configurações de Experimento
- **Afinidade (Thread Affinity):** Não definida manualmente. Foi utilizado o escalonamento padrão do Sistema Operacional (OS Default), permitindo que o escalonador do Linux gerencie a distribuição das threads nos núcleos disponíveis.
- **Semente do Gerador (Seed):** Não aplicável (N/A). A geração dos vetores seguiu uma lógica determinística (P.A.), onde:
  - `vetor1[i] = i + 1`
  - `vetor2[i] = i + 1 + N`
- **Schedule OpenMP:** Utilizado o schedule padrão (`static`), adequado para cargas de trabalho balanceadas.

## 4. Metodologia de Coleta
- **Amostragem:** Cada cenário (combinação de N e Número de Threads) foi executado **5 vezes**.
- **Processamento:** Os tempos de execução foram extraídos via script Bash (`run.sh`) e processados via script Python (`plot.py`) para cálculo de média aritmética e desvio padrão.
