import cv2

def extract_frames(video_path, output_folder, frame_interval):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    frame_num = 0
    extracted_frames = 0

    while frame_num < total_frames:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_num % frame_interval == 0:
            frame_filename = f"{output_folder}/frame_{extracted_frames:04d}.jpg"
            cv2.imwrite(frame_filename, frame)
            extracted_frames += 1

        frame_num += 1

    cap.release()

if __name__ == "__main__":
    video_path = input("Enter the path to your video file: ")
    output_folder = input("Enter the path to output video file: ")
    frame_interval = int(input("Enter the frame interval: "))
    print("Proccesing. . .")
    extract_frames(video_path, output_folder, frame_interval)
    print("Done. The output was saved in: " + output_folder)
    print("Press enter key to close console")
    input()

    
