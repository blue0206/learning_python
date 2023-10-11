from modules import AnonymousSurvey as AS

question = "What language did you first learn to speak?"
language_survey = AS(question)

language_survey.show_question()
print("Enter 'q' to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\nThanks to everyone who participated in the survey!")
language_survey.show_results()