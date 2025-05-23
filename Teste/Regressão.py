def test_regressao_login():
    assert login_usuario("marcio.silva@email.com", "1234") == "Login bem-sucedido"
    print("Teste de regressão para o login passou!")

test_regressao_login()

Saida: Teste de regressão para o login passou!
