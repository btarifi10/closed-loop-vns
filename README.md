# Closed-Loop Vagus Nerve Stimulation (VNS) Machine Learning Models
__Basheq Tarifi__

This repository focuses on the machine learning aspects of developing closed-loop vagus nerve stimulation systems using in silico data. The datasets generated from the [vns-ascent-models](https://github.com/btarifi10/vns-ascent-models) repository powers these machine learning models, which aim to predict optimal stimulation parameters and nerve activation levels.

🤖 Key Features:
* Neural network models trained on in silico data for VNS parameter estimation and activation level prediction.
* Comprehensive investigation into multi-parameter and single-parameter estimations.
* Models optimized via a neural network architecture search.
* CNN-based models for compound nerve action potential interpretation.
* Integration with in silico data from [vns-ascent-models](https://github.com/btarifi10/vns-ascent-models).

🌟 Machine Learning Models:
* Amplitude estimation model: Best-performing with a normalised test mean squared error (MSE) of 0.0102.
* Activation level prediction model: Best-performing CNN model achieving a normalized test MSE of 0.0010.
