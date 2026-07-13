#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# Ubuntu Deployment Installer
# Compatible: Ubuntu 22.04+
# ==========================================================

set -e


PROJECT_DIR="/opt/hetzner-shop"



echo "======================================"

echo " Hetzner Shop Ubuntu Installer"

echo "======================================"



echo ""

echo "[1/6] Updating system..."

apt update

apt upgrade -y



echo ""

echo "[2/6] Installing required packages..."

apt install -y \

    git \

    curl \

    ca-certificates \

    docker.io



echo ""

echo "[3/6] Installing Docker Compose..."



apt install -y docker-compose-plugin



echo ""

echo "[4/6] Starting Docker..."



systemctl enable docker

systemctl start docker



echo ""

echo "[5/6] Preparing project directory..."



if [ ! -d "$PROJECT_DIR" ]; then


    mkdir -p "$PROJECT_DIR"


fi



echo ""

echo "[6/6] Installation preparation completed"



echo ""

echo "Next steps:"

echo ""

echo "1) Copy project files to:"

echo "$PROJECT_DIR"

echo ""

echo "2) Create .env file"

echo ""

echo "3) Run:"

echo ""

echo "docker compose up -d"
