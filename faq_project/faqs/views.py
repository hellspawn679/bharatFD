from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer


@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()

    # Modify queryset with translations
    for faq in faqs:
        faq.question = faq.get_translation(lang)

    serializer = FAQSerializer(faqs, many=True)
    return Response(serializer.data)
