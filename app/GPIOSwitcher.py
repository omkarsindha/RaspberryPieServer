import RPi.GPIO as GPIO
import threading
import time


class GPIOSwitcher:
    RELAY_PIN_1 = 12
    RELAY_PIN_2 = 13

    toggle1_thread = None
    toggle1_thread_running = False
    toggle1_time = time.time()

    toggle2_thread = None
    toggle2_thread_running = False
    toggle2_time = time.time()

    @classmethod
    def setup(cls):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(cls.RELAY_PIN_1, GPIO.OUT)
        GPIO.setup(cls.RELAY_PIN_2, GPIO.OUT)

    @classmethod
    def toggle_gpio(cls, delay, ref):
        if ref == 1:
            while cls.toggle1_thread_running:
                GPIO.output(cls.RELAY_PIN_1, GPIO.HIGH)
                
                time.sleep(delay)
                
                if cls.toggle1_thread_running == False:
                    break;           
                
                GPIO.output(cls.RELAY_PIN_1, GPIO.LOW)
                time.sleep(delay)
                
        if ref == 2:
            while cls.toggle2_thread_running:
                GPIO.output(cls.RELAY_PIN_2, GPIO.HIGH)
                time.sleep(delay)
                
                if cls.toggle2_thread_running == False:
                    break;
                
                GPIO.output(cls.RELAY_PIN_2, GPIO.LOW)

                time.sleep(delay)

    @classmethod
    def start(cls, delay, ref):
        if ref == 1:
            if not cls.toggle1_thread_running:
                cls.toggle1_thread_running = True
                cls.toggle1_thread = threading.Thread(target=cls.toggle_gpio, args=(delay,ref))
                cls.toggle1_thread.start()
                cls.toggle1_time = time.time()
        if ref == 2:
            if not cls.toggle2_thread_running:
                cls.toggle2_thread_running = True
                cls.toggle2_thread = threading.Thread(target=cls.toggle_gpio, args=(delay,ref))
                cls.toggle2_thread.start()
                cls.toggle2_time = time.time()

    @classmethod
    def stop(cls, ref):
        if ref == 1:
            if cls.toggle1_thread_running:
                cls.toggle1_thread_running = False
                cls.toggle1_thread.join()
                cls.toggle1_time = time.time()
        if ref == 2:
            if cls.toggle2_thread_running:
                cls.toggle2_thread_running = False
                cls.toggle2_thread.join()
                cls.toggle2_time = time.time()
              

    @classmethod
    def cleanup(cls):
        GPIO.cleanup()
        
    
    @classmethod
    def get_status(cls):
        ref1 = ""
        ref2 = ""
        ref1_time = ""
        ref2_time = ""

        active1 = cls.toggle1_thread_running
        active2 = cls.toggle2_thread_running

        if active1:
            ref1 = "active"
        else:
            pin1 = GPIO.input(cls.RELAY_PIN_1)
            if pin1 == GPIO.HIGH:
                ref1 = "open"
            else:
                ref1 = "close"

        if active2:
            ref2 = "active"
        else:
            pin2 = GPIO.input(cls.RELAY_PIN_2)
            if pin2 == GPIO.HIGH:
                ref2 = "open"
            else:
                ref2 = "close"
                
        
        ref1_time = cls.get_time(cls.toggle1_time)
        ref2_time = cls.get_time(cls.toggle2_time)
        

        return ref1, ref2, ref1_time, ref2_time
    
    @classmethod
    def get_time(cls, toggle_time):
        current_time = time.time()
        time_diff = current_time - toggle_time
        if time_diff < 60:
            seconds = int(time_diff)
            ref_time = f"{seconds} seconds"
        elif time_diff < 3600:
            minutes = int(time_diff // 60)
            ref_time = f"{minutes} minutes"
        elif time_diff < 86400:
            hours = int(time_diff // 3600)
            ref_time = f"{hours} hours"
        else:
            days = time_diff // 86400
            ref_time = f"{days} days"
        return ref_time
        
