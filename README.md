# video_frame_extractor
This Python script uses OpenCV (cv2) to extract frames from a video file at a specified interval and save them as individual image files. Here's a brief explanation of what the code does:

1. The extract_frames function takes three arguments: video_path (the path to the input video file), output_folder (the path where the extracted frames will be saved), and frame_interval (the number of frames to skip before extracting the next frame).

2. The function opens the video file using cv2.VideoCapture, and total_frames is set to the total number of frames in the video.

3. The function then enters a loop to read each frame from the video using cap.read() until it reaches the end of the video.

4. In the loop, it checks if the current frame number (frame_num) is a multiple of frame_interval. If so, it saves the frame as an image file in the specified output_folder. The frame filenames are numbered sequentially, starting from 0000.

5. After processing all frames, the cap (video capture) object is released to free up system resources.

6. In the __name__ == "__main__" block, the script prompts the user to enter the paths to the input video file and the output folder, as well as the frame interval.

7. It then calls the extract_frames function with the provided input and starts the extraction process.

8. Once the extraction is complete, it displays a message indicating that the process is done and also informs the user about the location where the extracted frames have been saved.

9. The script waits for the user to press the Enter key before closing the console.

10. To use the script, you need to have OpenCV installed (pip install opencv-python). Save the script in a .py file and run it in a Python environment.

Please note that the script will extract frames from the video at the specified interval and save them as individual image files in the output folder. The frame filenames will be in the format "frame_0000.jpg", "frame_0001.jpg", and so on.