# BVP - CheckPoint 5 (FIWARE) - Sistema de Monitoramento Global de Vinherias🌿📡

Link do projeto no Wokwi: https://wokwi.com/projects/409941061090441217

## Visão Geral do Projeto 🌍
O projeto BVP implementa uma solução de Internet das Coisas (IoT) voltada para o monitoramento em tempo real de vinherias. O sistema coleta dados importantes como temperatura, umidade, luminosidade, permitindo que os produtores monitorem e tomem decisões mais rápidas e precisas para melhorar a qualidade das uvas e otimizar o manejo do vinho. Esses dados são visualizados em um painel interativo, permitindo um acompanhamento detalhado das condições de cultivo ao longo do tempo, com um histórico que vai se atualizando.

## Integrantes do Grupo 👥
### Bruno Carneiro Leão - 555563
### Paulo Akira Okama - 556840
### Victor Capp - 555753
### Matheus Henriques do Amaral - 556957

## Arquitetura do Sistema 🏗️
A arquitetura do sistema é dividida em duas camadas principais:

## Camada IoT 🌱:
Nesta camada, sensores e microcontroladores instalados na vinheria capturam dados ambientais em tempo real. Esses dados são transmitidos via Wi-Fi e MQTT para o servidor de processamento.

Microcontroladores: Dispositivos como ESP32 são usados para processar dados de sensores e transmiti-los em tempo real.
Sensores: Responsáveis por capturar informações como temperatura, umidade do ar e do solo, luminosidade e localização GPS.
Protocolo MQTT: Utilizado para garantir a transmissão eficiente dos dados para a nuvem ou servidores locais.

## Camada de Aplicação 📊:
Responsável por exibir os dados em um painel (dashboard) que os produtores utilizam para monitorar as condições da vinheria e otimizar a estratégia de cultivo.
Dash e Plotly: Bibliotecas utilizadas para criar gráficos interativos que exibem as condições da vinheria em tempo real.
STH-Comet: Para armazenar e consultar dados históricos, permitindo análises detalhadas ao longo das safras.

## Recursos Necessários 🚀
### Dispositivos IoT

Microcontroladores: ESP32 ou equivalentes para processar os dados dos sensores em tempo real.

### Sensores:
Sensores de Temperatura: Para monitorar o aquecimento do ambiente.
Sensores de Umidade: Para verificar a umidade do ar e do solo.
Luminosidade: Para monitorar a quantidade de luz recebida pelas vinhas.

## Back-End ⚙️
FIWARE Orion Context Broker: Gerencia e armazena os dados de telemetria da vinheria em tempo real.

STH-Comet: Armazena os dados históricos e permite consultas sobre as condições da vinheria em períodos anteriores.
Broker MQTT: Facilita a comunicação entre os sensores IoT e o servidor central.

## Front-End 🎨

Dash (Python): Criação do painel interativo para visualização dos dados.
Plotly: Gráficos dinâmicos que mostram os dados da vinheria.
HTML/CSS: Estruturação e estilização do dashboard.

## Passo a Passo de Implementação 🔧
### Configuração do Microcontrolador (ESP32)

Conecte os sensores de temperatura, umidade e luminosidade ao ESP32.
Suba o código no ESP32 para que ele colete os dados dos sensores e envie-os para o servidor via MQTT.

### Configuração do Back-End

Instale o FIWARE Orion Context Broker para gerenciar os dados em tempo real.
Configure o STH-Comet para armazenar o histórico de dados.
Configure o broker MQTT (como Mosquitto) para garantir que os dados dos sensores cheguem ao servidor de telemetria em tempo real.

### Configuração do Front-End

Clone o repositório: git clone https://github.com/BVP-projetos/CP5-EDGE-FIWARE-BVP/tree/main
Instale as dependências do Python: pip install -r requirements.txt
Execute o painel de controle: python app1_copy.py
Acesse o dashboard no navegador: http://localhost:8050

## Explicação do Código 🧑‍💻

### Códigos IoT (ESP32)
O código do ESP32 coleta dados dos sensores em tempo real e os envia para o broker MQTT. Aqui estão alguns detalhes do funcionamento do código:

### Leitura de Sensores:

O código lê os dados dos sensores de temperatura, umidade e luminosidade e os armazena para serem enviados ao servidor.
Exemplo: float temperature = dht.readTemperature(); MQTT.publish(TOPICO_PUBLISH_3, String(temperature).c_str());

### Transmissão de Dados via MQTT:

Após ler os sensores, o ESP32 utiliza o protocolo MQTT para enviar os dados para o servidor de telemetria.
Exemplo: MQTT.publish(TOPICO_PUBLISH_2, String(luminosity).c_str());
Códigos Front-End (Dashboard em Dash e Plotly)
O painel de controle foi construído utilizando Dash e Plotly para fornecer uma interface gráfica interativa e em tempo real. As principais funcionalidades incluem:

### Gráficos de Monitoramento em Tempo Real:

O sistema exibe gráficos de temperatura, umidade e luminosidade em tempo real.
Exemplo: trace_temp = go.Scatter(x=timestamps, y=temperature, mode='lines+markers', name='Temperatura')
O painel também exibe informações como temperatura e umidade em cartões dinâmicos, atualizados em tempo real.

### Histórico de Desempenho:

Os produtores podem verificar o histórico de dados coletados durante as safras para ajustes estratégicos.

## Funcionalidades Principais 🏆

Monitoramento em Tempo Real: Exibe as condições de temperatura, umidade e luminosidade da vinheria durante as 24 horas.
Armazenamento e Consulta de Dados Históricos: O histórico das condições ambientais é armazenado e pode ser consultado para análises futuras.
Alertas de Desempenho: Possibilidade de criar alertas quando parâmetros críticos, como temperatura ou umidade, atingem limites que podem comprometer o desenvolvimento do vinho.

## Instruções de Uso 📋
Inicie o sistema conectando os sensores ao ESP32 em cada área da vinheria.
Monitore os dados em tempo real através do painel de controle, ajustando a estratégia de manejo conforme necessário.
Revise o histórico de condições ambientais através dos gráficos históricos disponíveis no painel.

## Requisitos e Dependências 🛠️
Python 3.8 ou superior
Bibliotecas Python: dash, plotly, requests, pytz
Plataforma FIWARE: Orion Context Broker e STH-Comet configurados.
Broker MQTT: Mosquitto ou equivalente para comunicação de dados.

## Licença 📄
Este projeto é de código aberto e está licenciado sob os termos da licença MIT.

## Contato 💬
Para mais informações ou dúvidas, entre em contato com os integrantes do projeto BVP:

Bruno Carneiro Leão - 555563
Paulo Akira Okama - 556840
Victor Capp - 555753
Matheus Henriques do Amaral - 556957
