# from django.shortcuts import render

# # Create your views here.

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import UserForm, UserProfileForm

# @login_required
# def edit_profile(request):
#     user = request.user
#     user_profile = user.userprofile

#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=user)
#         profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('profile')  # Replace with the desired redirect

#     else:
#         user_form = UserForm(instance=user)
#         profile_form = UserProfileForm(instance=user_profile)

#     return render(request, 'edit-profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form,
#     })
