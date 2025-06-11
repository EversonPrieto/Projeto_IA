def atualizar_contagem(track_id, cy, line_y, ids_cruzaram):
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