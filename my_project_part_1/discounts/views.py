from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from discounts.models import Discount


# TODO здесь необходимо реализовать СBV которые
# TODO бы возвращали данные в соответствии со спецификацией
class DiscountListView(ListView):
    model = Discount

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for disc in self.object_list:
            response.append({
                     "id": disc.id,
                    "tour": disc.tour_id,
                    "category": disc.category,
                    "discount": disc.discount,
                    "code": disc.code,
                    "starts_at": disc.starts_at if disc.starts_at else '',
                    "ends_at": disc.ends_at if disc.ends_at else ''
                            })
        return JsonResponse(response, safe=False)


class DiscountDetailView(DetailView):
    model = Discount

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        return JsonResponse({
                         "id": self.object.id,
                        "tour": self.object.tour_id,
                        "category": self.object.category,
                        "discount": self.object.discount,
                        "code": self.object.code,
                        "starts_at": self.object.starts_at if self.object.starts_at else '',
                        "ends_at": self.object.ends_at if self.object.ends_at else ''
                                })