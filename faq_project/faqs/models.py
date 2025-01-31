from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG support
    question_hi = models.TextField(null=True, blank=True)  # Hindi Translation
    question_bn = models.TextField(null=True, blank=True)  # Bengali Translation
    language = models.CharField(max_length=10, default="en")  # Default to English

    def get_translation(self, lang="en"):
        return getattr(self, f"question_{lang}", self.question) or self.question

    def __str__(self):
        return self.question