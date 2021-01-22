import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):
    def test_future_polls(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_published_recently_with_new_question(self):
        time = timezone.now() - datetime.timedelta(hours=23,  minutes=59, seconds=59)
        new_question = Question(pub_date = time)
        self.assertIs(new_question.was_published_recently(), True)

