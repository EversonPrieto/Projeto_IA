def atualizar_contagem(track_id, cy, line_y, ids_cruzaram):
    """
    Processa a posição de um objeto rastreado e determina se houve cruzamento.

    Args:
        track_id (str): O ID do objeto rastreado.
        cy (int): A coordenada Y atual do centro do objeto.
        line_y (int): A coordenada Y da linha de contagem.
        ids_cruzaram (dict): Dicionário que armazena a última posição Y de cada ID.

    Returns:
        tuple[int, int]: Uma tupla contendo (novas_entradas, novas_saidas).
                         Os valores serão 1 ou 0.
    """
    nova_entrada = 0
    nova_saida = 0

    if track_id not in ids_cruzaram:
        ids_cruzaram[track_id] = cy
    else:
        y_antigo = ids_cruzaram[track_id]

        if y_antigo < line_y and cy >= line_y:
            nova_entrada = 1
        
        elif y_antigo > line_y and cy <= line_y:
            nova_saida = 1
        
        ids_cruzaram[track_id] = cy
            
    return (nova_entrada, nova_saida)