from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from colorama import init
from colorama import Fore, Style
init()

grupo_ofertas = {
    1:{'ocupacion': 'Gestion de Equipos',
        'habilidad_1': 'Facilidad de Comunicación',
        'habilidad_2': 'Escucha activa',
        'habilidad_3': 'Adaptación al cambio'},
    2: {'ocupacion': 'Machine Learning',
        'habilidad_1': 'Respeto a las opiniones',
        'habilidad_2': 'Optimización del tiempo',
        'habilidad_3': 'Adaptación al cambio'},
    3: {'ocupacion': 'Diseñador Gráfico',
        'habilidad_1': 'Facilidad de Comunicación',
        'habilidad_2': 'Escucha activa',
        'habilidad_3': 'Adaptación al cambio'},
    4: {'ocupacion': 'Jardinero',
        'habilidad_1': 'Actitud Positiva',
        'habilidad_2': 'Sociabilidad',
        'habilidad_3': 'Creatividad'},
}

grupo_demandas = {
    1:{'ocupacion': 'Jardinero',
        'habilidad_1': 'Actitud Positiva',
        'habilidad_2': 'Sociabilidad',
        'habilidad_3': 'Escucha activa'},
    2:{'ocupacion': 'Data Scientist',
        'habilidad_1': 'Facilidad de Comunicación',
        'habilidad_2': 'Escucha activa',
        'habilidad_3': 'Adaptación al cambio'},
    3:{'ocupacion': 'Cuidador',
        'habilidad_1': 'Facilidad de Comunicación',
        'habilidad_2': 'Escucha activa',
        'habilidad_3': 'Adaptación al cambio'},
    4:{'ocupacion': 'Gestion de Equipos',
        'habilidad_1': 'Facilidad de Comunicación',
        'habilidad_2': 'Escucha activa',
        'habilidad_3': 'Adaptación al cambio'},
}
def match():
    for i in range(4):
        for j in range(4):
            match = 0
            for (key, value) in set(grupo_demandas[i+1].items()) & set(grupo_ofertas[j+1].items()):
                #print('{}: {} is present in both aa and bb'.format(key, value))
                match += 1
                if key == 'ocupacion':
                    #match += 1
                    if match > 2:
                        print(Fore.RED + "Este sirve i: {} y j: {}".format(i+1,j+1))
                        return grupo_demandas[i+1]

revision = match()
print(revision)

class MatchTemplateView(LoginRequiredMixin, TemplateView):
	
	template_name = 'match.html'
	extra_context = {'match':revision}