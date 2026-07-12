#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop - Professional Installer
# Version: 1.0.0
# Compatible: Ubuntu / Debian
# ==========================================================

set -euo pipefail

APP_NAME="Hetzner Shop"
PYTHON_MIN_VERSION="3.10"
INSTALLER="install.py"

GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[1;33m"
BLUE="\033[0;34m"
RESET="\033[0m"


print_header() {
    echo -e "${BLUE}"
    echo "=================================================="
    echo "              ${APP_NAME}"
    echo "          Professional Installation"
    echo "=================================================="
    echo -e "${RESET}"
}


success() {
    echo -e "${GREEN}[✓] $1${RESET}"
}


error() {
    echo -e "${RED}[✗] $1${RESET}"
}


warning() {
    echo -e "${YELLOW}[!] $1${RESET}"
}


info() {
    echo -e "${BLUE}[i] $1${RESET}"
}


check_root() {

    if [[ "$EUID" -ne 0 ]]; then
        error "این نصب‌کننده باید با دسترسی root اجرا شود."
        echo
        echo "اجرا کنید:"
        echo "sudo bash install.sh"
        exit 1
    fi

    success "دسترسی root تایید شد."
}


check_os() {

    if [[ ! -f /etc/os-release ]]; then
        error "سیستم‌عامل شناسایی نشد."
        exit 1
    fi

    source /etc/os-release


    case "$ID" in

        ubuntu)
            success "Ubuntu شناسایی شد."
            ;;

        debian)
            success "Debian شناسایی شد."
            ;;

        *)
            error "این سیستم‌عامل پشتیبانی نمی‌شود: $ID"
            exit 1
            ;;

    esac
}


update_system() {

    info "در حال بروزرسانی مخازن..."

    apt update -y

    apt upgrade -y

    success "سیستم بروزرسانی شد."
}


install_dependencies() {

    info "در حال نصب پیش‌نیازها..."

    apt install -y \
        python3 \
        python3-pip \
        python3-venv \
        python3-dev \
        git \
        curl \
        wget \
        sqlite3 \
        nginx \
        openssl \
        ufw


    success "پیش‌نیازها نصب شدند."
}
check_python() {

    info "بررسی نسخه Python..."

    if ! command -v python3 &> /dev/null; then
        error "Python3 نصب نیست."
        exit 1
    fi


    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')


    success "Python نسخه $PYTHON_VERSION شناسایی شد."
}


create_virtual_environment() {

    if [[ ! -d "venv" ]]; then

        info "ساخت محیط مجازی Python..."

        python3 -m venv venv

        success "محیط مجازی ساخته شد."

    else

        warning "محیط مجازی قبلاً وجود دارد."

    fi
}


install_python_packages() {


    if [[ ! -f "requirements.txt" ]]; then

        error "فایل requirements.txt پیدا نشد."

        exit 1

    fi


    info "فعال‌سازی محیط مجازی..."

    source venv/bin/activate


    info "بروزرسانی pip..."

    pip install --upgrade pip


    info "نصب کتابخانه‌های پروژه..."

    pip install -r requirements.txt


    success "کتابخانه‌ها نصب شدند."
}



create_directories() {


    info "ساخت پوشه‌های اصلی..."


    mkdir -p \
        logs \
        backups \
        uploads \
        config \
        database \
        storage



    success "ساختار پوشه‌ها ایجاد شد."

}



check_ports() {


    DEFAULT_PORT=8080


    if command -v ss &> /dev/null; then


        if ss -tuln | grep -q ":${DEFAULT_PORT} "; then

            warning "پورت ${DEFAULT_PORT} در حال استفاده است."

        else

            success "پورت ${DEFAULT_PORT} آزاد است."

        fi

    fi

}



set_permissions() {


    chmod +x "$INSTALLER" 2>/dev/null || true


    chmod 700 config 2>/dev/null || true


    success "سطح دسترسی‌ها تنظیم شد."

}



run_python_installer() {


    if [[ ! -f "$INSTALLER" ]]; then

        error "فایل $INSTALLER وجود ندارد."

        exit 1

    fi


    info "اجرای نصب‌کننده اصلی..."


    source venv/bin/activate


    python3 "$INSTALLER"


}
main() {

    print_header

    check_root

    check_os

    update_system

    install_dependencies

    check_python

    create_directories

    create_virtual_environment

    install_python_packages

    check_ports

    set_permissions

    run_python_installer


    echo
    echo -e "${GREEN}"
    echo "=================================================="
    echo "       نصب Hetzner Shop با موفقیت انجام شد"
    echo "=================================================="
    echo -e "${RESET}"

}


trap 'error "نصب به دلیل خطا متوقف شد."' ERR


main "$@"
