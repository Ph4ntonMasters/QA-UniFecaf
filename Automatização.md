Centro:
Teste Automatizado com Selenium

1. Instalação e Configuração do Ambiente
pip install selenium

apt-get update

apt-get install chromium-browser chromium-chromedriver

2. Importação de Bibliotecas
selenium.webdriver

Service (gerenciar chromedriver)

By (localizar elementos)

Keys (teclado virtual)

time (esperas)

3. Configuração do Navegador Chrome
Criar chrome_options

Adicionar argumentos:

--headless (modo sem GUI)

--no-sandbox

--disable-dev-shm-usage

--disable-gpu

--window-size=1920,1200

4. Inicialização e Navegação
Iniciar driver com opções

Abrir URL: "https://www.saucedemo.com/"

5. Interação com Página
Preencher usuário: error_user

Preencher senha: secret_sauce

Clicar botão login

6. Espera e Validação
Esperar 2 segundos

Verificar se URL contém inventory

Imprimir mensagem de sucesso

7. Finalização
Fechar navegador (driver.quit)
