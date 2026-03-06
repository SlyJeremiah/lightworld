# Light World Engineering – Web Application

**Stack:** Django 4.2 · PostgreSQL · Bootstrap 5 · Vercel · Backblaze B2 · Gmail SMTP · Google Analytics

---

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone & enter
git clone https://github.com/yourorg/lightworld.git
cd lightworld

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your values (at minimum set SECRET_KEY & DATABASE_URL)

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Load initial data (optional)
python manage.py loaddata fixtures/initial_data.json

# 8. Run dev server
python manage.py runserver
```

Visit: http://127.0.0.1:8000  
Admin: http://127.0.0.1:8000/admin

---

## 📁 Project Structure

```
lightworld/
├── lightworld/          # Django project config
│   ├── settings.py      #   All settings (env-driven)
│   ├── urls.py          #   Root URL config
│   └── wsgi.py          #   WSGI entry (also used by Vercel)
│
├── core/                # Home, gallery, testimonials
│   ├── models.py        #   Testimonial, GalleryImage
│   ├── views.py         #   home, about, gallery
│   ├── admin.py
│   └── context_processors.py  # COMPANY + GA_ID → all templates
│
├── services/            # Service & pricing data
│   ├── models.py        #   Service, ServicePackage, BoreholeAddon
│   ├── views.py         #   list, detail, solar, borehole
│   └── admin.py
│
├── contact/             # Enquiry form + email notifications
│   ├── models.py        #   Enquiry (leads CRM)
│   ├── forms.py         #   EnquiryForm (Bootstrap-styled)
│   ├── views.py         #   form handling + Gmail SMTP emails
│   └── admin.py        #   Coloured status badges, inline editing
│
├── templates/
│   ├── base.html        # Navbar, footer, GA snippet, Bootstrap 5
│   ├── core/            # home.html, about.html, gallery.html
│   ├── services/        # list, detail, solar, borehole
│   ├── contact/         # contact.html, success.html
│   │   └── email/       # HTML email templates (admin + client)
│   └── partials/        # Reusable card snippets
│
├── static/
│   ├── css/main.css     # Full custom brand CSS (Navy/Gold/Red)
│   ├── js/main.js       # Scroll reveal, nav highlight, scroll bg
│   └── img/             # Brand images from project
│
├── requirements.txt
├── vercel.json          # Vercel deployment config
├── build_files.sh       # collectstatic for Vercel
├── .env.example         # All required environment variables
└── manage.py
```

---

## 🌐 Deploying to Vercel

1. Push code to GitHub
2. Import repo in Vercel dashboard
3. Set all environment variables from `.env.example`  
   (especially `DATABASE_URL`, `SECRET_KEY`, `DEBUG=False`)
4. Vercel auto-runs `build_files.sh` on each deploy

> **Database:** Use [Neon](https://neon.tech) or [Supabase](https://supabase.com) for free PostgreSQL that works with Vercel.

---

## ☁️ Backblaze B2 Storage

For production media files (gallery images etc.):

1. Create a B2 bucket named `lightworld-media` (set to Public)
2. Create Application Key with read/write access
3. Set `USE_B2_STORAGE=True` in your Vercel environment variables
4. Set `B2_KEY_ID`, `B2_APPLICATION_KEY`, `B2_ENDPOINT_URL`

---

## 📧 Gmail SMTP Setup

1. Enable 2FA on the Gmail account
2. Generate an **App Password** (Google Account → Security → App passwords)
3. Set `EMAIL_HOST_PASSWORD` to the 16-character app password (not your login password)

---

## 📊 Google Analytics

1. Create a GA4 property at analytics.google.com
2. Copy the Measurement ID (starts with `G-`)
3. Set `GOOGLE_ANALYTICS_ID=G-XXXXXXXXXX` in environment variables
4. The GA snippet is automatically injected via `base.html` when the ID is set

---

## 🛠️ Admin Panel

The Django admin at `/admin/` provides:

| Model | Features |
|-------|----------|
| **Enquiry** | Coloured status badges, inline editing, search by name/phone/email |
| **Service** | Manage all services + pricing, add packages inline |
| **ServicePackage** | Solar/borehole packages with featured flag |
| **BoreholeAddon** | Extra meter/casing pricing line items |
| **Testimonial** | Feature/unfeature on home page |
| **GalleryImage** | Upload via Backblaze B2, categorise, reorder |

---

## 🔑 Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | ✅ | Django secret key |
| `DEBUG` | ✅ | `True` locally, `False` in production |
| `DATABASE_URL` | ✅ | PostgreSQL connection string |
| `ALLOWED_HOSTS` | ✅ | Comma-separated hostnames |
| `EMAIL_HOST_USER` | ✅ | Gmail address |
| `EMAIL_HOST_PASSWORD` | ✅ | Gmail App Password |
| `ADMIN_EMAIL` | ✅ | Where enquiry notifications go |
| `USE_B2_STORAGE` | ⬜ | `True` to use Backblaze B2 |
| `B2_KEY_ID` | ⬜ | Backblaze key ID |
| `B2_APPLICATION_KEY` | ⬜ | Backblaze application key |
| `B2_BUCKET_NAME` | ⬜ | B2 bucket name |
| `B2_ENDPOINT_URL` | ⬜ | B2 S3-compatible endpoint |
| `GOOGLE_ANALYTICS_ID` | ⬜ | GA4 measurement ID |
