import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = 'What language did you first learn to speak'
        self.survey = AnonymousSurvey(question)
        self.responses = ['Arabic', 'Japanese', 'Mandarin']

    def test_store_single_response(self):
        # question = 'What language did you first learn to speak'
        self.survey.store_response('English')
        self.assertIn('English', self.survey.responses)

    def test_store_three_responses(self):
        question = 'What language did you first learn to speak'
        survey = AnonymousSurvey(question)
        # responses = ['Arabic', 'Japanese', 'Mandarin']
        for response in self.survey.responses:
            survey.store_response(response)

        for response in self.survey.responses:
            self.assertIn(response, self.survey.responses)


if __name__ == '__main__':
    unittest.main()
