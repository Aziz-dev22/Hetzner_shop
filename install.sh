#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop Installer
# Version: 1.0.0
# ==========================================================

set -e

GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
NC="\033[0m"

echo -e "${BLUE}"
echo "=================================================="
echo "             Hetzner Shop Installer"
echo "=================================================="
echo -e "${NC}"

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}لطفاً اسکریپت را با دسترسی root اجرا کنید.${NC}"
    echo
    echo "sudo bash install.sh"
    exit 1
fi

echo -e "${GREEN}✓ دسترسی Root تایید شد.${NC}"

echo
echo "در حال بروزرسانی مخازن..."

apt update

echo
echo "در حال نصب پیش‌نیازها..."

apt install -y \
python3 \
python3-pip \
python3-venv \
git \
curl \
wget \
sqlite3

echo
echo -e "${GREEN}✓ پیش‌نیازها نصب شدند.${NC}"

if [ ! -d "venv" ]; then
    echo
    echo "در حال ساخت محیط مجازی Python..."

    python3 -m venv venv
fi

echo
echo "در حال فعال‌سازی محیط مجازی..."

source venv/bin/activate

echo
echo "در حال بروزرسانی pip..."

pip install --upgrade pip

echo
echo "در حال نصب کتابخانه‌های پروژه..."

pip install -r requirements.txt

echo
echo -e "${GREEN}✓ کتابخانه‌ها نصب شدند.${NC}"

echo
echo "در حال اجرای نصب‌کننده..."

python3 install.py

echo
echo -e "${GREEN}"
echo "==========================================="
echo "      نصب اولیه با موفقیت انجام شد."
echo "==========================================="
echo -e "${NC}"
