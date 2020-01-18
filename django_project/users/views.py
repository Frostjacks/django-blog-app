from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':  # this will be true when user submits the form after filling it. as after submission it sends those post data to the register url itself
        form=UserRegisterForm(request.POST)  # then it creates a new form form with those user's data

        if form.is_valid():
            form.save()   # save the data to database
            username = form.cleaned_data.get('username')  # if the form is valid then those data are stored in the list called cleaned_data where you can access it's field values
            messages.success(request, f'Your account has been created! You are now able to login.')  # shows a flash message
            return redirect('login')  # at last redirects to home page
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required  # this is decorator. it adds extra functionality to the function
def profile(request):
    if request.method == 'POST': # if the updated form is submitted
        # making an instance of the forms
        u_form = UserUpdateForm(request.POST, instance=request.user)  # this instance will populate the update form with the data of the curently logged in user
        # we pass those updated data in request.POST argument
        # in profile form we also need image data so to get that we have to pass request.FILES argument
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)    # this instance will populate the update form with the data of the curently logged in user's profile
    
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')  
            return redirect('profile') # here if we click reload while midst of editing then it will not save those chages nor will display a prompt saying you want to submit a post request but rather will just display where you left editing

    else:  # when user only wants to view his profile ie not updating then we only show the his info
        u_form = UserUpdateForm(instance=request.user)  # this instance will populate the update form with the data of the curently logged in user
        p_form = ProfileUpdateForm(instance=request.user.profile) 

    # defining them form variables in context so that templates can access them
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

    return render(request, 'users/profile.html', context)
