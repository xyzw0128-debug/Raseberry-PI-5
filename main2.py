from gpiozero import LED
from time import sleep

carLedRed = 2            # GPIO 2번
carLedYellow = 3         # GPIO 3번
carLedGreen = 4            #GPIO 4번
humanLedRed = 20            #GPIO 20번
humanLedGreen = 21        #GPIO 21번

# gpiozero 라이브러리에 있는 LED 모듈 사용
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)

try:
    while 1:        #무한루프
        # 자동차 초록색, 보행자 빨간색 ON
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        # 3초 대기
        sleep(3.0)
        # 자동차 파란색, 보행자 빨간색 ON
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        # 1초 대기
        sleep(1.0)
        # 자동차 빨간색, 보행자 초록색 ON
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        #3초 대기
        sleep(3.0)
    
except KeyboardInterrupt:
    pass

carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0
