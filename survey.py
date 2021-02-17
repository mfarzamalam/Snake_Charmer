class AnonymousSurvey():
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def take_survey(self,response):
        self.responses.append(response)

    def show_results(self):
        print("The results are:")
        for response in self.responses:
            print("-"+response.title())