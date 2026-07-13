#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# SSL Setup Script
# Let's Encrypt + Nginx
# ==========================================================


set -e



DOMAIN=$1

EMAIL=$2



if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then


    echo "Usage:"

    echo "./ssl_setup.sh example.com admin@example.com"

    exit 1


fi



echo "======================================"

echo " Hetzner Shop SSL Setup"

echo "======================================"



echo ""

echo "[1/4] Installing Certbot..."



apt update


apt install -y \

    certbot \

    python3-certbot-nginx





echo ""

echo "[2/4] Requesting SSL Certificate..."



certbot \

    --nginx \

    -d "$DOMAIN" \

    --email "$EMAIL" \

    --agree-tos \

    --non-interactive





echo ""

echo "[3/4] Testing Renewal..."



certbot renew --dry-run





echo ""

echo "[4/4] SSL Setup Completed"



echo ""

echo "HTTPS enabled for:"

echo "$DOMAIN"
