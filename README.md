# 🎵 AI Music Composer 🎶

This project trains a Neural Network (NN) to generate piano compositions in real time based on user input. The system processes MIDI files, which combine audio and symbolic music data, to create new compositions dynamically.

## 🚀 Tech Stack
- **Frontend:** React + TypeScript
- **Backend:** Python

## 📂 Dataset
The project utilizes the **MAESTRO Dataset** 🎼, a rich collection of classical piano music data, including both MIDI and audio files. This dataset enables the model to learn intricate musical patterns and generate realistic compositions.

## 🤖 Model: Generative Adversarial Network (GAN)
A **Generative Adversarial Network (GAN)** is used to generate the compositions. GANs consist of two competing neural networks:

1. **🎹 Generator:** Creates new musical compositions.
2. **🕵️‍♂️ Discriminator:** Tries to distinguish between real and generated compositions.

Over time, the generator improves its ability to create realistic-sounding piano pieces by competing against the discriminator.

## ✨ Features
- 🎶 Real-time piano composition generation.
- 🎼 Input processing through MIDI files.
- 🎵 AI-driven music generation using GANs.

## 🛠️ Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-music-composer.git
   ```
2. Install dependencies for the frontend and backend.
3. Train the GAN model using the MAESTRO dataset.
4. Run the application and generate AI-composed piano music in real time.

## 🔮 Future Improvements
- 📈 Enhance model accuracy with more training data.
- 🧠 Experiment with different architectures (e.g., Transformer-based models).
- ⚡ Optimize real-time composition latency.

**💡 Contributions and feedback are welcome!** 🚀
