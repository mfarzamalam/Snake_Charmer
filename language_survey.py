from survey import *

question = "How many language you speak?"
result = AnonymousSurvey(question)
result.show_question()

print("Enter q to quit:")
while True:
    language = input("Language:")
    if language.lower() == 'q':
        break
    else:
        result.take_survey(language)

print("Thank you for participating in the poll")
result.show_results()