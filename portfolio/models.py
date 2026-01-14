from django.db import models

class Series(models.Model):
    # Bilingual content
    title_es = models.CharField("Título (ES)", max_length=120)
    title_en = models.CharField("Title (EN)", max_length=120, blank=True)
    slug = models.SlugField(unique=True)
    description_es = models.TextField("Descripción (ES)", blank=True)
    description_en = models.TextField("Description (EN)", blank=True)

    cover = models.ImageField(upload_to="covers/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title_es"]

    def __str__(self):
        return self.title_es

    def title_for(self, lang: str) -> str:
        if lang == "en" and self.title_en:
            return self.title_en
        return self.title_es

    def description_for(self, lang: str) -> str:
        if lang == "en" and self.description_en:
            return self.description_en
        return self.description_es


class Photo(models.Model):
    series = models.ForeignKey(Series, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos/")

    # Bilingual captions + metadata requested
    title_es = models.CharField("Título foto (ES)", max_length=200, blank=True)
    title_en = models.CharField("Photo title (EN)", max_length=200, blank=True)
    year = models.CharField("Año / Year", max_length=10, blank=True)
    location = models.CharField("Ubicación / Location", max_length=120, blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.series.title_es} — {self.id}"

    def title_for(self, lang: str) -> str:
        if lang == "en" and self.title_en:
            return self.title_en
        return self.title_es
