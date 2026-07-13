#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# Database Backup Script
# PostgreSQL
# ==========================================================


set -e



BACKUP_DIR="/opt/hetzner-shop/backups"

CONTAINER_NAME="hetzner_shop_postgres"


DATE=$(date +"%Y-%m-%d_%H-%M-%S")



mkdir -p "$BACKUP_DIR"



echo "======================================"

echo " Hetzner Shop Backup"

echo "======================================"



echo ""

echo "Creating database backup..."



docker exec "$CONTAINER_NAME" \

pg_dump -U "$DATABASE_USER" "$DATABASE_NAME" \

> "$BACKUP_DIR/database_$DATE.sql"





echo ""

echo "Compressing backup..."



gzip "$BACKUP_DIR/database_$DATE.sql"





echo ""

echo "Removing old backups..."



find "$BACKUP_DIR" \

-name "*.sql.gz" \

-mtime +30 \

-delete





echo ""

echo "Backup completed:"

echo "$BACKUP_DIR/database_$DATE.sql.gz"
