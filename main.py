from tkinter import *
import random

# Create Window Size
window_size = '600x600'

# Font Variable
textFont = "Courier New Baltic"

# Initialize Window
window = Tk()
window.geometry(window_size)
window.title("Quiz")

# Colors
bg_color = "#2e2e2e" 
button_bg = "#555555"  
button_fg = "#ffffff"  
label_bg = "#333333"  
label_fg = "#ffffff"  
select_color = "#444444" 

window.configure(bg=bg_color)

# Initialize Quiz State
question_count = 0
correct_answers = 0

def mainScreen():
    global mainSection, usernameTextField, titleLabel
    
    titleLabel = Label(window, 
                   text= "Welcome to my Quiz",
                   font=(textFont, 35), 
                   fg=label_fg, 
                   bg=label_bg, 
                   relief= SUNKEN,
                   bd=10,
                   pady=0)
    titleLabel.pack(expand=True, side='top', fill='y', padx=50, pady=100)
    
    # Main section
    mainSection = Frame(window, bg=bg_color)
    mainSection.pack(expand=True, side='top', pady=100)
    
    # Label for Username
    usernameLabel = Label(mainSection, text="Enter your Name", 
                        font=(textFont, 30),
                        bg=bg_color,
                        fg=label_fg)
    usernameLabel.pack()

    # Grab Username
    usernameTextField = Entry(mainSection, 
                            font=(textFont,30),
                            bg="#444444",  
                            fg=button_fg)
    usernameTextField.pack()
    
    # Start Button
    startButton = Button(mainSection, 
                        text="Start Quiz",
                        command=startQuiz,
                        bg=button_bg,
                        fg=button_fg,
                        font=(textFont, 20))
    startButton.pack()
    
# Function to Start Quiz
def startQuiz():
    global usernameTextField, usernameInput
    usernameInput = usernameTextField.get()
    
    if usernameInput:
        print("Hello " + usernameInput.capitalize() + ", Good Luck On The Test :)")
        usernameTextField.config(state=DISABLED)
        deleteScreen()
        quiz()

def deleteScreen():
    mainSection.pack_forget()
    titleLabel.pack_forget()

def quiz():
    global correct_answer, answerList, x, questionLabel, submitButton, radiobuttons, question_count
    
    # Increment question count
    question_count += 1
    
    # Check if the quiz has reached 10 questions
    if question_count > 10:
        show_final_score()
        return
    
    # Get Random Numbers for Quiz
    num1 = random.randint(1, 1000)
    num2 = random.randint(-5000, 10000)
    operator_list = ['/', '*', '+', '-']
    operator = random.choice(operator_list)
    
    # Show Question
    questionLabel = Label(window, 
                          text= f'Question {question_count}/10: What is {num1} {operator} {num2}? ',
                          font=(textFont, 15),
                          pady=50,
                          bg=bg_color,
                          fg=label_fg)
    questionLabel.pack()
    
    # Calculate Correct Answer
    if operator == '/':
        correct_answer = num1 / num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
        
    answerList = [round(correct_answer)]
    x = IntVar()
    
    # Show Answer Choices
    radiobuttons = []
    
    
    while len(answerList) < 4:
        incorrect_answer = round(correct_answer + random.randint(-100, 100))
        if incorrect_answer not in answerList:
            answerList.append(incorrect_answer)
            
    random.shuffle(answerList)
    
    for index in range(len(answerList)):
        rb = Radiobutton(window,
                         font=(textFont, 15),
                         text=answerList[index],
                         variable=x,
                         value=index,
                         bg=bg_color,
                         fg=label_fg,
                         selectcolor=select_color) 
        rb.pack()
        radiobuttons.append(rb)
    
    # Submit Button to Check Answer
    submitButton = Button(window,
                          text="Submit Answer",
                          command=check_answer,
                          bg=button_bg,
                          fg=button_fg,
                          font=(textFont, 20))
    submitButton.pack()

def check_answer():
    global correct_answer, answerList, correct_answers, question_count
    
    # Retrieve selected index and the corresponding answer
    current_index = x.get()
    selected_answer = answerList[current_index]
    
    # Check if the selected answer is correct
    if selected_answer == round(correct_answer):
        correct_answers += 1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    
    # Proceed to the next question
    nextQuestion()

def nextQuestion():
    
    # Hide the previous question
    if questionLabel:
        questionLabel.pack_forget()
    
    if submitButton:
        submitButton.pack_forget()
    
    # Hide all previous answer choices
    for rb in radiobuttons:
        rb.pack_forget()
    
    # Clear the list of answer choices
    radiobuttons.clear()
    
    # Generate the next question
    quiz()

def show_final_score():
    global final_score_label, homeButton
    
    # Clear submit and question Label
    if questionLabel:
        questionLabel.pack_forget()
    
    if submitButton:
        submitButton.pack_forget()
    
    # Hide all previous answer choices
    for rb in radiobuttons:
        rb.pack_forget()
    
    # Clear the list of answer choices
    radiobuttons.clear()
    
    # Display final score
    final_score_label = Label(window,
                              text=f'Good Job {usernameInput}, Your Quiz is Over! Your final score is {correct_answers} out of 10.',
                              font=(textFont, 13),
                              pady=50,
                              bg=bg_color,
                              fg=label_fg)
    final_score_label.pack()

    # Add Home Button to Final Screen
    homeButton = Button(window,
                        text='Back Home',
                        command=restart)
    homeButton.pack()

# Clear all variables to restart quiz    
def restart():
    global question_count, correct_answers, usernameInput
    correct_answers = 0
    question_count = 0
    final_score_label.pack_forget()
    homeButton.pack_forget()   
    usernameInput = '' 
    mainScreen()   

# Call the Main Screen Function
mainScreen()

# Run Window
window.mainloop()
