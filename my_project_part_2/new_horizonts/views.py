from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from new_horizonts.models import City
import json
from django.http import JsonResponse


# TODO поработайте над этим CBV
@method_decorator(csrf_exempt, name='dispatch')
class CityCreateView(CreateView):
    model = City
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        city_data = json.loads(request.body)

        city_obj, _ = City.objects.get_or_create(name=city_data['name'])
        #city_obj.save()

        # try:
        #     city = City.objects.get(name=city_data["name"])
        # except City.DoesNotExist:
        #     city = City.objects.create(
        #         name=city_data["name"]
        #     )

        return JsonResponse({
            "id": city_obj.id,
            "name": city_obj.name,
        })
