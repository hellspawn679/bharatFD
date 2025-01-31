from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    cache_key = f'faqs_{lang}'

    try:
        # Check if the cached data exists
        faqs = cache.get(cache_key)
    except Exception as e:
        # no redis avaliable 
        #print(f"Error retrieving cache: {e}")
        faqs = None
    #print(f"Cache hit: {faqs is not None}")  # Debugging statement

    if faqs is None:
        #print("Cache miss! Fetching from database...") 
        faqs = FAQ.objects.all()

        # Translate and prepare data
        for faq in faqs:
            translated_data = faq.get_translation(lang)
            faq.question = translated_data["question"]
            faq.answer = translated_data["answer"]

        # Serialize the FAQs
        serializer = FAQSerializer(faqs, many=True)
        faqs = serializer.data 

        try:
            cache.set(cache_key, faqs, timeout=3600)  
        except Exception :
            print("no redis")

    return Response(faqs)  
