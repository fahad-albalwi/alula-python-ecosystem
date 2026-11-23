import unittest
from alula_cropwatch import ndvi, ndmi, summarize_field
from alula_waterwise import irrigation_budget, rain_summary
from alula_heritage import search, plan_day

class EdgeCaseTests(unittest.TestCase):
    def test_indices_numeric_errors(self):
        with self.assertRaises(ValueError): ndvi(float('nan'), 0.2)
        self.assertAlmostEqual(ndmi(0.7, 0.3), 0.4)
    def test_empty_field(self):
        with self.assertRaises(ValueError): summarize_field([])
    def test_rain_rejects_negative(self):
        with self.assertRaises(ValueError): rain_summary([0, -1])
    def test_efficiency_rejects_zero(self):
        with self.assertRaises(ValueError): irrigation_budget(3,1,100,0,0)
    def test_search_casefold(self):
        self.assertEqual(search('dadan')[0]['id'], 'dadan')
    def test_day_requires_positive_integer(self):
        with self.assertRaises(ValueError): plan_day(0)

if __name__ == '__main__': unittest.main()
