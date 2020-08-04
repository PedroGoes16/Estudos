def notas(*n, sit=False):
    """
    -> Função para notas e situação de vário alunos.
    :param n: notas dos alunos
    :param sit: valor opcional, indincando de quer ou não mostrar a situação
    :return: dicionário com várias informações da turma.
    """
    d = {}
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['media'] = sum(n)/len(n)
    if sit:
        if d['media'] >= 7:
            d['situação'] = 'BOA'
        if 5 <= d['media'] <7:
            d['situação'] = 'RAZOÁVEL'
        if d['media'] < 5:
            d['situação'] = 'RUIM'
    return d


resp = notas(3, 6, 10, 6.5, sit=True)
print(resp)
help(notas)