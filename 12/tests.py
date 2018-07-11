import unittest
from Cache import Cache

class CacheCase(unittest.TestCase):
	def test_cache_store_elements_hits(self):
		cache = Cache(5, 1)
		cache.put('key1', 'value1');
		cache.put('key2', 'value2');
		cache.put('key3', 'value3');
		cache.put('key4', 'value4');
		cache.put('key5', 'value5');

		hits_plan = {'key1': 5, 'key2': 4, 'key3': 3, 'key4': 2, 'key5': 1}

		for key, value in hits_plan.items():
			for _ in range(value):
				cache.get(key)

		self.assertEqual(5, cache.hits[3])
		self.assertEqual(4, cache.hits[4])
		self.assertEqual(3, cache.hits[0])
		self.assertEqual(2, cache.hits[1])
		self.assertEqual(1, cache.hits[2])

	def test_cache_delete_least_popular_elements(self):
		cache = Cache(3, 1)
		cache.put('key1', 'value1');
		cache.put('key2', 'value2');
		cache.put('key3', 'value3');

		hits_plan = {'key1': 2, 'key2': 6, 'key3': 3}

		for key, value in hits_plan.items():
			for _ in range(value):
				cache.get(key)

		cache.put('key4', 'value4');		

		self.assertFalse(cache.is_key('key1'))
		self.assertTrue(cache.is_key('key4'))

if __name__ == '__main__':
	unittest.main(verbosity=2)		