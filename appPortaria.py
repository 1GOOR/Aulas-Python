# -*- coding: latin-1 -*-

def usuario(nome_input, cpf_input, email_input, telefone_input, data_cadastro_input, data_nascimeto_input):
    nome: str = nome_input
    cpf: str = cpf_input
    email: str = email_input
    telefone: str = telefone_input
    data_cadastro: str = data_cadastro_input
    data_nascimeto: str = data_nascimeto_input

    return [nome, cpf, email, telefone, data_cadastro, data_nascimeto]


def porteiro(nome_input, senha_input, cpf_input):
    nome: str = nome_input
    senha: str = senha_input
    cpf: str = cpf_input

    return [nome, senha, cpf]


def visita(cpf_usuario, data, hora_entrada, hora_saida, motivo, seguranca):

    cpf_usur = cpf_usuario
    data = data
    hora_entrada = hora_entrada
    hora_saida = hora_saida
    motivo = motivo
    responsavel = seguranca

    return [cpf_usur, data, hora_entrada, hora_saida, motivo, responsavel]


