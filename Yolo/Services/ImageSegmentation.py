import streamlit as st
import os
from streamlit_option_menu import option_menu

st.header("Image Segmentation")
st.markdown(
    """
    <h3 style='text-align: center; color: #FF6347; font-weight: bold;'>
    **By following these beside steps one by one, train your own model**
    </h3>
    """, unsafe_allow_html=True
)

current_dir = os.path.dirname(__file__)

Segmentation_img_path = os.path.join(current_dir, "media/images/onboarding-iseg.png")
# Sidebar navigation menu for steps in Image Segmentation

selected = option_menu(
    menu_title="Image Segmentation Steps",  # Required
    options=["Introduction", "Data Collection & Preparation", "Model Defining", "Training", "Testing"],  # Steps
    icons=["book", "database", "brain", "play", "check-circle"],  # Icons for each step
    menu_icon="menu",  # Sidebar icon
    default_index=0,  # Initially selected option
    orientation="horizontal",  # Sidebar vertical orientation
)


# Introduction Step
if selected == "Introduction":

    st.title("Introduction to Image Segmentation")
    st.subheader("What is Image Segmentation?")
    # Introduction section with one mini paragraph
    st.write("""
        Image segmentation is a more detailed task than object detection, where the goal is to classify each pixel in an image 
        into different categories. This process divides an image into regions for finer analysis, making it highly useful in fields 
        like medical imaging and autonomous driving.
    """)

    # Display the image
    st.image(Segmentation_img_path, caption="Example of Image Segmentation", width=600)

    # Two medium paragraphs
    st.write("""
        Image segmentation can be of two types: semantic segmentation, where objects of the same category are segmented as one, 
        and instance segmentation, where each object is segmented separately. Models like U-Net and Mask R-CNN are widely used for 
        this task, delivering pixel-level precision.

        Segmentation allows for a deeper understanding of image content, which is essential in industries such as healthcare for 
        identifying tumors in medical scans, autonomous vehicles for road understanding, and agriculture for identifying crops in aerial images.
    """)

# Data Collection & Preparation Step
elif selected == "Data Collection & Preparation":
    st.title("Data Collection & Preparation")
    st.subheader("Step 1: Data Collection")
    st.write("""
        Data collection involves gathering a dataset of images that require segmentation. 
        This dataset typically consists of images paired with their corresponding masks or ground truths.
    """)
    
    st.subheader("Step 2: Data Preparation")
    st.write("""
        Data preparation includes cleaning and organizing the dataset, converting images into a suitable format, 
        and splitting the data into training and validation sets.
    """)
    
    st.image("https://example.com/data-preparation-image.jpg", caption="Data Preparation Example", width=600)  # Replace with actual image path

# Model Defining Step
elif selected == "Model Defining":
    st.title("Model Defining")
    st.subheader("Step 3: Defining the Model")
    st.write("""
        Model defining involves selecting and building a neural network architecture specifically designed for segmentation tasks. 
        Common architectures include U-Net, Mask R-CNN, and DeepLab.
    """)
    
    st.image("https://example.com/model-architecture-image.jpg", caption="Segmentation Model Architecture", width=600)  # Replace with actual image path

# Training Step
elif selected == "Training":
    st.title("Training the Model")
    st.subheader("Step 4: Training")
    st.write("""
        During training, the model learns to predict segmentation masks from images. 
        This involves using loss functions like Dice loss or cross-entropy loss to optimize model parameters.
    """)
    
    st.image("https://example.com/training-process-image.jpg", caption="Training Process", width=600)  # Replace with actual image path

# Testing Step
elif selected == "Testing":
    st.title("Testing the Model")
    st.subheader("Step 5: Testing")
    st.write("""
        After training, the model is evaluated on a test dataset to measure its segmentation accuracy. 
        Metrics like Intersection over Union (IoU) and pixel accuracy are commonly used.
    """)
    
    st.image("https://example.com/testing-results-image.jpg", caption="Testing the Model", width=600)  # Replace with actual image path

# Main entry point
if __name__ == "__main__":
    pass
