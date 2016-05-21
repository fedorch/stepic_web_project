import os
import unittest
import sys
sys.path.append('/home/box/web/ask')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ask.settings'

from django import forms

class TestImport(unittest.TestCase):
    def test_import(self):
        import qa.forms

class TestAskForm(unittest.TestCase):
    def test_from(self):
        from qa.forms import AskForm
        assert issubclass(AskForm, (forms.Form, forms.ModelForm)), "AskForm does not inherits from Form or ModelForm"
        f = AskForm()
        title = f.fields.get('title')
        assert title is not None, "AskForm does not have title field"
        assert isinstance(title, forms.CharField), "title field is not an instance of forms.CharField"
        text = f.fields.get('text')
        assert text is not None, "AskForm does not have text field"
        assert isinstance(text, forms.CharField), "text field is not an instance of forms.CharField"

class TestAnswerForm(unittest.TestCase):
    def test_from(self):
        from qa.forms import AnswerForm
        assert issubclass(AnswerForm, (forms.Form, forms.ModelForm)), "AnswerForm does not inherits from Form or ModelForm"
        f = AnswerForm()
        text = f.fields.get('text')
        assert text is not None, "AnswerForm does not have text field"
        assert isinstance(text, forms.CharField), "text field is not an instance of forms.CharField"
        question = f.fields.get('question')
        assert question is not None, "AnswerForm does not have question field"
        assert isinstance(question, (forms.IntegerField, forms.ChoiceField)), "author field is not an instalce of IntegerField or ChoiceField"

suite = unittest.TestLoader().loadTestsFromTestCase(globals().get(sys.argv[1]))
unittest.TextTestRunner(verbosity=0).run(suite)
