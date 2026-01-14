from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import translation
from .models import Series

def _get_lang(request):
    # prefer session override, then current active
    lang = request.session.get("site_lang")
    if lang in ("es", "en"):
        return lang
    return translation.get_language() or "es"

def set_lang(request, lang):
    if lang not in ("es", "en"):
        lang = "es"
    request.session["site_lang"] = lang
    translation.activate(lang)
    # go back where user came from
    nxt = request.GET.get("next") or request.META.get("HTTP_REFERER") or reverse("home")
    return redirect(nxt)

def home(request):
    lang = _get_lang(request)
    hero_series = Series.objects.first()
    return render(request, "portfolio/home.html", {"hero_series": hero_series, "lang": lang})

def work(request):
    lang = _get_lang(request)
    series_list = Series.objects.all()
    return render(request, "portfolio/work.html", {"series_list": series_list, "lang": lang})

def series_detail(request, slug):
    lang = _get_lang(request)
    series = get_object_or_404(Series, slug=slug)
    photos = series.photos.all()
    return render(request, "portfolio/series_detail.html", {"series": series, "photos": photos, "lang": lang})

def about(request):
    lang = _get_lang(request)
    return render(request, "portfolio/about.html", {"lang": lang})

def contact(request):
    lang = _get_lang(request)
    return render(request, "portfolio/contact.html", {"lang": lang})
