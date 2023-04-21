import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 저장할 비디오 파일의 코덱 설정 및 프레임 레이트, 크기 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
frame_size = (int(cap.get(3)), int(cap.get(4)))
out = cv2.VideoWriter('output.mp4', fourcc, fps, frame_size, isColor=True)

# 녹화 여부 초기값 False 설정
is_recording = False

# 화면 뒤집기 여부 초기값 False 설정
is_flipped = False

# 키보드 이벤트 처리 함수
def process_key_event(key):
    global is_recording, is_flipped

    # 녹화 시작
    if key == ord('r') and not is_recording:
        is_recording = True

    # 녹화 중지
    elif key == ord('s') and is_recording:
        is_recording = False

    # 화면 뒤집기
    elif key == ord('f'):
        is_flipped = not is_flipped

    # 종료
    elif key == ord('q'):
        out.release()
        cv2.destroyAllWindows()
        quit()

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 화면 뒤집기
    if is_flipped:
        frame = cv2.flip(frame, 0)

    # 녹화 중일 때 프레임 저장
    if is_recording:
        out.write(frame)

    # 녹화 중일 때 빨간색 텍스트로 'REC' 추가
    if is_recording:
        cv2.putText(frame, 'REC', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    # 녹화 중이 아닐 때 녹화 시작을 위한 텍스트 추가
    else:
        cv2.putText(frame, 'Press "r" to start recording', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    # 화면에 프레임 출력
    cv2.imshow('Recording', frame)

    # 키보드 이벤트 대기
    key = cv2.waitKey(1)

    # 키 이벤트 처리
    process_key_event(key)
