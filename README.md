# Price Detection for E-commerce Products Using Deep Learning

For downloading the dataset, use the following dataset on Kaggle: [Mercari Price Suggestion Challenge](https://www.kaggle.com/competitions/mercari-price-suggestion-challenge/data) (Dataset here is imported from Google Drive as the notebook is created in Google Colab).

1. **Comprehensive Data Preprocessing and Transformation:**
   - Designed a comprehensive data preprocessing pipeline to handle missing values, categorical data transformation, tokenization, and sequence generation for text data.
   - Implemented LabelEncoder and Tokenizer for precise management of categorical data and text features, enhancing data quality and feature engineering.

2. **Advanced Model Evaluation and Deployment Readiness:**
   - Achieved an impressive RMSLE of 0.48 with a validation accuracy of 92.5% over 10 epochs, validating the model with train-test splits for high accuracy and generalization.
   - Seamlessly integrated data processing and model training, demonstrating the ability to deploy scalable, real-world machine learning solutions.

3. **Engineered High-Performance Price Detection Model:**
   - Developed a robust price detection model using TensorFlow Keras and pre-trained embeddings, achieving a validation accuracy of 96.5% over 10 epochs.
   - Optimized with GRU layers and dense networks in Keras' functional API, ensuring scalable, high-performance predictions for large-scale e-commerce datasets.

4. **Seamless Model Deployment with Modern Technologies:**
   - **Containerization and Orchestration:** Utilized Docker to containerize the application, ensuring consistent environments for development, testing, and production. Deployed the containerized application using Kubernetes for orchestration, enabling automatic scaling, load balancing, and high availability.
   - **Cloud Platform Integration:** Leveraged Google Cloud Platform (GCP) for robust, scalable infrastructure, utilizing services such as Google Kubernetes Engine (GKE) for deployment, Cloud Storage for dataset handling, and AI Platform for managing machine learning workflows.
   - **Backend and Frontend Integration:** Implemented a Flask-based backend to handle API requests and facilitate communication between the model and the application. Developed a user-friendly HTML frontend to enable easy interaction with the model, providing real-time price suggestions for e-commerce products.
