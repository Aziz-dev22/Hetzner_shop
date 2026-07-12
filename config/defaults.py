"""
==========================================================
Hetzner Shop
Default Configuration
==========================================================

تمام تنظیمات پیش‌فرض پروژه در این فایل قرار می‌گیرند.

هیچ بخشی از پروژه نباید مقادیر ثابت (Hard Code)
را مستقیماً داخل کد قرار دهد.

تمام مقادیر باید از این فایل یا settings.json خوانده شوند.
"""

from pathlib import Path


# ==========================================================
# Project Information
# ==========================================================

PROJECT_NAME = "Hetzner Shop"

PROJECT_VERSION = "1.0.0"

CONFIG_VERSION = 1

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# Directory Structure
# ==========================================================

DIRECTORIES = {

    "config": BASE_DIR / "config",

    "database": BASE_DIR / "database",

    "logs": BASE_DIR / "logs",

    "backups": BASE_DIR / "backups",

    "storage": BASE_DIR / "storage",

    "uploads": BASE_DIR / "uploads",

    "static": BASE_DIR / "static",

    "templates": BASE_DIR / "templates",

    "bot": BASE_DIR / "bot",

    "web": BASE_DIR / "web",

    "hetzner": BASE_DIR / "hetzner",

}


# ==========================================================
# Database
# ==========================================================

DATABASE = {

    "engine": "sqlite",

    "filename": "database.db",

    "pool_size": 10,

    "max_overflow": 20,

    "timeout": 30

}


# ==========================================================
# Web Panel
# ==========================================================

WEB = {

    "default_port": 8080,

    "host": "0.0.0.0",

    "debug": False,

    "session_timeout": 86400,

    "csrf_enabled": True,

    "max_login_attempts": 5,

    "lock_time": 900

}


# ==========================================================
# Telegram Bot
# ==========================================================

BOT = {

    "parse_mode": "HTML",

    "workers": 8,

    "request_timeout": 30,

    "connect_timeout": 15

}


# ==========================================================
# Security
# ==========================================================

SECURITY = {

    "password_min_length": 8,

    "password_max_length": 128,

    "bcrypt_rounds": 12,

    "api_token_encryption": True,

    "jwt_expire_hours": 24

}
# ==========================================================
# Hetzner Cloud
# ==========================================================

HETZNER = {

    # حداکثر تعداد اکانت‌های قابل اتصال
    "max_accounts": 100,

    # اکانت پیش‌فرض هنگام نصب
    "default_account": None,

    # مدت اعتبار کش اطلاعات (ثانیه)
    "cache_ttl": 60,

    # Timeout درخواست‌ها
    "request_timeout": 30,

    # تعداد تلاش مجدد
    "max_retries": 3,

    # فاصله بین تلاش‌ها
    "retry_delay": 2,

    # تست اتصال هنگام افزودن اکانت
    "verify_on_add": True,

    # همگام‌سازی خودکار
    "auto_sync": True,

    # فاصله همگام‌سازی (ثانیه)
    "sync_interval": 300

}


# ==========================================================
# Logging
# ==========================================================

LOGGING = {

    "enabled": True,

    "level": "INFO",

    "console": True,

    "file": True,

    "max_size_mb": 20,

    "backup_count": 10,

    "log_requests": True,

    "log_errors": True,

    "log_login": True,

    "log_admin_actions": True

}


# ==========================================================
# Backup
# ==========================================================

BACKUP = {

    "enabled": True,

    "directory": "backups",

    "automatic": True,

    "interval_hours": 24,

    "keep_last": 30,

    "compress": True

}


# ==========================================================
# Uploads
# ==========================================================

UPLOADS = {

    "max_size_mb": 50,

    "allowed_extensions": [

        "png",

        "jpg",

        "jpeg",

        "gif",

        "webp",

        "pdf",

        "zip"

    ]

}


# ==========================================================
# Rate Limit
# ==========================================================

RATE_LIMIT = {

    "enabled": True,

    "telegram_per_minute": 60,

    "web_per_minute": 120,

    "login_attempts": 5

}


# ==========================================================
# Notifications
# ==========================================================

NOTIFICATIONS = {

    "telegram": True,

    "web": True,

    "sound": False,

    "email": False

}
# ==========================================================
# Services
# ==========================================================

SERVICES = {

    "bot_service": "hetzner-shop-bot",

    "web_service": "hetzner-shop-web",

    "auto_start": True,

    "restart": "always",

    "restart_sec": 5

}


# ==========================================================
# Cache
# ==========================================================

CACHE = {

    "enabled": True,

    "default_ttl": 300,

    "max_items": 10000

}


# ==========================================================
# Session
# ==========================================================

SESSION = {

    "cookie_name": "hetzner_shop",

    "cookie_secure": True,

    "cookie_http_only": True,

    "cookie_same_site": "Lax",

    "lifetime_seconds": 86400

}


# ==========================================================
# API
# ==========================================================

API = {

    "version": "v1",

    "prefix": "/api",

    "enable_docs": False

}


# ==========================================================
# Development
# ==========================================================

DEVELOPMENT = {

    "debug": False,

    "profiling": False,

    "reload": False

}


# ==========================================================
# Production
# ==========================================================

PRODUCTION = {

    "strict_mode": True,

    "hide_errors": True,

    "force_https": False

}


# ==========================================================
# File Names
# ==========================================================

FILES = {

    "settings": "settings.json",

    "database": "database.db",

    "installer_log": "install.log"

}


# ==========================================================
# Default Administrator Permissions
# ==========================================================

ADMIN_PERMISSIONS = {

    "full_access": True,

    "manage_users": True,

    "manage_orders": True,

    "manage_servers": True,

    "manage_hetzner_accounts": True,

    "manage_settings": True,

    "view_logs": True,

    "create_backup": True,

    "restore_backup": True

}
