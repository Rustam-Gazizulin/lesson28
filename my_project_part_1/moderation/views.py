from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, ListView

from moderation.models import Review

class ReviewListView(ListView):
    model = Review

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []

        for rev in self.object_list:
            response.append({
                "author": rev.author,
                "content": rev.content,
                "tour": rev.tour_id

            })

        return JsonResponse(response, safe=False)



@method_decorator(csrf_exempt, name="dispatch")
class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)
