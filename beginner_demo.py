"""Beginner-friendly Arabic menu. Run: python beginner_demo.py"""
import unittest
import sys
from pathlib import Path

# Allow a beginner to run the bundled source without installing anything.
ROOT = Path(__file__).resolve().parent
for package_dir in ("alula_cropwatch", "alula_waterwise", "alula_heritage"):
    sys.path.insert(0, str(ROOT / package_dir))

from alula_cropwatch import ndvi, ndmi, summarize_field
from alula_waterwise import fao56_et0, irrigation_budget
from alula_heritage import attractions, plan_day


def crop_demo():
    print("\n[1] مراقبة مزرعة نخيل - بيانات افتراضية")
    pixels = [
        {"B04": 0.12, "B08": 0.51, "B11": 0.24},
        {"B04": 0.19, "B08": 0.43, "B11": 0.31},
    ]
    result = summarize_field(pixels)
    print("عدد نقاط القياس:", result["pixel_count"])
    print("متوسط NDVI:", result["mean_ndvi"])
    print("متوسط NDMI:", result["mean_ndmi"])
    print("مثال حساب فردي NDVI:", round(ndvi(0.6, 0.2), 3))
    print("تنبيه: ليست قراءة حقيقية من العلا ولا تشخيصاً لأمراض النخيل.")


def water_demo():
    print("\n[2] تقدير المياه - بيانات جوية افتراضية")
    et0 = fao56_et0(21, 36, 35, 2, 13)
    print("البخر-نتح المرجعي ET0:", et0, "ملم/يوم")
    for area in (1000, 2000):
        result = irrigation_budget(et0, crop_coefficient=0.9, area_m2=area)
        print(f"المساحة {area} م²: {result['gross_irrigation_m3']} م³/يوم تقريباً")
    print("تنبيه: ليست توصية ري لمزرعة حقيقية؛ يلزم بيانات محلية ومعايرة.")


def heritage_demo():
    print("\n[3] وجهات العلا - دليل غير متصل بالإنترنت")
    for site in attractions():
        print("-", site["name_ar"], f"({site['suggested_minutes']} دقيقة افتراضية)")
    route = plan_day(240)
    print("عدد الوجهات المختارة لميزانية 240 دقيقة:", len(route["sites"]))
    print("تنبيه: لا تشمل الخطة زمن التنقل أو توفر الزيارات والحجوزات.")


def tests_demo():
    print("\n[4] تشغيل الاختبارات الآلية")
    folder = Path(__file__).resolve().parent / "tests"
    suite = unittest.defaultTestLoader.discover(str(folder), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("النتيجة:", "ناجح" if result.wasSuccessful() else "يوجد اختبار فاشل")


def main():
    print("=" * 48)
    print("AlUla Python Libraries | FAHAD SAAD ALBALWI")
    print("إصدار تعليمي للمبتدئين — البيانات تجريبية")
    while True:
        print("\n1 - مراقبة المحاصيل")
        print("2 - حساب احتياج الري")
        print("3 - السياحة والتراث")
        print("4 - تشغيل الاختبارات")
        print("0 - خروج")
        choice = input("اختر رقمًا: ").strip()
        if choice == "0":
            print("إلى اللقاء")
            break
        action = {"1": crop_demo, "2": water_demo, "3": heritage_demo, "4": tests_demo}.get(choice)
        if action is None:
            print("اختيار غير صحيح؛ جرّب 0 أو 1 أو 2 أو 3 أو 4.")
        else:
            action()


if __name__ == "__main__":
    main()
