from django.core.paginator import Paginator

NUMBER_POST = 10


def utils(queryset, request):
    paginator = Paginator(queryset, NUMBER_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'paginator': paginator,
        'page_obj': page_obj,
        'page_number': page_number
    }
