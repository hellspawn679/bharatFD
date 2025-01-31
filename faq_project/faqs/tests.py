from django.test import TestCase
from .models import FAQ


class FAQModelTestCase(TestCase):

    def setUp(self):
        """Setup initial test data."""
        self.faq = FAQ.objects.create(
            question="What is your name?",
            answer="<p>My name is Mehul.</p>"
        )

    def test_hindi_translation(self):
        """Test for Hindi translation of question and answer."""
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question_hi, "आपका क्या नाम है?")
        self.assertEqual(self.faq.answer_hi, "<p> मेरा नाम मेहुल है। </p>")

    def test_dynamic_translation_french(self):
        """Test for dynamic translation of question and answer into French."""
        translated = self.faq.get_translation(lang="fr")
        self.assertEqual(translated["question"], "Quel est ton nom?")
        self.assertEqual(translated["answer"], "<p> Je m'appelle Mehul. </p>")

    def test_dynamic_translation_spanish(self):
        """Test for dynamic translation of question and answer into Spanish."""
        translated = self.faq.get_translation(lang="es")
        self.assertEqual(translated["question"], "¿Cómo te llamas?")
        self.assertEqual(translated["answer"], "<p> Mi nombre es Mehul. </p>")

    def tearDown(self):
        """Delete the FAQ object after test."""
        self.faq.delete()
