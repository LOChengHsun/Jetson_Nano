import Jetson.GPIO as GPIO
import time

LED_OUTPUT_Num = 11 # 輸出腳位
LED_OUTPUT2_Num = 15
LED_INPUT_Num = 13 # 輸入腳位
LED_OUPUT_Status = bool(GPIO.LOW) # 輸出給予低電位
LED_OUPUT2_Status = bool(GPIO.HIGH)


GPIO.setmode(GPIO.BOARD) # 設定 BOARD 編號規則程式(指定在電路版上接腳的號碼)
GPIO.setup(LED_OUTPUT_Num, GPIO.OUT, initial = LED_OUPUT_Status) # initial 為針腳設定預設值，設定輸出針腳同時給予低電位
GPIO.setup(LED_OUTPUT2_Num, GPIO.OUT, initial = LED_OUPUT2_Status)
GPIO.setup( LED_INPUT_Num, GPIO.IN ) # 設定輸入針腳
print("LED_OUPUT_Status=" + str(LED_OUPUT_Status))
print("LED_OUPUT2_Status=" + str(LED_OUPUT2_Status))
# setup()語法：GPIO.setup({channel | chan_list}, {GPIO.OUT | GPIO.IN}, [initial= {GPIO.HIGH | GPIO.LOW}])

while True:
    if( GPIO.input(LED_INPUT_Num) ): # input()，當針腳已被設定高低電位時，可以用此函式取得該針腳的當下狀態為何。若偵測輸入為高電位
        time.sleep(1)
                
        LED_OUPUT_Status = not LED_OUPUT_Status # ~：正、負、倒數。輸出電位由低變高        
        LED_OUPUT2_Status = not LED_OUPUT2_Status
        GPIO.output(LED_OUTPUT_Num, LED_OUPUT_Status) # GPIO.output(channel,GPIO.HIGH)，輸出腳位變高電位
        GPIO.output(LED_OUTPUT2_Num, LED_OUPUT2_Status)

        print ("LED_OUPUT_Status=" + str(LED_OUPUT_Status))
        print ("LED_OUPUT2_Status=" + str(LED_OUPUT2_Status))

        
#    if( GPIO.input(LED_INPUT_Num) ):
#        LED_OUPUT2_Status = ~LED_OUPUT2_Status
#        GPIO.output(LED_OUTPUT2_Num, LED_OUPUT2_Status) 
#        time.sleep(0.001)

#LED_OUTPUT2_Num = 19 # 輸出腳位
#LED_OUPUT2_Status = GPIO.HIGH
#GPIO.setup(LED_OUTPUT2_Num, GPIO.OUT, initial = LED_OUPUT2_Status)
#LED_OUPUT2_Status = ~LED_OUPUT2_Status
#GPIO.output(LED_OUTPUT2_Num, LED_OUPUT2_Status)
#    else(GPIO.input(LED_OUPUT_Num)):
#        LED_OUPUT_Status = ~LED_OUPUT_Status 
#        GPIO.output(LED_OUTPUT_Num, LED_OUPUT_Status) 
#        time.sleep(0.001)
#        
