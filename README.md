# 👁️ Cataract Detection Using Deep Learning (Fundus + Naked Eye Imaging)

## 🧠 Problem Statement
Cataract is one of the leading causes of vision loss globally. Early detection can help reduce irreversible blindness. This project aims to automate cataract detection using deep learning models on **fundus images** and **real-time naked eye images**, reducing dependency on manual diagnosis.

---

## 🎯 Objective
To build a robust, real-time cataract detection system using computer vision and deep learning techniques. This system leverages CNN architectures to classify images as *cataract* or *normal*, enabling screening with minimal equipment.

---

## 🛠️ Technologies Used
- **Python 3**
- **TensorFlow**, **Keras** – for building deep learning models (CNN, DCNN)
- **OpenCV** – for image preprocessing
- **Flask** – to deploy as a web application
- **NumPy**, **Matplotlib**, **Pandas** – for data handling and visualization

---

## 📁 Project Structure

cataract_Detection/
- **├──dataset/ #kaggle naked eye images,Fundus images**
- **├── models/ # .pkl**
- **├── app.py # Flask**
- **├── train_model.py # phase1_using_ODIR.ipynb for ODIR and naked_eye.ipynb for naked eye images**
- **├── utils.py #**
- **├── templates/ # HTML frontend**
- **├── static/ # CSS/images used in Flask app**
- **├── README.md # Project documentation**
- **└── requirements.txt # Python dependencies**

  ---

  
---

## 🚀 How to Run

### 1.Clone the Repository
```bash
git clone https://https://github.com/subba5076/Cataract_Detection_.git
cd Cataract_Detection_
```


### 2.Install Requirnments
```bash
pip install -r requirements.txt
```
### 3.Run the Flask App
```bash
python app.py
```

---

### 🔬 How It Works
Input image is uploaded through the web interface (either fundus or naked eye photo).

The image is preprocessed (resized, normalized).

It is passed through a trained CNN model.

The model predicts whether cataract is present or not.

Results are displayed along with confidence score.

### 📊 Results
Achieved high accuracy 96% on benchmark datasets

Handled diverse image sources including real-time webcam photos

Real-time deployment tested using Flask frontend


### 🧠 Future Work

Include multi-class classification for different cataract stages

Explore federated learning for privacy-preserving medical data training

### 📜 Publication
Title: Deep Learning Approaches for Cataract Detection Using Fundus and Real-Time Naked Eye Imaging
Presented at ICRASET 2024
📄 Read on ResearchGate

👨‍💻 Author
Subrahmanya Rajesh Nayak
LinkedIn • GitHub

📜 License
This project is licensed under the MIT License.



---


