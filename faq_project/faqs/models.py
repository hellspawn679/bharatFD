from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


translator = Translator()


def translate_text(text, lang):
    try:
        return translator.translate(text, dest=lang).text
    except Exception:
        return text  


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=10, default="en")

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        super().save(*args, **kwargs)

    def get_translation(self, lang="en"):
        return getattr(self, f"question_{lang}", self.question) or \
            self.question

    def __str__(self):
        return self.question
