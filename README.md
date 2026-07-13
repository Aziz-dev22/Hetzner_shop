# Hetzner Shop

## پلتفرم حرفه‌ای مدیریت و فروش سرورهای مجازی Hetzner

Hetzner Shop یک سیستم کامل برای مدیریت، فروش و کنترل سرورهای مجازی (VPS) بر پایه Hetzner Cloud است.

این پروژه شامل پنل مدیریت، سیستم کاربران، سفارش، پرداخت، اشتراک، اتصال مستقیم به API هتزنر و پردازش‌های پس‌زمینه می‌باشد.


---

# امکانات پروژه

✅ مدیریت کاربران

✅ سیستم ثبت‌نام و ورود کاربران

✅ احراز هویت با JWT Token

✅ مدیریت سرورهای مجازی VPS

✅ اتصال مستقیم به Hetzner Cloud API

✅ ساخت و حذف خودکار سرورها

✅ سیستم سفارش خرید VPS

✅ مدیریت فاکتور

✅ مدیریت پرداخت‌ها

✅ مدیریت اشتراک و تمدید سرویس

✅ پنل مدیریت ادمین

✅ ارسال اعلان تلگرام

✅ پردازش‌های پس‌زمینه با Celery

✅ پشتیبانی از Docker

✅ آماده نصب روی سرورهای لینوکسی


---

# تکنولوژی‌های استفاده شده

## Backend

- Python 3.12

- FastAPI

- SQLAlchemy

- PostgreSQL

- Redis

- Celery


## Security

- JWT Authentication

- Password Hashing با Bcrypt


## Deployment

- Docker

- Docker Compose

- Uvicorn


---

# پیش‌نیازهای نصب

برای اجرای پروژه نیاز دارید:

- Ubuntu 22.04 یا بالاتر

- Docker

- Docker Compose

- دامنه (اختیاری)


---

# نصب پروژه


## مرحله اول: دریافت پروژه


```bash
git clone https://github.com/your-user/hetzner-shop.git

cd hetzner-shop

مرحله دوم: ساخت فایل تنظیمات
ابتدا فایل نمونه تنظیمات را کپی کنید:
cp .env.example .env
سپس فایل تنظیمات را باز کنید:
nano .env
مقادیر مورد نیاز را وارد کنید:
HETZNER_API_TOKEN=توکن_هتزنر

DATABASE_PASSWORD=رمز_دیتابیس

JWT_SECRET_KEY=کلید_امنیتی
اجرای پروژه با Docker
برای اجرای تمام سرویس‌ها:
docker compose up -d
پس از اجرا سرویس‌های زیر فعال می‌شوند:
Hetzner Shop Application
PostgreSQL Database
Redis
Celery Worker
بررسی وضعیت سرویس‌ها
docker compose ps
مشاهده Logها
برنامه اصلی:
docker logs hetzner_shop_app
Worker:
docker logs hetzner_shop_worker
اجرای دستی Worker
در صورت نیاز:
docker compose restart worker
آدرس دسترسی
پس از اجرا:
http://SERVER_IP:8000
