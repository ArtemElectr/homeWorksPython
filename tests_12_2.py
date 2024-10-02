import runner_and_tournament as rt
import unittest as ut

# Дополнительно: если передавать в объект Tournament бегунов не в порядке уменьшения их скорости от большого к малому,
# например в начале бегун Андрей со скоростью 9, а потом бегун Усейн со скоростью 10, и при этом дистанция будет
# допустим 11, то бегун Андрей пробежит быстрее дистанцию с меньшей скоростью. Я изменил метод start класса Tournament,
# добавил метод sort, который отсортировывает список бегунов по их скорости от большего к меньшему. Также добавил в
# класс Runner метод __gt__, который сравнивает скорости бегунов, а также добавил новый тест, который проверяет, чтобы
# бегуны добавлялись в объект Tournament по порядку уменьшения скорости от большей к меньшей


class TournamentTest(ut.TestCase):
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    def test_run1(self):
        trn = rt.Tournament(90, self.runner_1, self.runner_3)
        self.assertTrue(self.runner_1 > self.runner_3)
        TournamentTest.all_results.update({'trn1': trn.start()})
        self.assertTrue(TournamentTest.all_results['trn1'][2] == self.runner_3)


    def test_run2(self):
        trn = rt.Tournament(90, self.runner_2, self.runner_3)
        self.assertTrue(self.runner_2 > self.runner_3)
        TournamentTest.all_results.update({'trn2': trn.start()})
        self.assertTrue(TournamentTest.all_results['trn2'][2] == self.runner_3)

    def test_run3(self):
        trn = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.assertTrue(self.runner_1 > self.runner_2)
        self.assertTrue(self.runner_2 > self.runner_3)
        TournamentTest.all_results.update({'trn3': trn.start()})
        self.assertTrue(TournamentTest.all_results['trn3'][3] == self.runner_3)

    @classmethod
    def tearDownClass(cls):
        for trn in cls.all_results.values():
            print(trn)


if __name__ == "__main__":
    ut.main()