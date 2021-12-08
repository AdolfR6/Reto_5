import unittest
from model.Geometria import Geometria as G

g=G(1,1,1)


class Mis_test(unittest.TestCase):
    def setUp(self):
        self.r=[]
        self.valores_a=[1,2,3,4]
        self.valores_b= [5,6,7,8]
        self.valores_c = [2,4,6,8]

    def test_areaCuadrado(self):
        r=[g.areaCuadrado(n) for n in self.valores_a]
        self.assertEqual(r, [1,4,9,16])
        print("Prueba areaCuadrado realizada")

    def test_areaCirculo(self):
        r=[g.areaCirculo(n) for n in self.valores_a]
        self.assertEqual(r, [3.1416,12.5664,28.2744,50.2656])
        print("Prueba areaCirculo realizada")

    def test_areaTiangulo(self):
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(g.areaTiangulo(valor_a,valor_b))

        self.assertEqual(self.r,[2.5,6,10.5,16])
        print("Prueba areaTriangulo realizada")

    def test_areaRectangulo(self):
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(g.areaRectangulo(valor_a,valor_b))

        self.assertEqual(self.r,[5,12,21,32])
        print("Prueba areaRectangulo realizada")

    def test_areaPentagono(self):
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(g.areaPentagono(valor_a,valor_b))

        self.assertEqual(self.r,[2.5,6,10.5,16])
        print("Prueba areaPentagono realizada")

    def test_areaRombo(self):
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(g.areaRombo(valor_a,valor_b))

        self.assertEqual(self.r,[2.5,6,10.5,16])
        print("Prueba areaRombo realizada")

    def test_areaRomboide(self):
        for valor_a, valor_b in zip(self.valores_a, self.valores_b):
            self.r.append(g.areaRomboide(valor_a,valor_b))

        self.assertEqual(self.r,[5,12,21,32])
        print("Prueba areaRomboide realizada")

    def test_areaTrapecio(self):
        for valor_a, valor_b, valor_c in zip(self.valores_a, self.valores_b,self.valores_c):
            self.r.append(g.areaTrapecio(valor_a,valor_b,valor_c))

        self.assertEqual(self.r,[6, 16, 30, 48])
        print("Prueba areaTrapecio realizada")

    def test_set_figuraName(self):

        self.assertIsNone(g.set_figuraName(10))
        print("Prueba set_figuraName realizada")

    def test_switch(self):

        self.assertEqual(g.switch(1),1)
        print("Prueba switch realizada")

    def tearDown(self):
        del self.valores_a
        del self.valores_b
        del self.r

if __name__=='__main__':
    unittest.main()

