from django.db.models import Count
from django.http import JsonResponse
from django.views.generic import ListView

from users_geography.models import City, User


# TODO внесите необходимые изменения в код ниже
class CityRateView(ListView):
    model = City
    #queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        #super().get(request, *args, **kwargs)
        #self.object_list = self.object_list.annotate(users=Count("user"))
        qs = City.objects.all().annotate(users=Count('user'))
        users = User.objects.aggregate(total=Count("pk"))
        cities = []

        for city in qs:
            cities.append(
                {
                    "id": city.id,
                    "name": city.name,
                    "status": city.status,
                    "users": city.users,
                    "users_percent": users["total"]
                }
            )
        return JsonResponse(cities, safe=False)

