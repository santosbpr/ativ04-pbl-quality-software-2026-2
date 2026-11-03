from playwright.sync_api import Page, expect

# Responsável: [Seu Nome]
def test_verificar_pagina_inicial(page: Page):
    page.goto("https://local-eats-unisenac.vercel.app/")

    # Busca o texto que realmente está na tela
    mensagem = page.locator("text=Bem-vindo ao app de Qualidade de Software")
    expect(mensagem).to_be_visible()