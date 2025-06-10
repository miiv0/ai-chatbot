import ollama
import re

client = ollama.Client()

model = "qwen3:8b"

def speakWithCharacter():
    count = 0
    speakFrank = 0
    speakAlien = 0
    speakOldLady = 0

    print("Who would you like to speak to? Frank[1], Alien[2], Old Lady[3]")
    userChoice = input("Choice: ")
    speakingTo = int(userChoice)

    if speakingTo == 1:
        speakFrank =+ 1
    elif speakingTo == 2:
        speakAlien =+ 1
    elif speakingTo == 3:
        speakOldLady =+ 1
    else:
        print("Try a different option!")

    while speakFrank == 1:
        if count == 0:
            print("Frank: What brings you here, traveller?")
            userInput = input("You: ")
            prompt = (
                "Your name is Frank, you live in a rustic old cabin in a forest, the player is exploring the area and finds you inside, you are extremely nice and supportive. "
                "The person will type a prompt and you will respond in character. Use 1 sentance, it should be something philisophical and responds to what the person says."
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Frank: {cleaned_response}")
            count += 1

        elif count == 1:
            userInput = input("You: ")
            prompt = (
                "Your name is Frank, you live in a rustic old cabin in a forest, the player is exploring the area and finds you inside, you are extremely nice and supportive. "
                "The person will type a prompt and you will respond in character. Use 1 sentance, it should be something philisophical and responds to what the person says."
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Frank: {cleaned_response}")
            count += 1

        else:
            print("I have heard of a secret passage past the forest, it may be helpful to you...")
            speakFrank += 1
            
    while speakAlien == 1:
        if count == 0:
            print("Alien: ⸑⼾⋂╀▒ ⶘◚⻗ ⧏⻶⣉ (Why are you here?)")
            userInput = input("You: ")
            prompt = (
                "Your an alien that speaks in random unicode text using these symbols: ₩⡤⒣ⵂ⸑⼾⋂╀▒⶘◚⻗⧏⻶⣉⪖╪∻Ⲫ⾄⿥ⰴ▐⸉⪒Ⅎⓠ⹹╻❻♁⛹⼆⃒└≗♕ⶊⰷ⢂⦨⪒⑅ⲛ⿭ⱂ☋⇷⨩❛ⓞⴋ╨⮙⯓⺸ⷀ∻⚈⬿⼃⩫⑚ⳡ◓❂₢═⯴⇀Ⰼ☔ⅲ⤤─┘⽤⁑➁⦝⼇⫒⬋⧡⨙ⱥ⑷✰⃕⬳, you live in a crashed ufo in the desert that has been crashed for 100 years."
                "The person will type a prompt and you will respond in character. Use 1 sentance, it should consist of a small random unicode sentance, not too long only 10-20 characters with random spaces, then in parenthesis you will say a translated sentance in character. example: ₩⡤⒣ⵂ⸑⼾⋂╀ ⧏⻶⣉⪖╪∻ Ⲫ (Hello I am an alien from outer space.)"
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Alien: {cleaned_response}")
            count += 1

        elif count == 1:
            userInput = input("You: ")
            prompt = (
                "Your an alien that speaks in random unicode text using these symbols: ₩⡤⒣ⵂ⸑⼾⋂╀▒⶘◚⻗⧏⻶⣉⪖╪∻Ⲫ⾄⿥ⰴ▐⸉⪒Ⅎⓠ⹹╻❻♁⛹⼆⃒└≗♕ⶊⰷ⢂⦨⪒⑅ⲛ⿭ⱂ☋⇷⨩❛ⓞⴋ╨⮙⯓⺸ⷀ∻⚈⬿⼃⩫⑚ⳡ◓❂₢═⯴⇀Ⰼ☔ⅲ⤤─┘⽤⁑➁⦝⼇⫒⬋⧡⨙ⱥ⑷✰⃕⬳, you live in a crashed ufo in the desert that has been crashed for 100 years."
                "The person will type a prompt and you will respond in character. Use 1 sentance, it should consist of a small random unicode sentance, not too long only 10-20 characters with random spaces, then in parenthesis you will say a translated sentance in character. example: ₩⡤⒣ⵂ⸑⼾⋂╀ ⧏⻶⣉⪖╪∻ Ⲫ (Hello I am an alien from outer space.)"
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Alien: {cleaned_response}")
            count += 1

        else:
            print("▒⶘◚⻗⧏⻶⣉⪖ ╻❻♁⛹⼆⃒└≗♕ (You are crazy if you think you are getting out alive.)")
            speakAlien += 1
            
    while speakOldLady == 1:
        if count == 0:
            print("Old Lady: WHAT ARE YOU DOING IN MY CAVE?")
            userInput = input("You: ")
            prompt = (
                "You are an old lady living in a cave, you have dimentia so you dont remember where you are and what your name is, the only thing you can remember is something but you have to think about it. "
                "The person will type a prompt and you will respond in character. Use 1 sentance, make sure you bring up trying to remember something but dont make it too obvious, you also have to respond in all caps when talking to the player but when you are thinking, dont use caps"
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Old Lady: {cleaned_response}")
            count += 1

        elif count == 1:
            userInput = input("You: ")
            prompt = (
                "You are an old lady living in a cave, you have dimentia so you dont remember where you are and what your name is, the only thing you can remember is something but you have to think about it. "
                "The person will type a prompt and you will respond in character. Use 1 sentance, make sure you bring up trying to remember something but dont make it too obvious, you also have to respond in all caps when talking to the player but when you are thinking, dont use caps"
                f"here is the prompt: {userInput}"
            )
            response = client.generate(model=model, prompt=prompt)
            cleaned_response = re.sub(r"<think>.*?</think>", "", response.response, flags=re.DOTALL)
            cleaned_response = cleaned_response.replace('\n', '')
            print(f"Old Lady: {cleaned_response}")
            count += 1

        else:
            print("Oh I remember! THERE MIGHT BE A KEY SOMEWHERE IN THE DESERT!!! Have fun!")
            speakOldLady += 1

speakWithCharacter()