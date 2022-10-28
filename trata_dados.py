def trata_dados(data_json):
    cod_funcionario = data_json['cod_funcionario']
    nome = data_json['nome']
    idade = data_json['idade']
    cargo_atual = data_json['cargos']['nome']
    data_admissao = data_json['data_admissao']
    data_ultima_promocao = data_json['data_ultima_promocao']
    salario = data_json['salario']
    return f'{cod_funcionario} - {nome} admitido em {data_admissao} | {idade} anos | {cargo_atual} desde {data_ultima_promocao} recebendo R${salario}'