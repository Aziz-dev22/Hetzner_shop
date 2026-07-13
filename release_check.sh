#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# Release Check Script
# ==========================================================

set -e


echo "======================================"
echo " Hetzner Shop Release Check"
echo "======================================"



echo ""
echo "[1/5] Checking Python..."


python3 --version



echo ""
echo "[2/5] Checking requirements..."


if [ -f "requirements.txt" ]; then

    echo "requirements.txt OK"

else

    echo "requirements.txt missing"

    exit 1

fi



echo ""
echo "[3/5] Checking project structure..."


if [ -f "project_check.py" ]; then

    python3 project_check.py

else

    echo "project_check.py missing"

    exit 1

fi



echo ""
echo "[4/5] Running tests..."


pytest



echo ""
echo "[5/5] Checking Docker..."


if command -v docker >/dev/null 2>&1; then

    docker --version

else

    echo "Docker not installed"

fi



echo ""

echo "======================================"

echo " Release Check Completed Successfully"

echo "======================================"
