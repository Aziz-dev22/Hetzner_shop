# Hetzner Shop
# GitHub Release Checklist


## بررسی فایل‌های اصلی


- [x] README.md موجود است

- [x] LICENSE موجود است

- [x] requirements.txt موجود است

- [x] Dockerfile موجود است

- [x] docker-compose.yml موجود است

- [x] .env.example موجود است



---

## امنیت


- [x] فایل .env در Git قرار نمی‌گیرد

- [x] Token هتزنر داخل کد نیست

- [x] رمز دیتابیس داخل Repository نیست

- [x] کلیدهای امنیتی حذف شده‌اند



---

## Backend


- [x] FastAPI تنظیم شده

- [x] Routerها آماده هستند

- [x] Service Layer کامل است

- [x] Database Layer آماده است



---

## Database


- [x] SQLAlchemy فعال است

- [x] Alembic فعال است

- [x] Migration اولیه ساخته شده



---

## Deployment


- [x] Dockerfile آماده است

- [x] Docker Compose آماده است

- [x] Installer آماده است

- [x] Firewall Setup آماده است



---

## Testing


- [x] Authentication Test

- [x] Database Test

- [x] API Test

- [x] Service Test



---

## قبل از Push


اجرا شود:


```bash
chmod +x release_check.sh

./release_check.sh
