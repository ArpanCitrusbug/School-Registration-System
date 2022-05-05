import re
from django.views.generic import FormView
from ..forms import CustomLoginForm

# class CustomLoginView(View):
#     template_name = 'registration/login.html'
#     def get(self,request):
#         return render(request,self.template_name)
        
#     def post(self,request):
#         email = request.POST.get('email')
#         password = request.POST.get("password")
#         if User.objects.filter(email=email):
#             user = User.objects.get(email=email)
#             print(user)
#             print(check_password(user.password,password))
#             if check_password(user.password,password):
#                 print("password Cheked")
#             else:
#                 print('password not Checked')
#         return render(request,self.template_name)


class CustomLoginView(FormView):
    template_name = 'registration/login.html'
    form_class = CustomLoginForm



    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs