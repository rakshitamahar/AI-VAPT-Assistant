"""
Application configuration.
"""
from pathlib import Path

# ==========================
# Project Directories
# ==========================

BASE_DIR = Path(__file__).parent

LOG_DIR = BASE_DIR / "logs"

OUTPUT_DIR = BASE_DIR / "outputs"

REPOT_DIR = BASE_DIR / "reports"

TEMPLATE_DIR = BASE_DIR / "templates"

# ==========================
# Logging
# ==========================

LOG_FILE = LOG_DIR / "app.log"

LOG_LEVEL = "INFO"

# ==========================
# Scanning
# ==========================

DEFAULT_TIMEOUT = 30 

# ==========================
# Report Settings
# ==========================

REPORT_NAME = "vapt_report.html"