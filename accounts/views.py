"""Accounts views."""

# Django
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

# Forms
from accounts.forms import SignupHunterForm, SignupPreyForm

# Models

from accounts.models import ProfileHunter, ProfilePrey

# Create your views here.

from django.shortcuts import render, redirect
import requests
import base64

# Función que codifica una cadena de texto en base64
def stringToBase64(data):
    return base64.b64encode(data.encode('utf-8'))

class SignupHunterView(FormView):
    """Signup View."""
    template_name = 'accounts/signup.html'
    form_class = SignupHunterForm
    success_url = reverse_lazy('accounts:login')
    extra_context = {'is_hunter':True}
    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)


class SignupPreyView(FormView):
    """Signup View."""
    template_name = 'accounts/signup.html'
    form_class = SignupPreyForm
    success_url = reverse_lazy('accounts:login')
    extra_context = {'is_hunter':False}
    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""

class UpdateProfileHunterView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'accounts/update_profile.html'
    model = ProfileHunter
    fields = ['biography', 'phone_number', 'picture']
    context_object_name = 'profile'
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profilehunter
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('accounts:detail', kwargs={'username_slug': username})

class UpdateProfilePreyView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'accounts/update_profile.html'
    model = ProfilePrey
    fields = ['biography', 'phone_number', 'picture', 'profession']
    context_object_name = 'profile'
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profileprey
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('accounts:detail', kwargs={'username_slug': username})


class UserDetailView(DetailView):
    """User detail view."""
    template_name = 'accounts/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_contex_data(self, **kwargs):
        context = super().get_contex_data(**kwargs)
        user = self.get_object()
        context['profile'] = ProfilePrey.objects.get(user=user)
        return context


# Función que renderiza la vista index de la aplicación
def oauth(request):
    context = {}
    return render(request, 'accounts/index.html', context)

# Función que renderiza formulario para el ingreso de datos requeridos por la app
def otpData(request):
    context = {}
    return render(request, 'accounts/otp-data.html', context)

# Función que redirecciona al otp de oauth bancolombia
def otpForm(request):
    context = {}
    if request.method == 'POST':
        #almacenamiento de datos en variables de sesión
        request.session['client_id'] = request.POST.get('client_id')
        request.session['client_secret'] = request.POST.get('client_secret')
        request.session['catalog'] = request.POST.get('catalog')
        request.session['scope'] = request.POST.get('scope')
        request.session['redirect_uri'] = request.POST.get('redirect_uri')
        # url redirect
        params = '?client_id='+request.session['client_id']+'&response_type=code'+'&scope='+request.session['scope']+'&redirect_uri='+request.session['redirect_uri'];
        url = 'https://api.us.apiconnect.ibmcloud.com/bancolombiabluemix-dev/'+request.session['catalog']+'/security/oauth-otp/oauth2/authorize'+params;
        return redirect(url)
    return render(request, 'accounts/oauth.html', context) # crear template de error y renderizarlo


# Función que obtiene el código de autorización de respuesta
def getAuthorizeCode(request):
    context = {}
    code = (request.GET.get('code'))
    context["authorization_code"] = code
    return render(request, 'accounts/authorize-code.html', context)

# Función que obtiene el token de acceso
def getAccessToken(request):
    context = {}
    if request.method == 'POST':
        url = "https://api.us.apiconnect.ibmcloud.com/bancolombiabluemix-dev/"+request.session['catalog']+"/security/oauth-otp/oauth2/token"
        client = str(stringToBase64(request.session['client_id']+":"+request.session['client_secret']))[2:][:-1]
        # parametrización de headers de la petición
        headers = {
            'accept':'application/json',
            'apim-debug':'true',
            'content-type':'application/x-www-form-urlencoded',
            'authorization':'Basic '+client
        }
        # Definición de parametros por body
        params = {  
            'grant_type': 'authorization_code',
            'code': request.POST.get('authorization-code',''),
            'redirect_uri': request.session['redirect_uri'],
            'scope': request.session['scope']
        }
        # ejecución de la petición
        r = requests.post(url, params = params, headers = headers)
        r = r.json()
    context['token_code'] = 'Pago Exitoso!'
    return render(request, 'home.html', context)

