"""
Hetzner Shop

Project Paths

تمام مسیرهای پروژه فقط از این فایل خوانده می‌شوند.
"""

from __future__ import annotations

from pathlib import Path


###############################################################################
# Root
###############################################################################

ROOT_DIR = Path(__file__).resolve().parents[2]


###############################################################################
# Application
###############################################################################

APP_DIR = ROOT_DIR / "app"

CORE_DIR = APP_DIR / "core"

BOT_DIR = APP_DIR / "bot"

WEB_DIR = APP_DIR / "web"

API_DIR = APP_DIR / "api"

DATABASE_DIR = APP_DIR / "database"

MODELS_DIR = APP_DIR / "models"

SCHEMAS_DIR = APP_DIR / "schemas"

SERVICES_DIR = APP_DIR / "services"

PROVIDERS_DIR = APP_DIR / "providers"

REPOSITORIES_DIR = APP_DIR / "repositories"

SECURITY_DIR = APP_DIR / "security"

INSTALLER_DIR = ROOT_DIR / "installer"

TESTS_DIR = ROOT_DIR / "tests"

DOCS_DIR = ROOT_DIR / "docs"

SCRIPTS_DIR = ROOT_DIR / "scripts"


###############################################################################
# Data
###############################################################################

DATA_DIR = ROOT_DIR / "data"

CACHE_DIR = DATA_DIR / "cache"

TEMP_DIR = DATA_DIR / "temp"

UPLOAD_DIR = DATA_DIR / "uploads"

EXPORT_DIR = DATA_DIR / "exports"


###############################################################################
# Database
###############################################################################

DATABASE_FILE = DATA_DIR / "database.db"

MIGRATIONS_DIR = DATABASE_DIR / "migrations"


###############################################################################
# Logs
###############################################################################

LOG_DIR = ROOT_DIR / "logs"


###############################################################################
# Backups
###############################################################################

BACKUP_DIR = ROOT_DIR / "backups"


###############################################################################
# Static
###############################################################################

STATIC_DIR = WEB_DIR / "static"

TEMPLATE_DIR = WEB_DIR / "templates"


###############################################################################
# Locales
###############################################################################

LOCALE_DIR = APP_DIR / "locales"


###############################################################################
# Runtime
###############################################################################

ENV_FILE = ROOT_DIR / ".env"

ENV_EXAMPLE_FILE = ROOT_DIR / ".env.example"

REQUIREMENTS_FILE = ROOT_DIR / "requirements.txt"

PYPROJECT_FILE = ROOT_DIR / "pyproject.toml"

README_FILE = ROOT_DIR / "README.md"


###############################################################################
# Runtime Directories
###############################################################################

RUNTIME_DIRECTORIES = (

    DATA_DIR,

    CACHE_DIR,

    TEMP_DIR,

    UPLOAD_DIR,

    EXPORT_DIR,

    LOG_DIR,

    BACKUP_DIR,

)
