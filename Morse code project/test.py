import pyttsx3

# 1. Initialize the speech engine
engine = pyttsx3.init()

# Optional: Change voice properties (Speed and Volume)
engine.setProperty('rate', 150)    # Speed (default is usually 200)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# 2. The text you want to speak
text = "Hello! I am ready to convert your text into speech."

# 3. Queue the text and run the engine
engine.say(text)
engine.runAndWait()