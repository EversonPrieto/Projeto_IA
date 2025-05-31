import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

VIDEO_PATH = "istockphoto-1152080347-640_adpp_is.mp4" 
MODEL_PATH = "yolov8n.pt"
LINE_Y = 250

model = YOLO(MODEL_PATH)
tracker = DeepSort(max_age=30)
cap = cv2.VideoCapture(VIDEO_PATH)

entradas = 0
saidas = 0
ids_cruzaram = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]
    detections = []

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if int(class_id) == 0:
            detections.append(([x1, y1, x2 - x1, y2 - y1], score, 'person'))

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, r, b = track.to_ltrb()
        cx = int((l + r) / 2)
        cy = int((t + b) / 2)

        if track_id not in ids_cruzaram:
            ids_cruzaram[track_id] = cy
        else:
            y_antigo = ids_cruzaram[track_id]
            if y_antigo < LINE_Y and cy >= LINE_Y:
                entradas += 1
                ids_cruzaram[track_id] = cy
            elif y_antigo > LINE_Y and cy <= LINE_Y:
                saidas += 1
                ids_cruzaram[track_id] = cy

        cv2.rectangle(frame, (int(l), int(t)), (int(r), int(b)), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (int(l), int(t) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.line(frame, (0, LINE_Y), (frame.shape[1], LINE_Y), (255, 0, 0), 2)
    cv2.putText(frame, f'Entradas: {entradas}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    cv2.putText(frame, f'Saídas: {saidas}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    cv2.imshow("Contador de Pessoas", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
