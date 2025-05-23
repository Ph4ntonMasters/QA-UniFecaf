def test_aceitacao_fluxo_completo():
    assert cadastrar_usuario("Marcelo", "marcelo.castro@email.com", "pipoca2025") == "Usuário cadastrado com sucesso!"
    assert login_usuario("marcelo.castro@email.com", "pipoca2025") == "Login bem-sucedido"
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Notebook")
    assert carrinho.finalizar_compra() == "Compra finalizada com sucesso!"
    print("Teste de aceitação do fluxo completo passou!")

test_aceitacao_fluxo_completo()

Saida: Teste de aceitação do fluxo completo passou!
