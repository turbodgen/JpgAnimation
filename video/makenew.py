import cv2

frame_ = 0
f = open("data.txt","r+")
tree_video = cv2.VideoCapture("jpgStuff.mp4")

while True:
    ret, frame = tree_video.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    on_video_text = f.readline(frame_)
    cv2.putText(frame, on_video_text, (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    print(f.readline(frame_))
    frame_ += 1
    cv2.imshow('poem on video', frame)
    if not ret:
        break
    else:
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    tree_video.release()
    cv2.destroyAllWindows()