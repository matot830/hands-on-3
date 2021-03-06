import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units
from asap3 import EMT


class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        # Set up a crystal
        size=5
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                            symbol="Cu",
                            size=(size, size, size),
                            pbc=True)
        atoms.calc = EMT()
        l = calcenergy(atoms)
        print(l)
        self.assertAlmostEqual(l[3], -0.0006011545839360579)



if __name__ == '__main__':

    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
