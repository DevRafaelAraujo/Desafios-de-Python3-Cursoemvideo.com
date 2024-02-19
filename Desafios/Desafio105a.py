def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de uma turna de alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 50)
    turma = {}
    turma['total'] = len(notas)
    for i, n in enumerate(notas):
        if i == 0:
            turma['maior'] = n
            turma['menor'] = n
        else:
            if n > turma['maior']:
                turma['maior'] = n
            elif n < turma['menor']:
                turma['menor'] = n
    turma['média'] = sum(notas) / len(notas)
    if sit == True:
        if turma['média'] <= 5:
            turma['situação'] = 'Ruim'
        elif turma['média'] <= 7:
            turma['situação'] = 'Boa'
        elif turma['média'] <= 10:
            turma['situação'] = 'Ótima'
    return turma


resp = notas(8, 7, 9, sit=True)
print(resp)