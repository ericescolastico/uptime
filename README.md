# UPTIME | Python Discord Bot

Este projeto é um bot simples para Discord desenvolvido em Python, projetado para monitorar e registrar o status (online e offline) de membros com um cargo específico em um servidor.

Funciona como um registro de inicio de horário de trabalho e fim do expediente, de acordo com o status do usuário.

Além disso, ele contém funcionalidades administrativas básicas e funcionalidades utilitárias para facilitar a manutenção e monitoramento do bot.

O bot foi construido de forma **modular**, portanto os comandos e funcionalidades do bot estão em módulos presentes na pasta *commands* e referenciados no arquivo principal, *bot.py*. Assim, a aplicação tem maior escalabilidade caso seja necessário.

## Funcionalidades

- **Registro de Presença**: Monitoramento da presença dos membros com cargo específico, registrando entradas e saídas em uma planilha do Google Sheets.

- **Administração do Servidor**: Comandos para limpeza de mensagens em um canal especifico de servidor, além de comando de encerramento do bot.

- **Eventos Utilitários**: Notificações sobre o status do bot, como quando ele está online ou desconectado.


## Tecnologias Utilizadas
- **Linguagem**: Python
- **Bibliotecas**: `discord.py`, `gspread`, `oauth2client`
- **Google Sheets API**: Utilizada para armazenar registros de presença dos membros.

## Próximas atualizações (Em breve)
* Cálculo automático de horas trabalhadas (horas online)
* Funções de consultas de horas trabalhadas, lembretes e relatórios.

## Contribuição e Suporte
Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções. Toda contribuição é bem-vinda! 💖

Caso precise, também pode entrar em contato comigo! 
___

# Eric Escolástico (Autor)
Este projeto foi desenvolvido por **Eric Escolástico**, especialista em marketing e comunicação com vasta experiência em planejamento e execução de campanhas digitais. 

Apaixonado por conectar marcas ao público-alvo certo, utilizando estratégias eficientes e automações inteligentes para aumentar o engajamento e a presença digital. Além de sua expertise em desenvolvimento, possui um sólido histórico em publicidade, marketing de conteúdo e gestão de comunidades online. 

### Redes Sociais
<div style="display: flex; gap: 2px; align-items: center;">
  <!-- Instagram -->
  <a href="https://www.instagram.com/ericescolastico.mkt" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram de Eric Escolástico">
  </a>

  <!-- LinkedIn -->
  <a href="https://www.linkedin.com/in/ericescolastico" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn de Eric Escolástico">
  </a>

  <!-- GitHub -->
  <a href="https://github.com/ericescolastico" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub de Eric Escolástico">
  </a>

  <!-- Website -->
  <a href="https://www.ericescolastico.com" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white" alt="Website de Eric Escolástico">
  </a>
</div>

