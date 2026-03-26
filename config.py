# src/core/config.py
from pathlib import Path

# ==========================================
# 1. Root & Base Directories
# ==========================================
# ไดรฟ์หลักและโฟลเดอร์ปลายทางของข้อมูลฝนทั้งหมด
HII_DRIVE = Path(r"D:\HII")
ONEDRIVE_DATA_DIR = HII_DRIVE / r"OneDrive\HydroDataSci\Data"

# ไดเรกทอรีของโปรเจค Shared Services
SHARED_SERVICES_DIR = HII_DRIVE / "shared_rain_services"

# ==========================================
# 2. Shared Data Files
# ==========================================
# ไฟล์ตั้งค่าปีเหมือน (ย้ายมาไว้ในโปรเจคตามที่คุยกัน)
ANALOG_YEARS_CSV_PATH = SHARED_SERVICES_DIR / "data" / "analog_years.csv"

# ==========================================
# 3. Rainfall Data Paths
# ==========================================

# --- 3.1 Observed, Avg 30Y & Analog (ฝนตรวจวัด, ค่าเฉลี่ย 30 ปี, และฝนปีเหมือน สสน.) ---
OBS_BASE_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\TMD\Picture"
OBS_REGION_DIR = OBS_BASE_DIR / "picture_region"
OBS_BASIN_DIR = OBS_BASE_DIR / "picture_basin"
OBS_ANOMALY_DIR = OBS_BASE_DIR / "picture_anomaly"
AVG30Y_DIR = OBS_BASE_DIR / "picture_avg30y"

# --- 3.2 HII Forecast (ฝนคาดการณ์ สสน. รายปี) ---
HII_FCST_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\HII\Forecast"

# --- 3.3 One Map (ฝนคาดการณ์ 3 cases) ---
ONEMAP_BASE_DIR = ONEDRIVE_DATA_DIR / r"OneMap\Leaflet\out"
ONEMAP_REGION_DIR = ONEMAP_BASE_DIR / r"region\map_image\3cases_map"
ONEMAP_BASIN_DIR = ONEMAP_BASE_DIR / r"basin\map_image\3cases_map"

# --- เพิ่ม Path สำหรับฝนคาดการณ์อุตุฯ (TMD Forecast) ---
ONEMAP_TMD_REGION_DIR = ONEMAP_BASE_DIR / r"region\map_image\tmd_region"
ONEMAP_TMD_COUNTRY_DIR = ONEMAP_BASE_DIR / "one_map"

# --- 3.4 Difference (ผลต่าง Observe vs Forecast) ---
DIFF_OBS_FCST_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\difference\Observe_Forecast"
DIFF_THAILAND_DIR = DIFF_OBS_FCST_DIR / "Thailand"
DIFF_REGION_DIR = DIFF_OBS_FCST_DIR / "Region"