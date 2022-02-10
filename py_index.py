# The following code will work only if you have pyttsx3 installed
# You can install it just by putting "pip instalal pyttsx3" command in your terminal
import pyttsx3
speaker = pyttsx3.init()
speaker.setProperty('rate', 100)
speaker.say("Hey, it's Muntaha again")
speaker.say("I've always loved this poem as a kid")
speaker.say("The itsy bitsy spider climbed up the waterspout")
speaker.say("Down come the rain")
speaker.say("and washed the spider out")
speaker.say("Out came the sun")
speaker.say("and dried up all the rain")
speaker.say("and the itsy bitsy spider climbed up the spout again.")
speaker.runAndWait()