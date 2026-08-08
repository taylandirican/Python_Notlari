#Question
#ne kadar az if bloğu kıullanırsak o kadar kaliteli ve düzenli kod yazmış oluruz

class question():
    def __init__(self,text,choices,answer):
            self.text = text
            self.choices = choices
            self.answer = answer

    def checkAnswer(self,answer):
          return self.answer == answer
    



# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("C#"))

#Quiz
class Quiz():
      def __init__(self,questions):
            self.questions = questions
            self.score = 0
            self.qİndex = 0
      def 


q1 = question("en iyi prog.dili?",["C#","Python","javascript","java"],"Python")
q2 = question("en popğler prog.dili?",["C#","Python","javascript","java"],"Python")
q3 = question("en kazandiran prog.dili?",["C#","Python","javascript","java"],"Python")
Questions = [q1,q2,q3]
quiz=Quiz(Questions)
Question = quiz.questions[quiz.qİndex]
print(Question.text)