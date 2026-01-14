# Cristo Portfolio (Django) — Dark Minimal, ES/EN, Drag & Drop Admin

## Requirements
- Python 3.10+ recommended
- VS Code

## Setup (Windows)
```bash
cd cristo_portfolio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Setup (macOS/Linux)
```bash
cd cristo_portfolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Use
- Website: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

### Create content
1. In Admin -> Series: create a series (title_es, title_en, slug, cover, order)
2. Inside the series, add photos (image, title_es/title_en, year, location)
3. Drag & drop to reorder series and photos.

## Language toggle
- Use ES/EN pills in the top nav.
- Content falls back to ES if EN fields are empty.

## Deploy (later)
- For production, set DEBUG=False, configure ALLOWED_HOSTS,
  and move media to S3/Cloudinary.
