import unittest
import turnos


class ResetTurnsTest(unittest.TestCase):

    def test_turnos_farmacia(self):
        farmacia = turnos.turnos_farmacia()

        turno = ""

        for tries in range(0, 51):
            turno = next(farmacia)

        self.assertEqual(turno, "F - 1")

    def test_turnos_perfumeria(self):
        perfumeria = turnos.turnos_perfumeria()

        turno = ""

        for tries in range(0, 51):
            turno = next(perfumeria)

        self.assertEqual(turno, "P - 1")

    def test_turnos_cosmeticos(self):
        cosmeticos = turnos.turnos_cosmeticos()

        turno = ""

        for tries in range(0, 51):
            turno = next(cosmeticos)

        self.assertEqual(turno, "C - 1")


if __name__ == '__main__':
    unittest.main()
