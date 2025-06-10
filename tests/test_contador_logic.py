from meu_modulo.contador_logic import atualizar_contagem

def test_entrada_sucesso():
    line_y = 100
    ids_cruzaram = {'pessoa_1': 90}  

    nova_entrada, nova_saida = atualizar_contagem('pessoa_1', 110, line_y, ids_cruzaram)

    assert nova_entrada == 1
    assert nova_saida == 0
    assert ids_cruzaram['pessoa_1'] == 110

def test_saida_sucesso():
    line_y = 100
    ids_cruzaram = {'pessoa_1': 110}

    nova_entrada, nova_saida = atualizar_contagem('pessoa_1', 90, line_y, ids_cruzaram)

    assert nova_entrada == 0
    assert nova_saida == 1
    assert ids_cruzaram['pessoa_1'] == 90

def test_sem_cruzamento():
    line_y = 100
    ids_cruzaram = {'pessoa_1': 50} 

    nova_entrada, nova_saida = atualizar_contagem('pessoa_1', 60, line_y, ids_cruzaram)

    assert nova_entrada == 0
    assert nova_saida == 0

def test_primeira_aparicao():
    line_y = 100
    ids_cruzaram = {} 

    nova_entrada, nova_saida = atualizar_contagem('pessoa_1', 50, line_y, ids_cruzaram)

    assert nova_entrada == 0
    assert nova_saida == 0
    assert 'pessoa_1' in ids_cruzaram
    assert ids_cruzaram['pessoa_1'] == 50