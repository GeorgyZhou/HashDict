from HashDict import HashDict
from unittest import TestCase

class TestHashDict(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def runTest(self):
        self.testSet()
        self.testLoad()
        self.testGet()
        self.testDelete()
        print '[PASSED]: All test cases passed!'

    def testSet(self):
        a = HashDict(10)
        for i in range(10):
            self.assertTrue(a.set('test' + str(i), 'test' + str(i)))
        self.assertFalse(a.set('cannot be written', 'cannot be written'))
        for i in range(10):
            self.assertEqual(a.get('test'+ str(i)),  'test' + str(i))

    def testLoad(self):
        a = HashDict(400)
        self.assertEqual(a.load(), 0.0)
        for i in range(200):
            a.set('test' + str(i), 'test' + str(i))
        self.assertEqual(a.load(), 0.5)
        for i in range(200, 250):
            a.set('test' + str(i), 'test' + str(i))
        self.assertEqual(a.load(), 0.625)
        for i in range(250, 400):
            a.set('test' + str(i), 'test' + str(i))
        self.assertEqual(a.load(), 1.0)

    def testGet(self):
        a = HashDict(59)
        for i in range(59):
            a.set( str(i) + 'test' + str(i), 'test' + str(i))
        for i in range(59):
            self.assertEqual(a.get(str(i) + 'test' + str(i)), 'test' + str(i))
        self.assertIsNone(a.get('Invalid Key'))

    def testDelete(self):
        a = HashDict(17)
        for i in range(17):
            a.set('test' + str(i), 'test' + str(i))
        for i in range(17):
            self.assertEqual(a.delete('test' + str(i)), 'test' + str(i))
        self.assertIsNone(a.delete('Invalid Key'))
        for i in range(17):
            a.set(str(i) + 'newtest' + str(i), 'newtest' + str(i))
        for i in range(17):
            self.assertEqual(a.delete( str(i) + 'newtest' + str(i)), 'newtest' + str(i))
        self.assertIsNone(a.delete('Invalid Key'))

if __name__ == '__main__':
    test = TestHashDict()
    test.runTest()
