import pytest
from main import nome
from main import cnpj

def test_nome_distribuidora():

    b = ""
    resultado = nome(b)
    assert resultado == "Nome Invalido"

def test_qntd_digitos_cnpj():
    b = 1234567890123
    resultado = cnpj(b)
    assert resultado == "Quantidade de dígitos invalidos"

def test_numeros_diferentes_zero():
    b = 00000000000000
    resultado = cnpj (b)
    assert resultado == "CNPJ Invalido"