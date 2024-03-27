import cv2
def display_video_slow_fast(video_path, delay):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def display_slow_motion(video_path):
    display_video_slow_fast(video_path, delay=50)

def display_fast_motion(video_path):
    display_video_slow_fast(video_path, delay=10)

if __name__ == "__main__":
    video_path = 'F:\parthihan\INFINIX\education\physics\Capacitance_Parallel_Plate_Capacitor_Physics 12_Tamil_MurugaMP ( 360 X 640 ).mp4'

    print("Displaying video in slow motion...")
    display_slow_motion(video_path)

    print("Displaying video in fast motion...")
    display_fast_motion(video_path)
