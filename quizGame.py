score= 0
# Create a list of questions and answers
questions = [
    ["What does CPU stand for?", ["central processing unit", "cpu"]],
    ["What does RAM stand for?", ["random access memory", "ram"]],
    ["What is the name of the device that connects a computer to a network?", ["modem", "router"]],
    ["What is the extension of a Python file?", [".py"]],
    ["What is the name of the software that allows you to browse the web?", ["browser", "web browser"]]
]

# Iterate over the questions and answers
for question, answer in questions:
    # Ask the question and get the user's input
    user_answer = input(question).strip().lower()
    # Check if the user's answer is correct
    if user_answer in answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You scored {score} out of {len(questions)}!")
