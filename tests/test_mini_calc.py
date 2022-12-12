from app.mini_calc import Mini_Calc


class Test_Mini_Calc:
    def setup_method(self):
        print("Is executed at the beginning.")
        self.calc = Mini_Calc(4, 4)

    def teardown_method(self):
        print("Is executed at the end.")

    def test_init(self):
        assert self.calc.a == 4, 'a is not correct'
        assert self.calc.b == 4, 'b is not correct'

    def test_sum(self):
        assert self.calc.sum() == 8, 'sum is doesn t properly'

    def test_dif(self):
        assert self.calc.dif() == 0, 'difference is doesn t properly'

    def test_multi(self):
        assert self.calc.multi() == 16, 'multiplication is doesn t properly'

    def test_divi(self):
        assert self.calc.divi() == 1, 'division is doesn t properly'