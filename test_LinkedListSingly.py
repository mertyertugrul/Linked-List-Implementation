import unittest
from LinkedListSingly import *

class MyTestCase(unittest.TestCase):
    def test_linked_list_singly(self):
        linkin = LinkedListSingly(10)
        linkin.append(20)
        linkin.append(30)
        linkin.append(40)
        linkin.append(50)
        linkin.append(60)
        self.assertEqual('head: 10=> 20=> 30=> 40=> 50=> tail: 60', str(linkin))
        linkin.prenend(5)
        self.assertEqual('head: 5=> 10=> 20=> 30=> 40=> 50=> tail: 60', str(linkin))
        self.assertEqual(3, linkin.search(30))
        linkin.delete(3)
        self.assertEqual('head: 5=> 10=> 20=> 40=> 50=> tail: 60', str(linkin))



if __name__ == '__main__':
    unittest.main()
