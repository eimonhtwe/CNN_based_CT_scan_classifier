This project is a part of my undergraduate thesis "Analysis and Classification of Lung Cancer Nodules using Convolutional Neural Network".
The objective is to provide an assistance to medical professionals in early detection of lung cancer.
The Iraq-Oncology Teaching Hospital/National Center for Cancer Diseases (IQ-OTH/NCCD) lung cancer dataset  is used. Dataset has three classes : 
normal, benign, and malignant. of these, 40 cases are diagnosed as malignant; 15 cases diagnosed with benign, and 55 cases classified as normal cases. 
kaggle link "https://www.kaggle.com/datasets/adityamahimkar/iqothnccd-lung-cancer-dataset"
Develop custom CNN classification models with differnt layers and compared the performance wiht pre-trained VGG-16 model.
Two custom CNN models are developed. Model 1 is with one convolutional layer and trained model for 10, 20 and 30 iterations.
For CNN model2, two layers of convolutional are designed and L2 Regularization and Dropout are added to prevent from overfitting. 
Pre-traned VGG-16 model with 'Imagenet' weights are used to trained for and evaluated the model performance.
In model evaluation, custom CNN model 2 with L2 regularization shows the best performance so it was deployed using Streamlit.

<img width="675" height="686" alt="image" src="https://github.com/user-attachments/assets/b3d3c94d-3c72-4d7c-9bcd-ba7156385659" />

<img width="1665" height="762" alt="image" src="https://github.com/user-attachments/assets/0c19a8d8-bf73-47e1-8866-ef0a4eaf8ee1" />
