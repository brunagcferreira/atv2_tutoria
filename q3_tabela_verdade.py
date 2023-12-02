def tabela_verdade(conectivo):
    print(f'Tabela verdade para {conectivo}:')
    print('p\tq\tresultado')
    print('-'*22)
    for p in [True, False]:
        for q in [True, False]:
            if conectivo == 'conjunção':
                result = p and q
            elif conectivo == 'disjunção':
                result = p or q
            elif conectivo == 'condicional':
                result = (not p) or q
            elif conectivo == 'bicondicional':
                result = p == q
            elif conectivo == 'xor':
                result = p != q
            print(f'{p}\t{q}\t{result}')
    print()

tabela_verdade('conjunção')
tabela_verdade('disjunção')
tabela_verdade('condicional')
tabela_verdade('bicondicional')
tabela_verdade('xor')