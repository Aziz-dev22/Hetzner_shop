#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# Health Check Script
# ==========================================================


set -e



APP_CONTAINER="hetzner_shop_app"

DB_CONTAINER="hetzner_shop_postgres"

REDIS_CONTAINER="hetzner_shop_redis"



echo "======================================"

echo " Hetzner Shop Health Check"

echo "======================================"



echo ""

echo "[1/4] Checking Application..."



if docker ps | grep -q "$APP_CONTAINER"; then

    echo "APP: OK"

else

    echo "APP: FAILED"

fi



echo ""

echo "[2/4] Checking Database..."



if docker ps | grep -q "$DB_CONTAINER"; then

    echo "DATABASE: OK"

else

    echo "DATABASE: FAILED"

fi



echo ""

echo "[3/4] Checking Redis..."



if docker ps | grep -q "$REDIS_CONTAINER"; then

    echo "REDIS: OK"

else

    echo "REDIS: FAILED"

fi



echo ""

echo "[4/4] Checking API..."



if curl -f http://localhost:8000/ >/dev/null 2>&1; then

    echo "API: OK"

else

    echo "API: FAILED"

fi



echo ""

echo "======================================"

echo " Health Check Finished"

echo "======================================"
