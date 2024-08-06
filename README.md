# InstaBERT-EmotionGraph

InstaBERT-EmotionGraph é uma aplicação Streamlit que extrai comentários de posts do Instagram, analisa o conteúdo emocional usando um modelo BERT treinado para emoções em português, e visualiza os resultados em um gráfico interativo. Esta ferramenta fornece insights valiosos sobre a paisagem emocional das interações dos usuários nas redes sociais.

## Primeiros Passos

### Pré-requisitos
- Python 3.6 ou superior
- Streamlit
- Bibliotecas Python necessárias (veja `requirements.txt`)

### Instalação
1. Clone este repositório para sua máquina local:
   ```
   git clone https://github.com/seu-usuario/InstaEmotionBERT.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd InstaEmotionBERT
   ```
3. Instale os pacotes Python necessários:
   ```
   pip install -r requirements.txt
   ```

### Executando a Aplicação
Execute o seguinte comando para rodar o app:
```
streamlit run emotion_ig.py
```

## Autorização de Acesso ao Instagram
Se você encontrar um erro durante a coleta de comentários, talvez seja necessário entrar no aplicativo ou site do Instagram para autorizar o acesso à rede social. Esse passo garante que sua aplicação tenha as permissões necessárias para interagir com os dados do Instagram.

## Segurança e Privacidade
Esta aplicação não armazena nem tem acesso às suas credenciais do Instagram. A autenticação é gerenciada de forma segura pela API do Instagram, garantindo que suas informações permaneçam privadas.

## Contribuição
Contribuições para este projeto são bem-vindas! Por favor, faça um fork do repositório e envie pull requests com suas melhorias.

## Licença
Este projeto é open-source e está disponível sob a Licença MIT.
