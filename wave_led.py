import RPi.GPIO as GPIO
import time

def measure(): #거리측정 메소드
  GPIO.output(GPIO_TRIGGER, True) #TRIGGER은 초음파 신호를 보낸다
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time() #시작시간 저장

  while GPIO.input(GPIO_ECHO)==0: #ECHO는 초음파 신호를 받는다
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1: 
    stop = time.time()

  elapsed = stop-start #경과 시간
  distance = (elapsed * 34300)/2

  return distance

def measure_average(): #거리를 3번 측정하고 평균값을 구하는 메소드
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23 #TRIGGER 번호 저장
GPIO_ECHO    = 24 #ECHO 번호 저장 
GPIO_LED     = 18
print("Ultrasonic Measurement")

GPIO.setup(GPIO_LED,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
#TRIGGER을 FALSE로 설정(Low)
GPIO.output(GPIO_TRIGGER, False)

try:

  while True:

    distance = measure_average()
    print("Distance : %.1f" % distance)
    time.sleep(1)

    if distance <=10: #거리가 10cm 가까이면 LED가 켜지고
    print("LED_ON!")
    GPIO.output(GPIO_LED, GPIO.HIGH)
    else :
    print("LED_OFF") #거리가 10cm 밖이면 LED가 꺼진다
    GPIO.output(GPIO_LED, GPIO.LOW)

except KeyboardInterrupt:
  GPIO.cleanup()