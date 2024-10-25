class DiscriminantTest(unittest.TestCase):

    def test_positive_discriminant(self):
        self.assertEqual(calculate_discriminant(1, -5, 6), 1)
        self.assertEqual(calculate_discriminant(1, 4, 3), 4)

    def test_negative_discriminant(self):
        self.assertEqual(calculate_discriminant(1, 2, 3), -8)
        self.assertEqual(calculate_discriminant(1, 1, 1), -3)

if __name__ == '__main__':
    unittest.main()
