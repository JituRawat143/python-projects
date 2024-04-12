import webbrowser
import pyttsx3
import os
import datetime
import time
import re
import asyncio

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to handle user input
def chat():
    print("Chatbot: Hi! How can I help you today?")
    engine.say("Hy! How can I help you today?")
    engine.runAndWait()
    while True:
        user_input = input("You: ").lower()
        if user_input in ["hello","hi","hy", "hii", "hellow"]:
            print("Chatbot: Hey! How can I help you?")
            engine.say("Hey! How can I help you?")
            engine.runAndWait()
        elif "video" in user_input:
            search_youtube(user_input)
        elif user_input == "how are you":
            print(" I'm good and here to assist you with any questions or tasks you have. How can I help you today?")
            engine.say("I'm here to assist you with any questions or tasks you have. How can I help you today?")
            engine.runAndWait()
        elif user_input == "open photos" or user_input == "open my photos" or user_input == "picture" or user_input == "photos" or user_input == "open my gallery" or user_input == "open pictures" or user_input == "my pictures":
            open_photos()
        elif user_input in ["open song","open music","open my music", "play music", "play song"]:
            open_music()
        elif user_input == "calculator" or user_input =="open calculator":
            calculate()
        elif user_input == "reminder":
            asyncio.run(set_reminder())
        elif user_input in ["bye","by","byy","good by"]:
            engine.say("by! have a nice day")
            engine.runAndWait()
            break
        else:
            search_google(user_input)
       

# Function to search YouTube videos
def search_youtube(query):
    query = query.replace("video", "").strip()  
    youtube_url = "https://www.youtube.com/results?search_query=" + "+".join(query.split())
    print("Chatbot: Here are some YouTube videos for you: " + youtube_url)
    engine.say("Here are some YouTube videos for you")
    engine.runAndWait()
   
    webbrowser.open(youtube_url)

# Function to search Google
def search_google(query):
    google_url = "https://www.google.com/search?q=" + query
    print("Chatbot: Let me search that for you on Google.")
    engine.say("Let me search that for you on google")
    engine.runAndWait()
    webbrowser.open(google_url)

# Function to open photos folder
def open_photos():
    folder_path = r"E:\photos"
    if os.path.exists(folder_path):
        os.startfile(folder_path)
        print("Chatbot: plz open only file manager folder.")
        engine.say("plz open your file manager folder and choose the photo")
        engine.runAndWait()
    else:
        print("Chatbot: Sorry, I couldn't find your photos folder.")
        engine.say("Chatbot: Sorry, I couldn't find your photos folder.")     
        engine.runAndWait()

# Function to open music folder
def open_music():
    folder_path = r"E:\New Songs"  
    if os.path.exists(folder_path):
        os.startfile(folder_path)
        engine.say("plz open your file manager folder and choose the song what you want to play")
        engine.runAndWait()
        print("Chatbot: plz open your file manager folder and choose the photo.")
    else:
        print("Chatbot: Sorry, I couldn't find your music folder.")
        engine.say("Chatbot: Sorry, I couldn't find your music folder.")
        engine.runAndWait()

# Function to calculate simple mathematics operation
def calculate():
    print("Chatbot: Please enter an expression to calculate (e.g., '2 + 2')")
    expression = input("You: ")
    try:
        result = eval(expression)
        print("Chatbot: The result is:", result)
        engine.say("The result is " + str(result))
        engine.runAndWait()
    except Exception as e:
        print("Chatbot: Sorry, I couldn't calculate that. Please enter a valid expression.")
        engine.say("Sorry, I couldn't calculate that. Please enter a valid expression.")
        engine.runAndWait()


# Function to set reminder
async def set_reminder():
    while True:
        print("please write in format ")
        print("ex- remind me in 5 minutes")
        engine.say("please write in format")
        engine.runAndWait()
        user_input = input(" Enter reminder time : ")
        reminder_time_text = re.search(r'in\s(\d+)\s(minute|hour)s?', user_input)
        if reminder_time_text:
            reminder_time = int(reminder_time_text.group(1))
            reminder_unit = reminder_time_text.group(2)
            if reminder_unit == 'hour':
                reminder_time *= 60

            engine.say("Please specify a reminder message: ")
            print("please write in format ")
            print("ex- remind i want to go home in 5 minutes")
            engine.say("please write in format")
            engine.runAndWait()
            reminder_message = input("Please specify a reminder message:")
            
            if reminder_message:
                print(f"Chatbot: Reminder set for '{reminder_message}' in {reminder_time * 60} seconds.")
                engine.say("reminder has been set")
                engine.runAndWait()
                await asyncio.sleep(reminder_time * 60)
                print(f"Chatbot: Reminder: {reminder_message}")
                engine.say(f"Reminder: {reminder_message}")
                engine.runAndWait()
                break
            else:
                print("Chatbot: Please specify a reminder message.")
                engine.say(" Please specify a reminder message.")
                engine.runAndWait()
        else:
            print("Chatbot: Please specify a valid reminder time.")
            engine.say(" Please specify a valid reminder time.")
            engine.runAndWait()
  
# Run the chatbot
if __name__ == "__main__":
    chat()
