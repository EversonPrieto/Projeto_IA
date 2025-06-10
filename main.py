import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import argparse

from meu_modulo.contador_logic import atualizar_contagem

VIDEO_PATH_DEFAULT = "istockphoto-1152080347-640_adpp_is.mp4"
MODEL_PATH = "yolov8l.pt"
LINE_Y_DEFAULT = 260
SCORE_THRESHOLD = 0.35
MIN_BOX_AREA = 400

def run_tracker(video_path, line_y, no_display=False, max_frames=None):
    """
    Função principal que executa o rastreador de pessoas e a contagem.
    """
    model = YOLO(MODEL_PATH)
    tracker = DeepSort(max_age=90)
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Erro: Não foi possível abrir o vídeo em {video_path}")
        return

    entradas = 0
    saidas = 0
    ids_cruzaram = {}
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Fim do vídeo ou erro na leitura.")
            break

        results = model(frame, verbose=False)[0]
        detections = []
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            box_w = x2 - x1
            box_h = y2 - y1
            box_area = box_w * box_h
            if (
                int(class_id) == 0 and
                score > SCORE_THRESHOLD and
                box_area > MIN_BOX_AREA
            ):
                detections.append(([x1, y1, box_w, box_h], score, 'person'))

        tracks = tracker.update_tracks(detections, frame=frame)

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            l, t, r, b = track.to_ltrb()
            cy = int((t + b) / 2)

            nova_entrada, nova_saida = atualizar_contagem(track_id, cy, line_y, ids_cruzaram)
            entradas += nova_entrada
            saidas += nova_saida

            if not no_display:
                cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 2)
                cv2.putText(frame, f'ID {track_id}', (int(l), int(t) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if not no_display:
            cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (255, 0, 0), 2)
            cv2.putText(frame, f'Entradas: {entradas}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.putText(frame, f'Saidas: {saidas}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            cv2.imshow("Contador de Pessoas", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        frame_count += 1
        if max_frames and frame_count >= max_frames:
            print(f"Parada automática após processar {max_frames} frames.")
            break

    cap.release()
    if not no_display:
        cv2.destroyAllWindows()
    
    print(f"Processamento finalizado. Total de Entradas: {entradas}, Total de Saídas: {saidas}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Contador de Pessoas com YOLOv8 e DeepSort.")
    parser.add_argument("--video_path", type=str, default=VIDEO_PATH_DEFAULT, help="Caminho para o arquivo de vídeo.")
    parser.add_argument("--line_y", type=int, default=LINE_Y_DEFAULT, help="Posição Y da linha de contagem.")
    parser.add_argument("--no-display", action="store_true", help="Roda o script sem exibir a janela de vídeo.")
    parser.add_argument("--max-frames", type=int, help="Número máximo de frames a processar antes de parar.")
    
    args = parser.parse_args()

    run_tracker(args.video_path, args.line_y, args.no_display, args.max_frames)