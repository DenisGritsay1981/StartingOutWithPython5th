class Question:
    
    player_1=0
    player_2=0
    
    def __init__(self, question, answer, c_answer):
        self.question=question
        self.answer=answer
        self.c_answer=c_answer
       
    def test1(self):
        if self.c_answer.lower()==self.answer:    
            print("Correct")
            print()
            Question.player_1+=1
        else:
            print("Wrong! The correct answer is", self.answer)
            print()
    
    def get_test1(self):
        return Question.player_1
            
    def test2(self):
        if self.c_answer.lower()==self.answer:    
            print("Correct")
            print()
            Question.player_2+=1
        else:
            print("Wrong! The correct answer is", self.answer)
            print()
        
    def get_test2(self):
        return Question.player_2
    
    def __str__(self):
        return "Player 1: " + str(Question.player_1) + "\n" +\
            "Player 2: " + str(Question.player_2)
    
def main():
    question_objects=[]
 
    questions=["What is the capital of Turkey?\n(a) Istanbul\n(b) Ankara\n(c) Izmir\n(d) Antalya",
               "What is the capital of France?\n(a) London\n(b) Paris\n(c) Moscow\n(d) Washington",
               "Where is the Great Pyramids?\n(a) Israel\n(b) Morocco\n(c) Egypt\n(d) Iraq",
               "What is the world's longest river?\n(a) Nile\n(b) Amazon\n(c) Colorado\n(d) Mississippi",
               "What is the capital of Spain?\n(a) Lisbon\n(b) Paris\n(c) Madrid\n(d) Cordoba",
               "When did the Cold War end?\n(a) 1989\n(b) 1990\n(c) 1985\n(d) 1992"]
    
   
    answers=["b", "b", "c", "b", "c", "a"]
    
    print("Player 1 questions:")
    print()
    for i in range(0,int(len(questions)/2), 1):
        print("Question: ", i+1)
        print(questions[i])
        user_answer=input("Enter correct answer (a,b,c,d): ")
        
        
        question=Question(questions[i], answers[i], user_answer)
        question_objects.append(question)           
        question.test1()
        
    question_objects=[]
    
    print("-------------------------------------------------------")
    print("Player 2 questions")
    print()      
    for i in range(int(len(questions)/2), len(questions),1):
        print("Question: ", i+1)
        print(questions[i])
        user_answer=input("Enter correct answer (a,b,c,d): ")
        
        
        question=Question(questions[i], answers[i], user_answer)
        question_objects.append(question)                  
        
        question.test2()
            
    if question.get_test1()>question.get_test2():
        print("Player 1 has won.")
    elif question.get_test2()>question.get_test1():
        print("Player 2 has won.")
    else:
        print("It is a draw.")
    print()
    print("Player 1 score: ", question.get_test1())
    print("Player 2 score: ",question.get_test2())
        

main()
