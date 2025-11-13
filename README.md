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
