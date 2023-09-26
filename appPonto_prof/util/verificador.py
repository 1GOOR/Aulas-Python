
def validarCpf(cpf):
    if len(cpf) == 11 and cpf.isdigit():
        return cpf


def validarTelefone(telefone):
    if (len(telefone) >= 8 or len(telefone) <= 11) and telefone.isdigit():
        return telefone


