print("Welcome to the Quiz Game!")

def start_quiz():
    print("Starting the quiz...")
    
    score = 0
    ans = input("What is the capital of France? (a) Paris (b) London (c) Berlin: ")
    if ans.lower() == 'a':
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Paris.")
    
    ans = input("What is the full form of HTML? (a) HyperText Markup Language (b) HyperText Machine Language (c) HyperText Marking Language: ")
    if ans.lower() == 'a':
        print("Correct!")
        score += 1
    ans = input("What is the largest planet in our solar system? (a) Earth (b) Jupiter (c) Saturn: ")
    if ans.lower() == 'b':
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Jupiter.")

    ans = input("What is the chemical symbol for water? (a) H2O (b) O2 (c) CO2: ")
    if ans.lower() == 'a': 
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is H2O.")
    

    print("Your final score is: ",score)
    print("You got ",( (score//4) *100), "% questions correct.")
    print("Thank you for playing the Quiz Game!")

start_quiz()