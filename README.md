# Análise de Carga e Descarga em Circuito RC
**Autora:** Raiane Araujo Brandão  
**Plataforma:** Tikercad Arduino Simulator  
**Linguagem:** C++ (Arduino)

## Objetivo
Este projeto tem como objetivo analisar o comportamento de **carga e descarga** em um circuito **RC (Resistor-Capacitor)**, utilizando dados obtidos pelo **Monitor Serial do Arduino** e processados no **Python** para geração de gráficos.

A atividade propõe compreender a variação da tensão nos componentes ao longo do tempo e comparar os comportamentos do capacitor e do resistor durante o processo.

---

## Etapas da Atividade

1. **Copiar os valores do Monitor Serial**
   - Execute o circuito RC no Arduino e abra o **Monitor Serial**.
   - Copie os valores de tempo (ms) e tensão (V).

2. **Colar os valores no Python**
   - Substitua os dados simulados no script `grafico_carga_descarga.py` pelos seus valores reais.

3. **Gerar os gráficos**
   - Execute o arquivo no terminal:
     ```bash
     python grafico_carga_descarga.py
     ```
   - O script gera três gráficos:
     - **Carga no Capacitor (C)**
     - **Descarga no Resistor (R)**
     - **Comparação entre C e R**

4. **Analisar os resultados**
   - Observe se os dois gráficos apresentam comportamento **complementar**:
     - Enquanto o capacitor descarrega (tensão decresce),
     - O resistor apresenta aumento na tensão (descarga do circuito).

---

## Gráficos Gerados

| Gráfico | Descrição |
|----------|------------|
| **Carga no Capacitor (C)** | Mostra a variação decrescente da tensão no capacitor ao longo do tempo. |
| **Descarga no Resistor (R)** | Mostra o aumento gradual da tensão no resistor durante a descarga. |
| **Comparação** | Exibe ambos os comportamentos no mesmo eixo temporal, evidenciando a relação inversa entre eles. |

Os arquivos gerados são salvos automaticamente:
- `grafico_carga_capacitor.png`
- `grafico_descarga_resistor.png`
- `grafico_comparacao.png`

---

## Tecnologias Utilizadas para criação dos gráficos:
- **Python 3**
- **Biblioteca Matplotlib**
- **NumPy**

---

## Conclusão
A partir dos gráficos, é possível observar o comportamento característico do circuito RC:
- A tensão no **capacitor** diminui exponencialmente durante a descarga;
- A tensão no **resistor** aumenta na mesma proporção, demonstrando a transferência de energia.

A comparação dos gráficos permite validar experimentalmente as leis do circuito RC e compreender como o capacitor armazena e libera carga elétrica ao longo do tempo.

---

Projeto desenvolvido por **Raiane Araujo Brandão**,  
como parte das atividades práticas do curso do **Inteli – Instituto de Tecnologia e Liderança**.
