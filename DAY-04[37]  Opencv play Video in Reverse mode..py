import cv2

# Read the image
image = cv2.imread("F:/Computer Vision/Image/picture5.png")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Get total number of frames (should be 1 for an image)
    total_frames = 1

    # Start from the last frame index
    current_frame = total_frames - 1

    while current_frame >= 0:
        # Read the frame (image)
        frame = image

        # Show the frame
        cv2.imshow('Image in Reverse', frame)

        # Wait for 25ms, if 'q' is pressed break the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        current_frame -= 1

    cv2.destroyAllWindows()
