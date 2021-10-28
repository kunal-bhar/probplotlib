import unittest

from src import Gaussian
from src import Binomial

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(78.091, 92.875)
        self.gaussian.read_dataset('num.txt')

    def test_initialization(self): 
        self.assertEqual(round(self.gaussian.mean,3), 78.091, 'incorrect mean')
        self.assertEqual(round(self.gaussian.stdev,3), 92.875, 'incorrect standard deviation')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data,\
         [1, 3, 99, 100, 120, 32, 330, 23, 76, 44, 31], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),\
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated mean not as expected')

    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 92.87, 'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 88.55, 'population standard deviation incorrect')
           
    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(25), 5), 0.00365,\
         'pdf function does not give expected result') 
        self.gaussian.calculate_mean()
        self.gaussian.calculate_stdev()
        self.assertEqual(round(self.gaussian.pdf(75), 5), 0.00429,\
        'pdf function after calculating mean and stdev does not give expected result')      

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)
        
class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial(0.615, 13)
        self.binomial.read_dataset('num_binomial.txt')

    def test_initialization(self):
        self.assertEqual(round(self.binomial.p,3), 0.615, 'p value incorrect')
        self.assertEqual(self.binomial.n, 13, 'n value incorrect')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')
    
    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 8)
    
    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev,3),1.754 )
          
    def test_pdf(self):
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)
    
        self.binomial.params()
        self.assertEqual(round(self.binomial.pdf(5), 5), 0.05439)
        self.assertEqual(round(self.binomial.pdf(3), 5), 0.00472)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)
        
    
if __name__ == '__main__':
    unittest.main()