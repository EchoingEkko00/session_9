from gpiozero import LED, Button

led = LED(17)
button = Button(26)

while True:
    print("Relâché.")
    button.wait_for_press()
    print("Pressé.")
    button.wait_for_release()
    
    

