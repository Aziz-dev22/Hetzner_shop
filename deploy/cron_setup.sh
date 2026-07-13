#!/usr/bin/env bash

# ==========================================================
# Hetzner Shop
# Cron Jobs Setup
# ==========================================================


set -e



PROJECT_DIR="/opt/hetzner-shop"

BACKUP_SCRIPT="$PROJECT_DIR/deploy/backup.sh"

HEALTH_SCRIPT="$PROJECT_DIR/deploy/health_check.sh"



echo "======================================"

echo " Hetzner Shop Cron Setup"

echo "======================================"



chmod +x "$BACKUP_SCRIPT"

chmod +x "$HEALTH_SCRIPT"





echo ""

echo "Installing scheduled tasks..."



(crontab -l 2>/dev/null; echo "

# Hetzner Shop Daily Database Backup

0 3 * * * $BACKUP_SCRIPT >> /var/log/hetzner_backup.log 2>&1


# Hetzner Shop Health Check Every 10 Minutes

*/10 * * * * $HEALTH_SCRIPT >> /var/log/hetzner_health.log 2>&1

") | crontab -





echo ""

echo "Cron jobs installed successfully"



echo ""

crontab -l
