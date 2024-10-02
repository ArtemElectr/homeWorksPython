import unittest as ut
import tests_12_1 as t1
import tests_12_2 as t2


tournTS = ut.TestSuite()

tournTS.addTest(ut.TestLoader().loadTestsFromTestCase(t1.RunnerTest))
tournTS.addTest(ut.TestLoader().loadTestsFromTestCase(t2.TournamentTest))

runner = ut.TextTestRunner(verbosity=2)

runner.run(tournTS)