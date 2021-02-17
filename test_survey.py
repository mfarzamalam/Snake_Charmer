import unittest
from survey import *

class TestAnonymousClass(unittest.TestCase):
    
    def setUp(self):
        question = "What language you first learn to speak?"
        self.survey_question = AnonymousSurvey(question)
        self.responses = ['English','Urdu','Punjabi']

    def test_single_response(self):
        self.survey_question.take_survey(self.responses[2])
        self.assertIn(self.responses[2],self.survey_question.responses)

    def test_two_responses(self):
        for response in self.responses:
            self.survey_question.take_survey(response)

        for response in self.responses:
            self.assertIn(response,self.survey_question.responses)

unittest.main()