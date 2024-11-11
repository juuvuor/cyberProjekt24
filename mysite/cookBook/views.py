from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login
# FIX FLAW 2:
# from django.views.decorators.csrf import csrf_protect
from django import forms
from .models import Entry
from .forms import RecipeForm



#FLAW 3: Security Logging and Monitoring Failures

# import logging

# # Get an instance of a logger
# logger = logging.getLogger(__name__)



@login_required
# FLAW 2: using @csrf_exempt 
@csrf_exempt
# FIX FLAW 2: remove the csrf_exempt decorator add @csfr_protect decorator
def home(request):
    username = request.user.username
    # FLAW 1: SQL Injection vulnerability due to f-string usage
    query = f"SELECT * FROM cookBook_entry WHERE user_id = (SELECT id FROM auth_user WHERE username = '{username}')"
    # FIX FLAW 1: 
    # entry = get_entries_by_username(username)
    # Look at the fix in the function get_entries_by_username
    with connection.cursor() as cursor:
        cursor.execute(query) 
        recipe = cursor.fetchall()
        
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            # FIX FLAW 3: logger.info(f"User {username} created a new recipe with ID {new_recipe.id}.")
            return redirect('/') 
    else:
        form = RecipeForm()

    return render(request, 'cookBook/index.html', {'cookBook':recipe, 'form': form})


# FIX FLAW 1: 
# def get_entries_by_username(username):
#     query = """
#         SELECT * FROM cookBook_recipe 
#         WHERE user_id = (SELECT id FROM auth_user WHERE username = %s)
#     """
#     with connection.cursor() as cursor:
#         cursor.execute(query, [username])
#         entries = cursor.fetchall()
#     return entries



# FLAW 2: using @csrf_exempt 
@csrf_exempt
# FIX flaw 2: remove the csrf_exempt decorator add @csfr_protect decorator

# FLAW 5: Broken access Control missing @login_required decorator
# FIX FLAW 5: add @login_required 
def delete(request, recipe_id):
    recipe=Entry.objects.get(pk=recipe_id)
    #FIX FLAW 5:
    # if recipe.user != request.user:
    #      return redirect('/')
    # else:
    recipe.delete()
    # FIX FLAW 3: logger.info(f"User {request.user.username} deleted recipe with ID {recipe_id}.")
    return redirect('/')




# FLAW 2: using @csrf_exempt 
@csrf_exempt
# FIX FLAW 2: remove the csrf_exempt decorator add @csfr_protect decorator

# FLAW 5: Broken access Control missing @login_required decorator
# FIX FLAW 5: add @login_required decorator
# @login_required
def edit(request, recipe_id):
    recipe = Entry.objects.get(pk=recipe_id)
    #FIX FLAW 5:
    # if recipe.user != request.user:
    #     return HttpResponse(' You do not have access to this recipe')
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            edited_recipe = form.save(commit=False)
            edited_recipe.user = request.user
            edited_recipe.save()
            # FIX FLAW 3: logger.info(f"User {request.user.username} deleted recipe with ID {recipe_id}.")
            return redirect('/')
    else:
        form = RecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form    
    }
    return render(request, 'cookBook/edit.html', context)

