import cv2
from ultralytics import YOLO
import os
import numpy as np                 
import matplotlib.pyplot as plt    
import seaborn as sns            
model = YOLO('yolov8n.pt')


video_path = 'partida.mp4'

print(f"Tentando abrir o vídeo em: {video_path}")
if not os.path.exists(video_path):
    print(f"--- ERRO ---")
    print(f"O arquivo '{video_path}' NÃO FOI ENCONTRADO.")
    print(f"Verifique se o nome está correto e se ele está na MESMA PASTA do script.")
    print(f"Local atual do script: {os.getcwd()}")
    exit()

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"--- ERRO ---")
    print(f"O OpenCV NÃO CONSEGUIU ABRIR o vídeo: '{video_path}'.")
    print("Isso pode ser um problema de codec de vídeo (formato) ou permissão.")
    print("Tente usar outro vídeo ou converter este para .mp4 padrão.")
    exit() 
else:
    print(">>> Vídeo aberto com sucesso! Iniciando processamento...")


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

output_path = 'partida_detectada.mp4'
output_width = int(frame_width * 0.5)
output_height = int(frame_height * 0.5)
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec para .mp4
out = cv2.VideoWriter(output_path, fourcc, fps, (output_width, output_height))

print(f"O vídeo processado será salvo em: {output_path}")

frame_count = 0


while cap.isOpened():
    success, frame = cap.read()

    if success:
        frame_count += 1 

      
        original_height, original_width, _ = frame.shape
        target_width = 640
        ratio = target_width / original_width
        target_height = int(original_height * ratio)
        
        resized_frame = cv2.resize(frame, (target_width, target_height))
        
        results = model(resized_frame, conf=0.5, classes=[0, 32])
        
       
        annotated_frame = resized_frame 

        for box in results[0].boxes:
   
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            

            class_name = model.names[cls_id]

        
            color = (0, 0, 0) 
            if class_name == 'person':
                color = (255, 0, 0) 
            elif class_name == 'sports ball':
                color = (0, 0, 255) 

            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

            label = f'{class_name} {conf:.2f}'

            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.imshow("FUTVIEW", annotated_frame) 

        
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Tecla 'q' pressionada. Encerrando...")
            break
    else:
       
        print("Fim do vídeo.")
        break

# --- 8. Limpeza ---
print("Liberando recursos...")
out.release() 
cv2.destroyAllWindows()

print("--- Processamento Concluído ---")
print(f"Total de frames processados: {frame_count}")
print(f"Vídeo salvo em '{output_path}'")

import cv2
from ultralytics import YOLO
import os
from collections import defaultdict 

model = YOLO('yolov8n.pt')


video_path = 'partida.mp4'
if not os.path.exists(video_path):
    print(f"--- ERRO --- O arquivo '{video_path}' NÃO FOI ENCONTRADO.")
    exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"--- ERRO --- O OpenCV NÃO CONSEGUIU ABRIR o vídeo: '{video_path}'.")
    exit()


track_history = defaultdict(lambda: [])

print(">>> Processando vídeo com RASTREAMENTO. Pressione 'q' para sair...")

while cap.isOpened():
    success, frame = cap.read()

    if success:
       
        results = model.track(frame, persist=True, conf=0.5, classes=[0, 32]) # Só rastreia pessoas e bola

        
        if results[0].boxes.id is not None:

            boxes = results[0].boxes.xyxy.cpu().numpy()
            track_ids = results[0].boxes.id.cpu().numpy().astype(int)

           
            for box, track_id in zip(boxes, track_ids):
               
                x_center = (box[0] + box[2]) / 2
                y_bottom = box[3]
                point = (int(x_center), int(y_bottom))
           
                track_history[track_id].append(point)

       
        annotated_frame = results[0].plot()

       
        for track_id, points in track_history.items():
            
            for i in range(1, len(points)):
                cv2.line(annotated_frame, points[i - 1], points[i], (0, 255, 0), 2) # Linha verde


        height, width, _ = annotated_frame.shape
        small_frame = cv2.resize(annotated_frame, (int(width * 0.5), int(height * 0.5)))
        
        cv2.imshow("FUTVIEW RASTREAMENTO)", small_frame) 

        # --- 7. Sair do Loop ---
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# --- 8. Limpeza ---
cap.release()
cv2.destroyAllWindows()

print("--- Processamento Concluído ---")
print("Histórico de rastreamento foi capturado.")

# (Opcional) Mostra os dados de um jogador (ex: o primeiro ID que apareceu)
if track_history:
    first_tracked_id = list(track_history.keys())[0]
    print(f"Exemplo de dados (ID: {first_tracked_id}):")
    print(track_history[first_tracked_id])

import cv2
from ultralytics import YOLO
import os
from collections import defaultdict
import numpy as np                 # NOVO: Para manipulação de dados
import matplotlib.pyplot as plt    
import seaborn as sns              

# --- 1. Carregar o Modelo ---
model = YOLO('yolov8n.pt')

# --- 2. Abrir o Vídeo ---
video_path = 'partida.mp4'
if not os.path.exists(video_path):
    print(f"--- ERRO --- O arquivo '{video_path}' NÃO FOI ENCONTRADO.")
    exit()

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"--- ERRO --- O OpenCV NÃO CONSEGUIU ABRIR o vídeo: '{video_path}'.")
    exit()

# --- NOVO: Variáveis para o Heatmap ---
track_history = defaultdict(lambda: [])
primeiro_frame = None  # Vamos guardar o primeiro frame para usar de fundo
video_height = 0
video_width = 0

# --- 3. Loop Principal (Frame por Frame) ---
print(">>> Processando vídeo com RASTREAMENTO. Pressione 'q' para sair...")

frame_index = 0 # Contador de frames
while cap.isOpened():
    success, frame = cap.read()
    if success:
        # --- NOVO: Salvar o primeiro frame e as dimensões ---
        if frame_index == 0:
            primeiro_frame = frame.copy() # Salva uma cópia
            video_height, video_width, _ = frame.shape
        frame_index += 1

        # --- 4. Rastreamento ---
        results = model.track(frame, persist=True, conf=0.5, classes=[0]) # Só rastreia pessoas

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            track_ids = results[0].boxes.id.cpu().numpy().astype(int)

            for box, track_id in zip(boxes, track_ids):
                x_center = (box[0] + box[2]) / 2
                y_bottom = box[3]
                point = (int(x_center), int(y_bottom))
                track_history[track_id].append(point)

        # --- 5. Desenhar Resultados no Vídeo ---
        annotated_frame = results[0].plot()
        
        # (Opcional) Desenhar o rastro no vídeo
        for track_id, points in track_history.items():
            for i in range(1, len(points)):
                cv2.line(annotated_frame, points[i - 1], points[i], (0, 255, 0), 2)

        # --- 6. Mostrar o Vídeo ---
        small_frame = cv2.resize(annotated_frame, (int(video_width * 0.5), int(video_height * 0.5)))
        cv2.imshow("FUTVIEW RASTREAMENTO", small_frame)

        # --- 7. Sair do Loop ---
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# --- 8. Limpeza (Libera o vídeo e fecha as janelas) ---
cap.release()
cv2.destroyAllWindows()
print("--- Processamento de vídeo Concluído ---")

# --- 9. NOVO: Gerar o Heatmap ---
print(">>> Gerando Heatmap...")

if not track_history or primeiro_frame is None:
    print("Não foram capturados dados suficientes para gerar o heatmap.")
else:
    # Criar listas para todos os pontos x e y de todos os jogadores
    all_x_points = []
    all_y_points = []
    
    for track_id, points in track_history.items():
        # Filtro opcional: ignora rastros muito curtos (ex: menos de 10 pontos)
        if len(points) < 10:
            continue
            
        for point in points:
            all_x_points.append(point[0]) # Adiciona o x
            all_y_points.append(point[1]) # Adiciona o y

    if not all_x_points:
        print("Nenhum rastro longo o suficiente foi encontrado.")
    else:
        
        plt.figure(figsize=(video_width / 100, video_height / 100)) 

        sns.kdeplot(
            x=all_x_points, 
            y=all_y_points, 
            cmap="rocket_r", 
            fill=True, 
            thresh=0.05, 
            alpha=0.6
        )
       
        plt.imshow(cv2.cvtColor(primeiro_frame, cv2.COLOR_BGR2RGB), extent=[0, video_width, video_height, 0])

        plt.title("Heatmap de Posição dos Jogadores")
        plt.xlabel("Posição X (pixel)")
        plt.ylabel("Posição Y (pixel)")
        plt.xlim(0, video_width)   
        plt.ylim(video_height, 0)  
        plt.axis('off') 
        
        output_filename = "heatmap_final.png"
        plt.savefig(output_filename, dpi=150, bbox_inches='tight', pad_inches=0)
        
        print(f"--- Sucesso! Heatmap salvo como '{output_filename}' ---")
        
        plt.show()    