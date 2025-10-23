import matplotlib.pyplot as plt
import numpy as np

# SIMULAÇÃO DE DADOS (substitua pelos valores do Monitor Serial)

# Tempo em milissegundos
tempo = np.linspace(0, 4000, 40)

# Simulando a CARGA no capacitor (tensão decrescendo)
tensao_C = 5 - 0.00022 * tempo  # exemplo de decaimento linear

# Simulando a DESCARGA no resistor (tensão crescendo)
tensao_R = 0.00022 * tempo      # exemplo de aumento linear

# GRÁFICO 1: Carga no Capacitor (C)
plt.figure(figsize=(6, 4))
plt.plot(tempo, tensao_C, color='blue', label='Tensão no C (V)')
plt.title('Carga no Capacitor (C)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# GRÁFICO 2: Descarga no Resistor (R)
plt.figure(figsize=(6, 4))
plt.plot(tempo, tensao_R, color='red', label='Tensão no R (V)')
plt.title('Descarga no Resistor (R)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# GRÁFICO 3: Comparação entre C e R
plt.figure(figsize=(6, 4))
plt.plot(tempo, tensao_C, color='blue', label='Tensão no C (V)')
plt.plot(tempo, tensao_R, color='red', label='Tensão no R (V)')
plt.title('Comparação: Carga no C e Descarga no R')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
