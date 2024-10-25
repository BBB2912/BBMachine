import streamlit as st
import cv2
import numpy as np
from io import BytesIO



# Function to capture video from webcam
def video_capture(frame_size,camera_index):
    cap = cv2.VideoCapture(camera_index)  # Open the webcam
    while True:
        ret, frame = cap.read()  # Read a frame from the webcam
        if not ret:
            break
        # Resize frame based on the user-specified frame size
        frame = cv2.resize(frame, frame_size)
        # Convert the frame from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Yield the frame to the Streamlit app
        yield frame
    cap.release()  # Release the webcam

# Streamlit method to collect image classification data
def imageclassification_data():


    # Initialize session state for labels, collected data, frame counts, capture toggle, and button state
    if 'labels' not in st.session_state:
        st.session_state.labels = []
    if 'collected_data' not in st.session_state:
        st.session_state.collected_data = {}  # Nested list to store frames for each label
    if 'frame_counts' not in st.session_state:
        st.session_state.frame_counts = {}  # Track frame counts for each label
    if 'capture' not in st.session_state:
        st.session_state.capture = False  # Toggle for capturing frames
    if 'completed_labels' not in st.session_state:
        st.session_state.completed_labels = set()  # Track labels that have completed frame capture

    # Step 1: Enter labels for classification
    label_input = st.text_input("Enter labels for classification (comma-separated):")
    
    # Add labels to session state when "Add Labels" button is clicked
    if st.button("Add Labels"):
        if label_input:
            new_labels = label_input.split(",")
            # Add new labels to session state
            st.session_state.labels.extend([label.strip() for label in new_labels])
            st.session_state.labels = list(set(st.session_state.labels))  # Remove duplicates
            st.success(f"Labels added: {', '.join(st.session_state.labels)}")

            # Initialize nested lists for new labels (one per label)
            for label in st.session_state.labels:
                st.session_state.collected_data[label] = []
                st.session_state.frame_counts[label] = 0  # Initialize frame counts

    # Display the list of labels
    if st.session_state.labels:
        st.write(f"Current Labels: {', '.join(st.session_state.labels)}")

        # Step 2: Specify the number of frames to collect for each label
        frame_goal = st.number_input("Enter number of frames to collect for each label:", min_value=1, value=10, step=1)
        camera_index = st.number_input("Camera Index:", min_value=0,max_value=3, value=0, step=1)

        # Step 3: Input fields for frame width and height
        col1, col2 = st.columns(2)
        with col1:
            frame_width = st.text_input("Enter Frame Width:", "640")
        with col2:
            frame_height = st.text_input("Enter Frame Height:", "480")

        # Validate the frame size input
        try:
            frame_size = (int(frame_width), int(frame_height))
        except ValueError:
            st.error("Please enter valid integer values for width and height!")
            return

        # Step 4: Select label for capturing data
        label_selection = st.selectbox("Select label for this session:", [label for label in st.session_state.labels if label not in st.session_state.completed_labels])
        
        # Start capturing frames when button is clicked
        if st.button("Start Capture"):
            st.session_state.capture = True
        
        stframe = st.empty()  # Frame placeholder
        video_stream = video_capture(frame_size,camera_index)  # Initialize video stream

        # Loop through video frames
        for frame in video_stream:
            # Display frame
            stframe.image(frame, channels="RGB", use_column_width=True)

            # Capture frames if toggle is ON and frame count is below goal
            if st.session_state.capture and st.session_state.frame_counts[label_selection] < frame_goal:
                st.session_state.collected_data[label_selection].append(frame)
                st.session_state.frame_counts[label_selection] += 1

                # Check if frame goal is met for the current label
                if st.session_state.frame_counts[label_selection] >= frame_goal:
                    st.session_state.capture = False
                    st.session_state.completed_labels.add(label_selection)
                    st.success(f"Completed capturing {frame_goal} frames for label: {label_selection}")

            # Break loop if frame capture is complete for current label
            if not st.session_state.capture:
                break

        # Show download button only after capturing frames for all labels
        if len(st.session_state.completed_labels) == len(st.session_state.labels):
            buffer = BytesIO()
            np.savez(buffer, **{label: np.array(frames) for label, frames in st.session_state.collected_data.items()})
            buffer.seek(0)
            # Provide download link
            st.download_button(
                label="Download Collected Data",
                data=buffer,
                file_name="collected_data.npz",
                mime="application/octet-stream"
            )

# Call the function inside the Streamlit app
if __name__ == "__main__":
    imageclassification_data()
