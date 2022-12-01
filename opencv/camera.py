import cv2

# PCのカメラをつかまえる
cam = cv2.VideoCapture(0)

# カメラで、写真をとる
ret, frame = cam.read()

# 写真を表示する
cv2.imshow('camera', frame)

# 写真を保存する
cv2.imwrite('aloha.jpg', frame)

# おわる
key = cv2.waitKey()		# キーを押すまで待つ
cam.release()			# 写真データを捨てる
