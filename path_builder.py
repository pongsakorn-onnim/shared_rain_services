# src/core/path_builder.py
from pathlib import Path
import config
from analog_year_service import AnalogYearService

class RainPathBuilder:
    def __init__(self, analog_service: AnalogYearService):
        self.analog_service = analog_service

    # ==========================================
    # 1. ค่าเฉลี่ย 30 ปี
    # ==========================================
    def build_avg30y_yearly(self) -> Path:
        """ค่าเฉลี่ย 30 ปี รายปี (ชื่อไฟล์คงที่)"""
        return config.AVG30Y_DIR / "avg30y_update202111.png"

    # ==========================================
    # 2. ฝนคาดการณ์ สสน. (อิงปีเหมือนจาก csv)
    # ==========================================
    def build_hii_forecast_yearly(self, target_year: int, init_year: int, init_month: int, is_diff: bool = False) -> Path:
        """ฝนคาดการณ์รายปี สสน."""
        suffix = "d" if is_diff else ""
        filename = f"HII_th{target_year}_init{init_year}{init_month:02d}{suffix}.png"
        return config.HII_FCST_DIR / filename

    def build_hii_forecast_path(self, init_year: int, init_month: int, target_year: int, target_month: int, is_diff: bool = False, area: str = "region") -> Path:
        """สร้าง Path ฝนคาดการณ์ สสน. 1 ภาพ (อิงปีเหมือน)"""
        # ดึงปีเหมือนที่เป็นฐาน 
        analog_base_year = self.analog_service.get_analog_year(init_year, init_month)
        
        # คำนวณปี analog สำหรับเป้าหมาย (รองรับกรณี target_year ข้ามปีไปแล้ว)
        current_analog_year = analog_base_year + (target_year - init_year)
        
        base_dir = config.OBS_REGION_DIR if area == "region" else config.OBS_BASIN_DIR
        suffix = "d" if is_diff else ""
        filename = f"o_th{current_analog_year}{target_month:02d}{suffix}.png"
        
        return base_dir / str(current_analog_year) / filename

    # ==========================================
    # 3. ฝนคาดการณ์ One Map 
    # ==========================================
    def build_onemap_path(self, init_year: int, init_month: int, target_year: int, target_month: int, model_type: str = "MFCST", is_diff: bool = False, area: str = "region") -> Path:
        """
        สร้าง Path ฝนคาดการณ์ One Map 1 ภาพ
        model_type: MFCST (Mean), UFCST (Upper), LFCST (Lower)
        """
        base_dir = config.ONEMAP_REGION_DIR if area == "region" else config.ONEMAP_BASIN_DIR
        parent_folder = f"{init_year}{init_month:02d}"
        suffix = "d" if is_diff else ""
        
        filename = f"OM_{model_type}_{target_year}{target_month:02d}{suffix}.png"
        return base_dir / parent_folder / filename

    # ==========================================
    # 4. ฝนคาดการณ์อุตุฯ (TMD Forecast)
    # ==========================================
    def build_tmd_forecast_path(self, init_year: int, init_month: int, target_year: int, target_month: int, is_diff: bool = False, area: str = "region") -> Path:
        """สร้าง Path ฝนคาดการณ์อุตุฯ (TMD) 1 ภาพ"""
        if area == "region":
            base_dir = config.ONEMAP_TMD_REGION_DIR
        elif area == "country":
            base_dir = config.ONEMAP_TMD_COUNTRY_DIR
        else:
            raise ValueError(f"ฝนคาดการณ์อุตุฯ ไม่รองรับขอบเขตพื้นที่: {area}")
            
        parent_folder = f"{init_year}{init_month:02d}"
        suffix = "d" if is_diff else ""
        filename = f"forecast_TMD_{target_year}{target_month:02d}{suffix}.png"
        
        return base_dir / parent_folder / filename

    # ==========================================
    # 5. ฝนตรวจวัด 
    # ==========================================
    def build_obs_path(self, target_year: int, target_month: int, is_diff: bool = False, area: str = "region") -> Path:
        """ฝนตรวจวัดรายเดือน หรือ ผลต่างเทียบค่าเฉลี่ย 30 ปี"""
        base_dir = config.OBS_REGION_DIR if area == "region" else config.OBS_BASIN_DIR
        suffix = "d" if is_diff else ""
        filename = f"o_th{target_year}{target_month:02d}{suffix}.png"
        return base_dir / str(target_year) / filename

    # ==========================================
    # 6. ผลต่างเทียบฝนตรวจวัด (รายเดือน และ กรณีพิเศษรายปี)
    # ==========================================
    def build_diff_obs_vs_forecast_path(self, target_year: int, target_month: int, model: str) -> Path:
        """
        ผลต่าง ฝนตรวจวัด vs คาดการณ์ (สสน, อุตุฯ, One Map)
        model: "HII", "TMD", "OM"
        """
        filename = f"o_th{target_year}{target_month:02d}d{model}-region.png"
        
        folder_map = {
            "HII": "Observe_HIIforecast",
            "TMD": "Observe_TMDforecast",
            "OM": "Observe_OMforecast"
        }
        subfolder = folder_map.get(model, "")
        return config.DIFF_REGION_DIR / subfolder / str(target_year) / filename

    def build_diff_obs_yearly_jan_report(self, obs_year: int, report_year: int, compare_to: str = "HII") -> Path:
        """
        [กรณีพิเศษฉบับ ม.ค.] ผลต่างฝนตรวจวัดรายปี
        compare_to: "HII" (เทียบ สสน.) หรือ "AVG30Y" (เทียบค่าเฉลี่ย 30 ปี)
        """
        if compare_to == "HII":
            filename = f"o_th{obs_year}dHII.png"
            return config.DIFF_THAILAND_DIR / "Observe_HIIforecast" / str(report_year) / filename
        elif compare_to == "AVG30Y":
            filename = f"o_th{obs_year}d.png"
            return config.OBS_ANOMALY_DIR / str(obs_year) / filename
            
        raise ValueError(f"ไม่รองรับการเปรียบเทียบกับ: {compare_to}")

# ==========================================
# ส่วนจำลองการรันทดสอบ (จะไม่ทำงานหากถูก Import)
# ==========================================
if __name__ == "__main__":
    # 1. สร้าง Mock Service เพื่อจำลองว่าอ่านค่าจาก CSV ได้ปี 2012
    class MockAnalogService:
        def get_analog_year(self, t_yr, i_mo): 
            return 2012 # ตัวแทนของปี 2555

    builder = RainPathBuilder(MockAnalogService())

    print("="*60)
    print("TESTING: RainPathBuilder (Initial: 03-2026, Analog: 2012)")
    print("="*60)

    # ------------------------------------------
    print("\n[1] ค่าเฉลี่ย 30 ปี")
    # ------------------------------------------
    print(f"รายปี: {builder.build_avg30y_yearly()}")

    # ------------------------------------------
    print("\n[2] ฝนคาดการณ์ สสน.")
    # ------------------------------------------
    print(f"รายปี (ปกติ): {builder.build_hii_forecast_yearly(2026, 2026, 3)}")
    print(f"รายปี (ผลต่าง): {builder.build_hii_forecast_yearly(2026, 2026, 3, is_diff=True)}")
    
    print(f"รายเดือน t1 (Region): {builder.build_hii_forecast_path(2026, 3, 2026, 3, area='region')}")
    print(f"รายเดือน t2 (Region, ผลต่าง): {builder.build_hii_forecast_path(2026, 3, 2026, 4, is_diff=True, area='region')}")
    print(f"รายเดือน t1 (Basin): {builder.build_hii_forecast_path(2026, 3, 2026, 3, area='basin')}")
    print(f"รายเดือน t6 (Basin, ผลต่าง): {builder.build_hii_forecast_path(2026, 3, 2026, 8, is_diff=True, area='basin')}")

    # ------------------------------------------
    print("\n[3] ฝนคาดการณ์ One Map")
    # ------------------------------------------
    print(f"Mean t1 (Region): {builder.build_onemap_path(2026, 3, 2026, 3, model_type='MFCST', area='region')}")
    print(f"Mean t2 (Region, ผลต่าง): {builder.build_onemap_path(2026, 3, 2026, 4, model_type='MFCST', is_diff=True, area='region')}")
    
    print(f"Upper t1 (Basin): {builder.build_onemap_path(2026, 3, 2026, 3, model_type='UFCST', area='basin')}")
    print(f"Upper t6 (Basin, ผลต่าง): {builder.build_onemap_path(2026, 3, 2026, 8, model_type='UFCST', is_diff=True, area='basin')}")
    
    print(f"Lower t3 (Region): {builder.build_onemap_path(2026, 3, 2026, 5, model_type='LFCST', area='region')}")

    # ------------------------------------------
    print("\n[4] ฝนตรวจวัด")
    # ------------------------------------------
    print(f"รายเดือน ม.ค. 2026 (Region): {builder.build_obs_path(2026, 1, area='region')}")
    print(f"ผลต่าง ม.ค. 2026 (Region): {builder.build_obs_path(2026, 1, is_diff=True, area='region')}")

    # ------------------------------------------
    print("\n[5] ผลต่าง ฝนตรวจวัด vs คาดการณ์ (รายเดือน)")
    # ------------------------------------------
    print(f"ตรวจวัด vs สสน. (ม.ค. 2026): {builder.build_diff_obs_vs_forecast_path(2026, 1, 'HII')}")
    print(f"ตรวจวัด vs อุตุฯ (ก.พ. 2026): {builder.build_diff_obs_vs_forecast_path(2026, 2, 'TMD')}")
    print(f"ตรวจวัด vs One Map (ธ.ค. 2025): {builder.build_diff_obs_vs_forecast_path(2025, 12, 'OM')}")

    # ------------------------------------------
    print("\n[6] กรณีพิเศษ: รายงานฉบับ ม.ค. (ผลต่างรายปี)")
    # ------------------------------------------
    print(f"ตรวจวัด 2025 vs สสน. (เก็บโฟลเดอร์ 2026): {builder.build_diff_obs_yearly_jan_report(2025, 2026, compare_to='HII')}")
    print(f"ตรวจวัด 2025 vs ค่าเฉลี่ย 30 ปี: {builder.build_diff_obs_yearly_jan_report(2025, 2026, compare_to='AVG30Y')}")

    # ------------------------------------------   
    print("\n[7] ฝนคาดการณ์อุตุฯ")
    # ------------------------------------------ 
    print(f"t1 (Region): {builder.build_tmd_forecast_path(2026, 3, 2026, 3, area='region')}")
    print(f"t6 (Country, ผลต่าง): {builder.build_tmd_forecast_path(2026, 3, 2026, 8, is_diff=True, area='country')}")
    print("="*60)