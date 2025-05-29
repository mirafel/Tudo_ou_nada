# Tudo ou Nada - Interview Assistant - README

## 1. Descrição do Projeto

Este é um assistente de entrevista desktop que:
*   Escuta o áudio do seu microfone em tempo real.
*   Transcreve o que foi dito usando a API Google Cloud Speech-to-Text.
*   Gera uma sugestão de resposta usando a API Google Gemini.
*   Exibe a transcrição e a sugestão na interface gráfica.

## 2. Estrutura dos Arquivos

*   `main.py`: O código principal da aplicação, contendo a interface Tkinter e a lógica de streaming, transcrição e chamada da API Gemini.
*   `config.py`: Arquivo de configuração onde você deve colocar suas chaves de API e caminhos de arquivos.
*   `requirements.txt`: Lista das bibliotecas Python necessárias para o projeto.
*   `README.txt`: Este arquivo, com as instruções.
*   `assets/`: Pasta para guardar recursos visuais opcionais (como ícones para a janela).

## 3. Pré-requisitos

*   Python 3.7 ou superior instalado.
*   Acesso à internet para as APIs do Google.
*   Um microfone configurado no seu sistema.

## 4. Instalação

1.  **Clone ou baixe o projeto:** Coloque todos os arquivos em uma pasta no seu computador.
2.  **(Opcional, mas recomendado) Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate    # Windows
    ```
3.  **Instale as dependências:** Navegue até a pasta do projeto no seu terminal e execute:
    ```bash
    pip install -r requirements.txt
    ```
    *   **Atenção PyAudio:** A instalação do `PyAudio` pode falhar se você não tiver as dependências do sistema (como `portaudio` no Linux/Mac, ou às vezes requer Microsoft Visual C++ Build Tools no Windows). Se falhar, veja a mensagem de erro ou consulte a documentação do PyAudio: <https://people.csail.mit.edu/hubert/pyaudio/>

## 5. Configuração (Importante!)

Abra o arquivo `config.py` em um editor de texto e **modifique as seguintes variáveis**:

*   `GEMINI_API_KEY`: Substitua `"YOUR_GEMINI_API_KEY_HERE"` pela sua chave de API real da Gemini. Você pode obter uma no Google AI Studio: <https://aistudio.google.com/app/apikey>
*   `GOOGLE_APPLICATION_CREDENTIALS_PATH`: Substitua o caminho de exemplo pelo **caminho completo** para o seu arquivo JSON de credenciais do Google Cloud. Este arquivo é necessário para a API Speech-to-Text. Veja como obter um aqui: <https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev>

**Outras configurações (opcional):**

*   `TRANSCRIPTION_LANGUAGE_CODE`: Mude para o código de idioma desejado (ex: `"pt-BR"` para português).
*   `GEMINI_MODEL_NAME`: Escolha outro modelo Gemini compatível, se desejar.

## 6. Executando a Aplicação

Após instalar as dependências e configurar o `config.py`, navegue até a pasta do projeto no seu terminal e execute:

```bash
python main.py
```

A interface gráfica deve aparecer.

## 7. Como Usar

1.  Clique no botão "Iniciar Escuta".
2.  O status mudará para "Ouvindo...". Fale algo no microfone.
3.  Após uma pausa, o que você disse será transcrito e exibido como "[Você disse]: ...".
4.  Em seguida, a sugestão da API Gemini será exibida como "[Sugestão Gemini]: ...".
5.  O assistente continuará ouvindo para a próxima interação.

## 8. Pasta Assets

A pasta `assets/` pode ser usada para colocar arquivos de imagem (como `.png` ou `.ico`) para usar como ícone da aplicação. O código em `main.py` tem uma seção comentada para carregar um ícone chamado `app_icon.png` desta pasta.

