"""
Hetzner Shop
Global Constants

تمام ثابت‌های پروژه فقط در این فایل تعریف می‌شوند.
هیچ رشته (Magic String) نباید مستقیماً در پروژه استفاده شود.
"""

from __future__ import annotations

from enum import Enum


###############################################################################
# Application
###############################################################################

APP_NAME = "Hetzner Shop"

PACKAGE_NAME = "server_shop"

DEFAULT_LANGUAGE = "fa"

DEFAULT_TIMEZONE = "UTC"

###############################################################################
# Roles
###############################################################################


class UserRole(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    SUPPORT = "support"
    ACCOUNTANT = "accountant"
    USER = "user"


###############################################################################
# User Status
###############################################################################


class UserStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    BANNED = "banned"
    PENDING = "pending"


###############################################################################
# Provider
###############################################################################


class Provider(str, Enum):
    HETZNER = "hetzner"

    LEASEWEB = "leaseweb"

    WORLDSTREAM = "worldstream"

    OVH = "ovh"

    LINODE = "linode"

    DIGITALOCEAN = "digitalocean"

    VULTR = "vultr"

    GCORE = "gcore"

    CONTABO = "contabo"

    SCALEWAY = "scaleway"


###############################################################################
# Product
###############################################################################


class ProductType(str, Enum):
    DEDICATED = "dedicated"

    VPS = "vps"

    CLOUD = "cloud"

    STORAGE = "storage"

    LICENSE = "license"


###############################################################################
# Order
###############################################################################


class OrderStatus(str, Enum):
    PENDING = "pending"

    WAITING_PAYMENT = "waiting_payment"

    PAID = "paid"

    PROCESSING = "processing"

    COMPLETED = "completed"

    CANCELLED = "cancelled"

    FAILED = "failed"

    REFUNDED = "refunded"


###############################################################################
# Payment
###############################################################################


class PaymentStatus(str, Enum):
    CREATED = "created"

    PENDING = "pending"

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"

    REFUNDED = "refunded"


###############################################################################
# Wallet
###############################################################################


class WalletTransaction(str, Enum):
    DEPOSIT = "deposit"

    WITHDRAW = "withdraw"

    PURCHASE = "purchase"

    REFUND = "refund"

    BONUS = "bonus"

    ADJUSTMENT = "adjustment"


###############################################################################
# Ticket
###############################################################################


class TicketStatus(str, Enum):
    OPEN = "open"

    ANSWERED = "answered"

    WAITING_USER = "waiting_user"

    CLOSED = "closed"


###############################################################################
# Server
###############################################################################


class ServerStatus(str, Enum):
    AVAILABLE = "available"

    RESERVED = "reserved"

    DEPLOYING = "deploying"

    ACTIVE = "active"

    SUSPENDED = "suspended"

    EXPIRED = "expired"

    TERMINATED = "terminated"

    ERROR = "error"


###############################################################################
# API Accounts
###############################################################################


class ProviderAccountStatus(str, Enum):
    ACTIVE = "active"

    DISABLED = "disabled"

    INVALID = "invalid"

    ERROR = "error"


###############################################################################
# Currency
###############################################################################


class Currency(str, Enum):
    EUR = "EUR"

    USD = "USD"

    IRR = "IRR"

    USDT = "USDT"


###############################################################################
# Language
###############################################################################


class Language(str, Enum):
    PERSIAN = "fa"

    ENGLISH = "en"


###############################################################################
# Theme
###############################################################################


class Theme(str, Enum):
    LIGHT = "light"

    DARK = "dark"

    SYSTEM = "system"


###############################################################################
# Backup
###############################################################################


class BackupType(str, Enum):
    MANUAL = "manual"

    AUTO = "auto"


###############################################################################
# Log Level
###############################################################################


class LogLevel(str, Enum):
    DEBUG = "DEBUG"

    INFO = "INFO"

    WARNING = "WARNING"

    ERROR = "ERROR"

    CRITICAL = "CRITICAL"


###############################################################################
# Future Features
###############################################################################

FEATURE_MULTI_PROVIDER = True

FEATURE_MULTI_ADMIN = True

FEATURE_MULTI_LANGUAGE = True

FEATURE_MULTI_CURRENCY = True

FEATURE_PUBLIC_API = True

FEATURE_PLUGIN_SYSTEM = True

FEATURE_BACKUP = True

FEATURE_AUTO_UPDATE = True

FEATURE_WEB_PANEL = True

FEATURE_TELEGRAM_BOT = True
