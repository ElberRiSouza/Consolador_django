from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . views import index, assistsocial, atendimento_fr, bazar, blog, comarte, consolarte, contact, doacoes, estudos,eventos, evang_infantil, mocidade

urlpatterns = [
    path('', index),
    path('assistsocial/', assistsocial),
    path('atendimento/', atendimento_fr),
    path('bazar/', bazar),
    path('blog/', blog),
    path('comarte/', comarte),
    path('consolarte/', consolarte),
    path('contact/', contact, name='contact'),
    path('doacoes/', doacoes),
    path('estudos/', estudos),
    path('eventos/', eventos),
    path('evang_infantil/', evang_infantil),
    path('mocidade/', mocidade),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)