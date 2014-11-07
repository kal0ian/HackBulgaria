from weapon import Weapon
import unittest


class WeaponTest(unittest.TestCase):

    def setUp(self):
        self.w = Weapon("axe", 50, 0.4)

    def test_init(self):
        self.assertEqual(self.w.type, "axe")
        self.assertEqual(self.w.demage, 50)
        self.assertEqual(self.w.critical_strike_percent, 0.4)
        with self.assertRaises(ValueError):
            self.weapon = Weapon("axe", 50, 2)

    def test_critical_hit(self):
        arr = []
        flag = [False, False]
        for i in range(1, 100):
            arr.append(self.w.critical_hit())

        for i in arr:
            if i:
                flag[0]=True
            else:
                flag[1]=True

if __name__ == '__main__':
    unittest.main()
