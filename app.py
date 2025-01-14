import streamlit as st
import streamlit.components.v1 as components

# Código HTML para o chatbot
html_code = """
<div id="chatbot">
  <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
  <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>

  <df-messenger
    location="us-east1"
    project-id="corporativo-ia"
    agent-id="f1c06274-0f5c-4254-a839-1d5161c3202a"
    language-code="pt-br"
    max-query-length="-1">
    <df-messenger-chat chat-title="Gerador de Query - GCP"></df-messenger-chat>
  </df-messenger>

  <style>
    df-messenger {
      z-index: 999;
      position: fixed;
      --df-messenger-font-color: #000;
      --df-messenger-font-family: Roboto Mono;
      --df-messenger-chat-background: #2A56C6;
      --df-messenger-message-user-background: #4285F4;
      --df-messenger-message-bot-background: #FFFFFF;
      --df-messenger-message-user-font-color: #FFFFFF;
      top: 0;
      left: 0;  right: 0;  bottom: 0;
      width: 100vw;  height: 100vh; }
  </style>
</div>
"""

# Usando o método `st.components.v1` para renderizar o HTML
components.html(html_code)
