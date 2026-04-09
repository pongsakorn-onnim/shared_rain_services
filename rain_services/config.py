# rain_services\config.py
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
OBS_BASE_DIR    = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\TMD\Picture"
OBS_REGION_DIR  = OBS_BASE_DIR / "picture_region"
OBS_BASIN_DIR   = OBS_BASE_DIR / "picture_basin"
OBS_ANOMALY_DIR = OBS_BASE_DIR / "picture_anomaly"
OBS_COUNTRY_DIR = OBS_BASE_DIR / "picture_observation"   # whole-country yearly observed

# ค่าเฉลี่ย 30 ปี — root (yearly file lives here) + monthly subdirs by area type
#   region  → picture_region
#   basin   → picture_basin
#   country → picture_monthly  (whole-country shapefile)
AVG30Y_DIR         = OBS_BASE_DIR / "picture_avg30y"
AVG30Y_REGION_DIR  = AVG30Y_DIR / "picture_region"
AVG30Y_BASIN_DIR   = AVG30Y_DIR / "picture_basin"
AVG30Y_COUNTRY_DIR = AVG30Y_DIR / "picture_monthly"

# --- 3.2 HII Forecast (ฝนคาดการณ์ สสน. รายปี) ---
HII_FCST_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\HII\Forecast"

# --- 3.3 One Map (ฝนคาดการณ์ 3 cases) ---
ONEMAP_BASE_DIR = ONEDRIVE_DATA_DIR / r"OneMap\Leaflet\out"
ONEMAP_REGION_DIR = ONEMAP_BASE_DIR / r"region\map_image\3cases_map"
ONEMAP_BASIN_DIR = ONEMAP_BASE_DIR / r"basin\map_image\3cases_map"

# --- One Map Weighted (OM_W) — แทนที่ OM_M (Mean) ---
ONEMAP_WEIGHT_REGION_DIR = ONEMAP_BASE_DIR / r"region\map_image\om_weight"
ONEMAP_WEIGHT_BASIN_DIR  = ONEMAP_BASE_DIR / r"basin\map_image\om_weight"

# --- เพิ่ม Path สำหรับฝนคาดการณ์อุตุฯ (TMD Forecast) ---
ONEMAP_TMD_REGION_DIR = ONEMAP_BASE_DIR / r"region\map_image\tmd_region"
ONEMAP_TMD_COUNTRY_DIR = ONEMAP_BASE_DIR / "one_map"

# --- 3.4 Observed monthly rasters & TMD forecast rasters ---
OBS_MONTHLY_RASTER_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\TMD\Raster\observation 1 km\ascii"
TMD_FCST_RASTER_DIR    = ONEDRIVE_DATA_DIR / r"OneMap\data\tmd_fcst"

# --- 3.5 Difference (ผลต่าง Observe vs Forecast) ---
DIFF_OBS_FCST_DIR = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\difference\Observe_Forecast"
DIFF_THAILAND_DIR = DIFF_OBS_FCST_DIR / "Thailand"
DIFF_REGION_DIR       = DIFF_OBS_FCST_DIR / "Region"
DIFF_REGION_EXCEL_DIR = DIFF_REGION_DIR / "Excel"
DIFF_BASIN_EXCEL_DIR  = DIFF_OBS_FCST_DIR / "Basin" / "Excel"

# --- 3.6 One Map CSV data (region/basin forecast + anomaly by LOWER/MEAN/UPPER) ---
ONEMAP_REGION_CSV_DIR = ONEMAP_BASE_DIR / "region" / "csv_file"
ONEMAP_BASIN_CSV_DIR  = ONEMAP_BASE_DIR / "basin"  / "csv_file"

# --- 3.8 Extracted Excel fallback (output from extract_rain_to_excel) ---
EXTRACT_RAIN_EXCEL_DIR = HII_DRIVE / "extract_rain_to_excel" / "outputs" / "extract"

# --- 3.7 TMD Excel Monthly data (avg30y + observed monthly) ---
_TMD_EXCEL_MONTHLY_DIR  = ONEDRIVE_DATA_DIR / r"Rainfall\Interpolation\TMD\Excel\Monthly"
AVG30Y_REGION_CSV       = _TMD_EXCEL_MONTHLY_DIR / "avg30y_update202111" / "avg30y_2020_update202111_region.csv"
AVG30Y_BASIN_CSV        = _TMD_EXCEL_MONTHLY_DIR / "avg30y_update202111" / "avg30y_2020_update202111_basin.csv"
MONTHLY_RAIN_REGION_CSV = _TMD_EXCEL_MONTHLY_DIR / "monthlyrain_region.csv"
MONTHLY_RAIN_BASIN_CSV  = _TMD_EXCEL_MONTHLY_DIR / "monthlyrain_basin.csv"