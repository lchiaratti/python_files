endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, RJ, 23440-120"

import re # Regular Expression -- REGEX

# 5 digitos +- (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)
