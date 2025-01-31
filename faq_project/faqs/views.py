from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()

    # Create a list of translated FAQ data
    faq_data = []

    for faq in faqs:
        translated_data = faq.get_translation(lang)
        # Append translated data to the faq_data list
        faq_data.append({
            "id": faq.id,
            "question": translated_data["question"],
            "answer": translated_data["answer"],
        })

    # Use the FAQSerializer to serialize the translated FAQ data
    serializer = FAQSerializer(faq_data, many=True)
    return Response(serializer.data)
