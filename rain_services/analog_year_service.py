# ฟังก์ชันสำหรับอ่านปีเหมือนจาก CSV

# rain_services\analog_year_service.py
import csv
from pathlib import Path

# หากรันจากโปรเจคย่อย สามารถ import config ได้
# สมมติว่าโครงสร้างโปรเจคอยู่ในระดับเดียวกัน
from rain_services.config import ANALOG_YEARS_CSV_PATH

class AnalogYearService:
    def __init__(self, csv_path: Path | str = ANALOG_YEARS_CSV_PATH):
        self.csv_path = Path(csv_path)
        self._analog_data = self._load_data()

    def _load_data(self) -> dict[tuple[int, int], int]:
        """
        อ่านไฟล์ CSV และแปลงเป็น Dictionary
        รูปแบบคีย์: (target_year, init_month) -> ค่า: analog_year
        """
        data = {}
        if not self.csv_path.exists():
            raise FileNotFoundError(f"ไม่พบไฟล์ CSV ปีเหมือน (Analog Years) ที่: {self.csv_path}")
        
        with open(self.csv_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    t_year = int(row['target_year'])
                    i_month = int(row['init_month'])
                    a_year = int(row['analog_year'])
                    data[(t_year, i_month)] = a_year
                except ValueError as e:
                    print(f"พบข้อมูลที่ไม่ใช่ตัวเลขในไฟล์ CSV ข้ามบรรทัดนี้: {row}")
                    continue
                    
        return data

    def get_analog_year(self, target_year: int, init_month: int) -> int:
        """
        ดึงข้อมูลปีเหมือน จากปีและเดือนที่ต้องการคาดการณ์
        """
        key = (target_year, init_month)
        if key not in self._analog_data:
            raise ValueError(
                f"ไม่พบข้อมูลปีเหมือนสำหรับ ปีเป้าหมาย {target_year} "
                f"เดือนเริ่มต้น {init_month} ในไฟล์ CSV"
            )
        return self._analog_data[key]

# ==========================================
# ตัวอย่างการเรียกใช้งาน
# ==========================================
if __name__ == "__main__":
    try:
        service = AnalogYearService()
        
        # สมมติว่าต้องการหาปีเหมือนของ target_year=2566, init_month=3
        analog_yr = service.get_analog_year(2566, 3)
        print(f"ปีเหมือนคือ: {analog_yr}")
        
    except Exception as e:
        print(f"Error: {e}")