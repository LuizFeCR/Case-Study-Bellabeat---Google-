Estudo de Caso Bellabeat | Projeto de Análise de Dados

## 📌 Visão Geral do Projeto

Este projeto faz parte do programa Google Data Analytics Professional Certificate e tem como objetivo responder à seguinte pergunta de negócio:

> **Como uma empresa de bem-estar pode tomar decisões inteligentes com base em dados?**

A análise utiliza dados de dispositivos inteligentes (Fitbit) para entender o comportamento dos usuários e gerar insights que possam apoiar estratégias de marketing da Bellabeat.

---

## 🎯 Objetivo de Negócio

Identificar tendências no uso de dispositivos inteligentes para:

- Compreender o comportamento dos usuários  
- Apoiar decisões estratégicas de marketing  
- Gerar insights acionáveis para o negócio  

---

## 📂 Fonte de Dados

Os dados utilizados são públicos e disponíveis no Kaggle, contendo informações de usuários de dispositivos Fitbit.

Link: [Dados retirado do Kaggle](https://www.kaggle.com/datasets/arashnic/fitbit)

Os principais dados incluem:

    - Atividade diária (passos, calorias, intensidade)
    - Padrões de sono
    - Atividade por hora (opcional)

---

## 🛠️ Ferramentas Utilizadas

    - Python (Pandas, NumPy)
    - Power BI
    - Jupyter Notebook

---

## 🧹 Limpeza e Preparação dos Dados (Python)

As seguintes etapas foram realizadas:

### 1. Importação dos dados
    
    - Download da base de dados do Kaggle para a pasta Company
    - Leitura dos arquivos CSV utilizando Pandas

### 2. Junção dos dados

    - União dos datasets `dailyActivity` de diferentes períodos  
    - Junção entre dados de atividade e sono utilizando `Id` e `Data`

### 3. Limpeza dos dados
   
    - Remoção de duplicidades  
    - Padronização de formatos de data   
    - Tratamento de valores ausentes  

### 4. Criação de variáveis (Feature Engineering)

    - Criação da coluna `Activity_Level` baseada na quantidade de passos  
    - Criação da coluna `Weekday` (dia da semana)  

---

## 📊 Análise de Dados

A análise foi dividida em duas partes principais:

### 🔹 Tendências de Atividade

    - Média de passos diários  
    - Calorias queimadas  
    - Tempo sedentário  
    - Distribuição de nível de atividade  

### 🔹 Comportamento dos Usuários

    - Relação entre atividade física e sono  
    - Duração do sono  
    - Variação de atividade ao longo da semana  

---

## 📈 Dashboard (Power BI)

O dashboard foi estruturado em duas páginas:

### 🟢 Página 1 — Tendências de Atividade

<div align="center">
    <img width="750" height="550" alt="image" src="https://github.com/user-attachments/assets/4e21a92c-4667-4c2b-a321-d610f87f9395" />

</div>

    - Média de passos, calorias e tempo sedentário  
    - Distribuição do nível de atividade  
    - Passos por dia da semana  

---

### 🔵 Página 2 — Comportamento do Usuário

<div align="center">
    <img width="750" height="550" alt="image" src="https://github.com/user-attachments/assets/061f7f84-e487-4106-8750-adf1b1aff81d" />

</div>

    - Métricas médias de sono  
    - Relação entre atividade e sono  
    - Tempo sedentário por nível de atividade  

---

## 🔍 Principais Insights

    - A maioria dos usuários não atinge a meta recomendada de 10.000 passos por dia  
    - Os usuários apresentam alto nível de sedentarismo (~11 horas por dia)  
    - Usuários mais ativos tendem a ter melhor padrão de sono  
    - O comportamento de atividade varia ao longo da semana  

---

## 💡 Insights de Negócio e Recomendações

### 🚨 Problema

Os usuários apresentam baixos níveis de atividade física e alto comportamento sedentário.

---

### 📊 Oportunidade

Existe uma grande oportunidade de aumentar o engajamento dos usuários e promover hábitos mais saudáveis.

---

### 🚀 Recomendações

    - Implementar metas personalizadas de atividade diária  
    - Enviar notificações inteligentes para reduzir o sedentarismo  
    - Destacar a relação entre atividade física e qualidade do sono  
    - Criar campanhas de marketing voltadas para iniciantes  
    - Oferecer insights personalizados dentro do aplicativo  

---

## 🎯 Conclusão

A análise demonstra como dados de comportamento dos usuários podem ser utilizados para gerar insights estratégicos. Ao focar no aumento da atividade física e na melhoria do bem-estar geral, a Bellabeat pode fortalecer sua estratégia de marketing e aumentar o valor percebido do produto.

---

## 📎 Arquivos do Projeto

    - Data -> Dados retirados do Kaggle
    - Data_Cleaned -> Dados limpos que será utilizado
    - Python_Notebooks -> Arquivos de limpeza, preparação e análise dos dados  
    - Visualization -> Dashboard realizado no Power BI (.pbix)  
    - Reports -> Estudo de caso utilizado para este projeto



