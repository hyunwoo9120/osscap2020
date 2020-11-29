import start_ui
import playRacing_test
import gameOver_ui
import keyboard
import time
while True:

    
    # TODO: 시작화면
        # 시작화면을 띄우고
        # o 입력 시 소리 on off
        # 엔터 입력 시 사용자의 이름 입력받기
        # 입력받은 사용자의 이름을 저장
    
    username, sound_on = start_ui.start()
    username = username.upper()
    
    # 게임 시작
    # TODO: 게임화면
        # 게임 진행
        # HP가 0 이하인 경우 게임을 종료
        # 종료 시 score를 리턴
    score = playRacing_test.play(sound_on)




    # 이름과 score를 ranking에 기록, ranking 계산
    # 사용자의 이름과 score, ranking 종료화면으로 넘겨줌
    



    # TODO: 종료화면
        # 인자로 받은 이름과 score, ranking을 화면에 출력
        # 엔터 입력 시 시작화면으로 돌아가기
        # q 입력 시 루틴을 끝내고 종료

    result = gameOver_ui.end(username, score)
    if result == "again":
        continue
    if result=="quit":
        break