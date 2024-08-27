import time

def typing_speed_test():
    prompt_text = "Jobs are there for those with skills and a good work ethic."
    print(" Welcome to the Typing Speed Test!")
    print("Type the sentence -- ", prompt_text)
    input("Press enter when you are ready to start typing...")
    
    start_time = time.time()
    user_input = input("Start typing:\n")
    end_time = time.time()
    
    time_taken = end_time - start_time
    minutes_taken = time_taken / 60.0
    
    words_typed = len(user_input.split())
    wpm = words_typed / minutes_taken
    
    print("\n--- Test Results ---")
    print(f"You typed {words_typed} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is approximately {wpm:.2f} WPM.")
    
    average_typing_speed = 25.0 
    
    if wpm >= average_typing_speed:
        print("Great job! Your typing speed is above average.")
    else:
        print("Keep practicing to improve your typing speed.")
    
    accuracy = calculate_accuracy(prompt_text, user_input)
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(prompt, typed_text):
    prompt_words = prompt.split()
    typed_words = typed_text.split()
    
    correct_words = 0
    for pw, tw in zip(prompt_words, typed_words):
        if pw == tw:
            correct_words += 1
    
    accuracy = (correct_words / len(prompt_words)) * 100
    return accuracy

typing_speed_test()
