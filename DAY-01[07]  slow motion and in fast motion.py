import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(cap.get(cv2.CAP_PROP_FPS))
output_path = "F:\parthihan\INFINIX\education\physics\Effect_Dielectrics_Capacitors_Battery_Disconnected_Physics 12_Tamil_MurugaMP ( 360 X 640 ).mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

output = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    cv2.imshow("frame", frame)

    output.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
output.release()
cv2.destroyAllWindows()
