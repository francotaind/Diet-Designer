from django.shortcuts import redirect

def shift_view(request):
    # Example logic to decide which app to redirect to
    if 'meals' in request.GET:
        return redirect('meals_index')
    elif 'recipes' in request.GET:
        return redirect('recipes_index')
    elif 'store' in request.GET:
        return redirect('store_index')
    elif 'accounts' in request.GET:
        return redirect('login')
    else:
        # Default redirect if no valid parameter is provided
        return redirect('home')  # Ensure 'home' is defined in your URLs

