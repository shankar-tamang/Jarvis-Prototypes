import speech_recognition as sr



def speech_recognizer():

    recognizer = sr.Recognizer()

    while True:  # Infinite loop for continuous listening
        try:
            with sr.Microphone() as source:
                print("Listening... Speak now.")
                recognizer.adjust_for_ambient_noise(source)  # Adjusts for background noise
                audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            

            # Optional: Break the loop if a specific keyword is spoken
            if "stop" in text.lower():
                print("Stopping...")
                break

            return text

        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error: {e}")
