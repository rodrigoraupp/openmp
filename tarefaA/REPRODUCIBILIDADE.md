# Relatório de Reprodutibilidade - Tarefa A

Este arquivo documenta o ambiente exato utilizado para gerar os resultados experimentais.

## 1. Hardware (CPU)
```text
Arquitetura:                          x86_64
Modo(s) operacional da CPU:           32-bit, 64-bit
Address sizes:                        39 bits physical, 48 bits virtual
Ordem dos bytes:                      Little Endian
CPU(s):                               4
Lista de CPU(s) on-line:              0-3
ID de fornecedor:                     GenuineIntel
Nome do modelo:                       Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz
Família da CPU:                       6
Modelo:                               61
Thread(s) per núcleo:                 2
Núcleo(s) por soquete:                2
Soquete(s):                           1
Step:                                 4
CPU(s) scaling MHz:                   94%
CPU MHz máx.:                         3000,0000
CPU MHz mín.:                         500,0000
BogoMIPS:                             4788,85
Opções:                               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb pti ssbd ibrs ibpb stibp tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid rdseed adx smap intel_pt xsaveopt dtherm ida arat pln pts vnmi md_clear flush_l1d ibpb_exit_to_user
Virtualização:                        VT-x
cache de L1d:                         64 KiB (2 instances)
cache de L1i:                         64 KiB (2 instances)
cache de L2:                          512 KiB (2 instances)
cache de L3:                          4 MiB (1 instance)
Nó(s) de NUMA:                        1
CPU(s) de nó0 NUMA:                   0-3
Vulnerability Gather data sampling:   Not affected
Vulnerability Itlb multihit:          KVM: Mitigation: VMX disabled
Vulnerability L1tf:                   Mitigation; PTE Inversion; VMX conditional cache flushes, SMT vulnerable
Vulnerability Mds:                    Mitigation; Clear CPU buffers; SMT vulnerable
Vulnerability Meltdown:               Mitigation; PTI
Vulnerability Mmio stale data:        Unknown: No mitigations
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed:               Not affected
Vulnerability Spec rstack overflow:   Not affected
Vulnerability Spec store bypass:      Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1:             Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:             Mitigation; Retpolines; IBPB conditional; IBRS_FW; STIBP conditional; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
Vulnerability Srbds:                  Mitigation; Microcode
Vulnerability Tsx async abort:        Not affected
Vulnerability Vmscape:                Mitigation; IBPB before exit to userspace
```

## 2. Software (Compilador)
```text
gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```

## 3. Informações do Sistema Operacional
```text
Linux acer 6.8.0-90-generic #91-Ubuntu SMP PREEMPT_DYNAMIC Tue Nov 18 14:14:30 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
PRETTY_NAME="Linux Mint 22.1"
```

## 4. Configurações de Compilação (Flags)

As seguintes flags foram utilizadas no `Makefile`:

* **Compilador:** `gcc`
* **Flags Gerais:** `-Wall -O3` (Avisos habilitados, Otimização nível 3)
* **OpenMP:** `-fopenmp`
* **Libraries:** `-lm` (Math library)

## 5. Afinidade de Threads e Execução

* **Afinidade (Affinity):** Nenhuma afinidade explícita foi definida (`OMP_PROC_BIND` ou `OMP_PLACES` não foram setados). O gerenciamento de threads ficou a cargo do escalonador padrão do Sistema Operacional (Linux/Docker).
* **Threads:** Os testes variaram de 1 a 16 threads conforme especificado no `run.sh`.

## 4. Reprodução dos Experimentos

```bash
# 1. Clonar e entrar no diretório
git clone https://github.com/rodrigoraupp/openmp
cd openmp/tarefaA

# 2. Compilar
make all

# 3. Executar experimentos
make run

# 4. Gerar gráficos
make plot
```