import streamlit as st
import os
from streamlit_option_menu import option_menu

st.header("Image Classification")
st.markdown(
    """
    <h3 style='text-align: center; color: #FF6347; font-weight: bold;'>
    **By following these  beside steps one by one, train your own model**
    </h3>
    """, unsafe_allow_html=True
)
current_dir = os.path.dirname(__file__)

Classification_img_path = os.path.join(current_dir, "media/images/onboarding-classification-v2.png")
# Sidebar navigation menu for steps in Image Classification
selected = option_menu(
    menu_title="Image Classification Steps",  # Required
    options=["Introduction", "Data Collection & Preparation", "Model Defining", "Training", "Testing"],  # Steps
    icons=["book", "database", "brain", "play", "check-circle"],  # Icons for each step
    menu_icon="list",  # Sidebar icon
    default_index=0,  # Initially selected option
    orientation="vertical",  # Sidebar vertical orientation
)
# Introduction Step
if selected == "Introduction":
    st.title("Introduction to Image Classification")
    st.subheader("What is Image Classification?")
    st.write("""
        Image classification is a core task in computer vision where the objective is to assign a label to an image based on its content. 
        This task has widespread applications, from categorizing photos to advanced fields like autonomous driving and medical diagnosis.
    """)

    # Display the image
    st.image(Classification_img_path, caption="Example of Image Classification", width=600)

    # Two medium paragraphs
    st.write("""
        In image classification, models learn patterns in images from labeled data, which helps them recognize and categorize 
        new images into predefined classes. For instance, a model trained on images of animals like cats, dogs, and birds 
        will learn to distinguish between them by identifying unique features like fur texture, color, and shape. 

        Modern image classification models, especially those using deep learning methods like Convolutional Neural Networks (CNNs), 
        have achieved remarkable accuracy by efficiently capturing spatial hierarchies in images. These models are now widely used 
        across industries, and their performance has been significantly boosted by techniques such as transfer learning and data augmentation.
    """)

# Data Collection & Preparation Step
elif selected == "Data Collection & Preparation":
    st.title("Data Collection & Preparation")
    st.subheader("Step 1: Data Collection")
    st.write("""
        Data collection involves gathering a large dataset of labeled images that represent various categories. 
        For example, if you're classifying animals, you'd collect images of cats, dogs, birds, etc.
    """)
    
    st.subheader("Step 2: Data Preparation")
    st.write("""
        Data preparation involves cleaning, labeling, and organizing the dataset. 
        This might include resizing images, augmenting the dataset, and splitting it into training and testing sets.
    """)
    
    st.image("https://example.com/data-preparation-image.jpg", caption="Example of Data Preparation", width=600)  # Replace with actual image path

# Model Defining Step
elif selected == "Model Defining":
    st.title("Model Defining")
    st.subheader("Step 3: Defining the Model")
    st.write("""
        Model defining is the process of selecting and building a neural network architecture that can classify images. 
        Common models used for image classification include CNNs (Convolutional Neural Networks) like ResNet, VGG, etc.
    """)
    
    st.image("https://example.com/model-architecture-image.jpg", caption="Model Architecture", width=600)  # Replace with actual image path

# Training Step
elif selected == "Training":
    st.title("Training the Model")
    st.subheader("Step 4: Training")
    st.write("""
        Training involves feeding the prepared dataset into the model and allowing it to learn from the data by optimizing its weights.
        This step typically uses techniques like gradient descent and backpropagation.
    """)
    
    st.image("https://example.com/training-process-image.jpg", caption="Training Process", width=600)  # Replace with actual image path

# Testing Step
elif selected == "Testing":
    st.title("Testing the Model")
    st.subheader("Step 5: Testing")
    st.write("""
        After training, the model is evaluated on a separate test set to measure its accuracy and generalization. 
        The performance metrics, such as accuracy, precision, recall, and F1 score, are used to assess the model.
    """)
    
    st.image("https://example.com/testing-results-image.jpg", caption="Testing the Model", width=600)  # Replace with actual image path

# Main entry point
if __name__ == "__main__":
    pass
