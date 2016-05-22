import os
import unittest
import sys
sys.path.append('/home/box/web/ask')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ask.settings'

from django import forms

class TestAuthorship(unittest.TestCase):
    def test_authorship(self):
        username = sys.argv[2]
        q_id = sys.argv[3]
        from qa.models import Question
        from django.contrib.auth.models import User
        question = Question.objects.get(pk=q_id)
        user = User.objects.get(username=username)
        assert question.author == user, "Question id={0} created by authorized user username={1}, but author field is empty".format(q_id, username)

suite = unittest.TestLoader().loadTestsFromTestCase(globals().get(sys.argv[1]))
unittest.TextTestRunner(verbosity=0).run(suite)
