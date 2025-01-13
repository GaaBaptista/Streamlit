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
    <df-messenger-chat chat-title="BQ_Query_Generator"></df-messenger-chat>
  </df-messenger>

  <style>
    df-messenger {
      z-index: 999;
      position: fixed;
      --df-messenger-font-color: #000;
      --df-messenger-font-family: Roboto Mono;
      --df-messenger-chat-background: #C8E6C9;
      --df-messenger-message-user-background: #097138;
      --df-messenger-message-bot-background: #EEF7EE;
      bottom: 0;
      right: 0;
      top: 0;
      width: 350px;
    }
  </style>
</div>
"""

# Usando o método `st.components.v1` para renderizar o HTML
components.html(html_code, height=600)