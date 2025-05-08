import requests
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SearchHistory
from django.views.decorators.http import require_POST


OPENVERSE_API_BASE = "https://api.openverse.org/v1/images/"

def search_view(request):
    query = request.GET.get('q', '').strip()
    license = request.GET.get('license', '')
    extension = request.GET.get('extension', '')

    results = []
    error = None

    if query:
        params = {
            'q': query,
            'page_size': 10,
        }
        if license:
            params['license'] = license
        if extension:
            params['extension'] = extension

        try:
            response = requests.get(OPENVERSE_API_BASE, params=params)
            response.raise_for_status()
            data = response.json()
            results = data.get('results', [])
        except requests.RequestException as e:
            error = f"Failed to fetch results: {e}"

        # Save to search history if user is authenticated
        if request.user.is_authenticated:
            SearchHistory.objects.create(user=request.user, query=query)

    context = {
        'query': query,
        'results': results,
        'error': error,
        'title': 'Search Openverse',
    }
    
    return render(request, 'search_results.html', context)





from django.core.paginator import Paginator

@login_required
def profile_view(request):
    search_list = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    paginator = Paginator(search_list, 5)  # 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profile.html', {'searches': page_obj, 'title':'Profile'})


from django.views.decorators.http import require_POST

@login_required
@require_POST
def delete_search_view(request, search_id):
    search = get_object_or_404(SearchHistory, id=search_id, user=request.user)
    search.delete()
    return redirect('profile')
