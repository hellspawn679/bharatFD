from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)
    language = models.CharField(max_length=10, default="en")

    def save(self, *args, **kwargs):
        """Translate question and answer into Hindi & Bengali before saving."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')

        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')

        super().save(*args, **kwargs)

    def translate_text(self, text, lang):
        """Helper function to translate text dynamically."""
        if not text:
            return ""
        try:
            return translator.translate(text, dest=lang).text
        except Exception:
            return text  # Fallback to original text

    def get_translation(self, lang="en"):
        """
        Retrieves translated question & answer dynamically.
        - If stored translation exists, return it.
        - Otherwise, generate it dynamically.
        """
        translated_question = getattr(self, f"question_{lang}", None)
        translated_answer = getattr(self, f"answer_{lang}", None)

        if not translated_question:
            translated_question = self.translate_text(self.question, lang)
        if not translated_answer:
            translated_answer = self.translate_text(self.answer, lang)

        return {
            "question": translated_question or self.question,
            "answer": translated_answer or self.answer,
        }

    def __str__(self):
        return self.question
