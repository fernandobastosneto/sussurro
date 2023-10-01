# README: Tradutor de Vídeos do YouTube

---

## 📖 Sobre

O "Tradutor de Vídeos do YouTube" é um aplicativo desenvolvido com a biblioteca Streamlit que permite que os usuários transcrevam e traduzam vídeos do YouTube para a língua portuguesa. Ele usa o modelo Whisper da OpenAI para transcrição e o GPT-4 para tradução.

---

## 🌟 Funcionalidades

- **Transcrição de Vídeos do YouTube**: Converta a narração de vídeos do YouTube em texto.
- **Tradução para Português**: Traduza a transcrição para a língua portuguesa com alta precisão e entendimento contextual, graças ao GPT-4.
- **Contagem de Tokens**: Veja quantos tokens foram usados na transcrição, permitindo um controle melhor sobre o uso da API da OpenAI.
- **Interface Amigável**: O app possui uma interface simples e intuitiva, tornando a transcrição e tradução um processo fácil.

---

## 🛠️ Instalação e Uso

1. Clone o repositório:

```bash
git clone https://github.com/fernandobastosneto/sussurro.git
```

2. Instale as dependências:

```bash
pip install streamlit whisper pytube validators tiktoken openai
```

3. Execute o aplicativo:

```bash
streamlit run app.py
```

4. Acesse a interface do aplicativo em um navegador e insira a URL do vídeo do YouTube que deseja transcrever e traduzir.

---

## ⚠️ Requisitos

- **OpenAI API Key**: Este aplicativo requer uma chave API da OpenAI para funcionar corretamente. Você pode obter uma chave [aqui](https://platform.openai.com/account/api-keys).

![API Key Required](https://img.shields.io/badge/API%20Key-Required-red)

---

## 🙌 Contribuições

Sinta-se à vontade para contribuir para o projeto! Abra um Pull Request ou uma Issue no [GitHub](https://github.com/fernandobastosneto/sussurro/).

---

## 📫 Contato

Para quaisquer dúvidas ou sugestões, entre em contato:

👤 **Fernando Bastos**  
📧 fernando.bastos@itamaraty.gov.br

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT.

![GitHub](https://img.shields.io/github/license/fernandobastosneto/sussurro)

---

**Nota**: Este README é uma proposta e pode ser ajustado de acordo com as necessidades e preferências do desenvolvedor.