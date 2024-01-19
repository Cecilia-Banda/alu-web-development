#!/usr/bin/python3
"""
    BaseCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a simple caching system

      To use:
      >>> my_cache = BasicCache()
      >>> my_cache.print_cache()
      Current cache:

      >>> my_cache.put("A", "Hello")
      >>> my_cache.print_cache()
      A: Hello

      >>> print(my_cache.get("A"))
      Hello
    """

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: Key to identify the item.
            item: Value to be stored in the cache.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key: Key to retrieve the item.

        Returns:
            Value of the key in the cache or None if key is not found.
        """
        value_cache = self.cache_data.get(key)
        return value_cache
