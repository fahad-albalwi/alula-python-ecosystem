import unittest
from alula_cropwatch import ndvi,ndmi,summarize_field
from alula_waterwise import fao56_et0,irrigation_budget,groundwater_trend,rain_summary
from alula_heritage import attractions,search,plan_day
class TestLibrary(unittest.TestCase):
    def test_indices(self):
        self.assertAlmostEqual(ndvi(.6,.2),.5)
        self.assertAlmostEqual(ndmi(.6,.2),.5)
        self.assertIsNone(ndvi(0,0))
        self.assertEqual(summarize_field([{'B04':.2,'B08':.6,'B11':.2}])['pixel_count'],1)
    def test_et0(self):
        self.assertGreater(fao56_et0(20,35,40,2,14),0)
        with self.assertRaises(ValueError): fao56_et0(35,20,40,2,14)
    def test_budget(self):
        self.assertAlmostEqual(irrigation_budget(5,1,1000,1,.8)['gross_irrigation_m3'],5)
    def test_well(self):
        self.assertEqual(groundwater_trend([('2026-01-01',10),('2026-02-01',11)])['interpretation'],'water_table_lower')
        self.assertEqual(rain_summary([0,2,3])['total_mm'],5)
    def test_tourism(self):
        self.assertTrue(search('Dadan'))
        self.assertTrue(attractions('heritage'))
        self.assertLessEqual(plan_day(180)['visit_minutes'],180)
if __name__=='__main__':unittest.main()
