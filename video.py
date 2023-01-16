import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
org_out = cv2.VideoWriter('my_video.avi', fourcc, 20.0, (640,480))

while True:
	_,frame = cap.read()
	cv2.imshow('video',frame)
	org.out.write(frame)
	if cv2.waitKey(1) and 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()