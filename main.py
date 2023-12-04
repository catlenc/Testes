def nome(a):
    if a == "":
        return "Nome Invalido"
        
    else:
        return a
    
def cnpj(a):
    
    if a == 00000000000000:
        return "CNPJ Invalido"
    
    a = str(a)
    if len(a) < 15:
        return "Quantidade de dígitos invalidos"
    
    else:
        return a