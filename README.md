⚽ FutView - Football Analysis with YOLO
A computer vision system for football analysis using YOLO object detection to track players and generate heatmaps of field activity.

🎯 Features
Player Detection: Real-time detection of players and sports balls using YOLOv8
Player Tracking: Advanced tracking system to follow player movements throughout the match
Heatmap Generation: Visual representation of player activity zones on the field
Video Processing: Process entire football matches and save annotated videos
Custom Visualization: Color-coded bounding boxes for different object types
📋 Requirements
Python 3.8+
OpenCV
Ultralytics YOLO
NumPy
Matplotlib
Seaborn
🚀 Installation
Clone the repository:
git clone https://github.com/vitoriaayres/futview.git
cd futview
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
pip install opencv-python ultralytics numpy matplotlib seaborn
📁 Project Structure
futview/
│
├── detector.py           # Main detection and analysis script
├── yolov8n.pt           # YOLOv8 model weights
├── campo.jpg            # Football field background image
├── partida.mp4          # Input video file
├── partida_detectada.mp4 # Output video with detections
├── heatmap_final.png    # Generated heatmap
└── README.md            # Project documentation
🎮 Usage
Prepare your data:

Place your football video as partida.mp4
Ensure you have a field background image as campo.jpg
Run the analysis:

python detector.py
Output:
partida_detectada.mp4: Video with player detection boxes
heatmap_final.png: Heatmap showing player activity zones
🔧 How it works
1. Video Processing
Loads the input video frame by frame
Resizes frames for optimal inference speed
Applies YOLO detection with confidence threshold of 0.5
2. Player Tracking
Uses YOLOv8's built-in tracking capabilities
Tracks individual players throughout the match
Records position history for each tracked ID
3. Heatmap Generation
Collects all player positions from tracking data
Filters out short tracking sequences (< 10 points)
Uses Kernel Density Estimation (KDE) to create smooth heatmaps
Overlays heatmap on the football field background
🎨 Visualization Features
Blue boxes: Detected players
Red boxes: Sports balls
Green trails: Player movement paths (in real-time view)
Heatmap: Red zones indicate high activity areas, blue zones indicate low activity
⚙️ Configuration
You can modify detection parameters in detector.py:

conf=0.5: Confidence threshold for detections
classes=[0, 32]: Detect only persons (0) and sports balls (32)
Minimum track length filter for heatmap generation
🤝 Contributing
Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ultralytics for the YOLOv8 model
OpenCV community for computer vision tools
Seaborn for beautiful heatmap visualizations
📞 Contact
Vitória Ayres - @vitoriaayres

Project Link: https://github.com/vitoriaayres/futview


----------------------------PORTUGUêS----------------------------------


⚽ FutView - Análise de Futebol com YOLO
Um sistema de visão computacional para análise de futebol usando detecção de objetos YOLO para rastrear jogadores e gerar mapas de calor da atividade em campo.

🎯 Funcionalidades
Detecção de Jogadores: Detecção em tempo real de jogadores e bolas usando YOLOv8
Rastreamento de Jogadores: Sistema avançado de rastreamento para seguir movimentos dos jogadores durante a partida
Geração de Mapa de Calor: Representação visual das zonas de atividade dos jogadores no campo
Processamento de Vídeo: Processa partidas completas e salva vídeos anotados
Visualização Personalizada: Caixas delimitadoras com códigos de cor para diferentes tipos de objetos
📋 Requisitos
Python 3.8+
OpenCV
Ultralytics YOLO
NumPy
Matplotlib
Seaborn
🚀 Instalação
Clone o repositório:
git clone https://github.com/vitoriaayres/futview.git
cd futview
Crie um ambiente virtual:
python -m venv venv
venv\Scripts\activate  # No Windows
Instale as dependências:
pip install opencv-python ultralytics numpy matplotlib seaborn
📁 Estrutura do Projeto
futview/
│
├── detector.py           # Script principal de detecção e análise
├── yolov8n.pt           # Pesos do modelo YOLOv8
├── campo.jpg            # Imagem de fundo do campo de futebol
├── partida.mp4          # Arquivo de vídeo de entrada
├── partida_detectada.mp4 # Vídeo de saída com detecções
├── heatmap_final.png    # Mapa de calor gerado
├── README.md            # Documentação do projeto (inglês)
└── README_PT.md         # Documentação do projeto (português)
🎮 Como Usar
Prepare seus dados:

Coloque seu vídeo de futebol como partida.mp4
Certifique-se de ter uma imagem de fundo do campo como campo.jpg
Execute a análise:

python detector.py
Saída:
partida_detectada.mp4: Vídeo com caixas de detecção de jogadores
heatmap_final.png: Mapa de calor mostrando zonas de atividade dos jogadores
🔧 Como Funciona
1. Processamento de Vídeo
Carrega o vídeo de entrada quadro por quadro
Redimensiona quadros para velocidade otimizada de inferência
Aplica detecção YOLO com limiar de confiança de 0,5
2. Rastreamento de Jogadores
Usa capacidades de rastreamento integradas do YOLOv8
Rastreia jogadores individuais durante toda a partida
Registra histórico de posições para cada ID rastreado
3. Geração de Mapa de Calor
Coleta todas as posições dos jogadores dos dados de rastreamento
Filtra sequências de rastreamento curtas (< 10 pontos)
Usa Estimação de Densidade de Kernel (KDE) para criar mapas de calor suaves
Sobrepõe o mapa de calor no fundo do campo de futebol
🎨 Recursos de Visualização
Caixas azuis: Jogadores detectados
Caixas vermelhas: Bolas esportivas
Trilhas verdes: Caminhos de movimento dos jogadores (na visualização em tempo real)
Mapa de calor: Zonas vermelhas indicam áreas de alta atividade, zonas azuis indicam baixa atividade
⚙️ Configuração
Você pode modificar parâmetros de detecção em detector.py:

conf=0.5: Limiar de confiança para detecções
classes=[0, 32]: Detectar apenas pessoas (0) e bolas esportivas (32)
Filtro de comprimento mínimo de trilha para geração de mapa de calor
🎯 Próximas Funcionalidades
[ ] Análise de formação tática
[ ] Estatísticas de corrida por jogador
[ ] Detecção automática de eventos (gols, faltas, etc.)
[ ] Interface gráfica de usuário
[ ] Exportação de dados em diferentes formatos
🤝 Contribuindo
Faça um fork do repositório
Crie uma branch para sua funcionalidade (git checkout -b feature/funcionalidade-incrivel)
Faça commit das suas mudanças (git commit -m 'Adiciona funcionalidade incrível')
Faça push para a branch (git push origin feature/funcionalidade-incrivel)
Abra um Pull Request
🐛 Problemas Conhecidos
Arquivos de vídeo muito grandes podem causar lentidão no processamento
Condições de iluminação ruins podem afetar a precisão da detecção
O modelo atual é otimizado para câmeras em perspectiva aérea
📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

🙏 Agradecimentos
Ultralytics pelo modelo YOLOv8
Comunidade OpenCV pelas ferramentas de visão computacional
Seaborn pelas belas visualizações de mapas de calor
📞 Contato
Vitória Ayres - @vitoriaayres

Link do Projeto: https://github.com/vitoriaayres/futview

🚀 Começando Rapidamente
Se você quer testar o projeto rapidamente:

Certifique-se de ter Python instalado
Clone o repositório
Instale as dependências: pip install opencv-python ultralytics numpy matplotlib seaborn
Coloque seu vídeo como partida.mp4
Execute: python detector.py
Aguarde o processamento e verifique os resultados!
