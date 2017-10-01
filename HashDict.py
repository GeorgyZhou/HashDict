#coding:utf8
#	Author: Michael Zhou
#	version: 1.0
#	Description: Hash dictionary implemented by open addressing.

class HashDict(object):
    def __init__(self, size):
        """Constructor for hashDict.

        Args:
            size: An int value indicating slots number.
        """
        if not isinstance(size, int) or size <= 0:
            raise ValueError('Invalid Size!')
        self.container = [None for _ in range(size)]
        self.size = size
        self.occupied = 0

        # DUMMY is used to mark the slots that are being deleted
        self.DUMMY = None

    def __delitem__(self, key):
        """Deletes the value associated with the given key.

        Rewrites del operation on '[]'

        Args:
            key: A string to be deleted from the hash dictionary.

        Returns:
            Returns the value if successfully deletes the key otherwise none.
        """
        return self.delete(key)

    def __getitem__(self, key):
        """Gets the value associated with the given key.

        Rewrites '[]' operation

        Args:
            key: A string to be retrieved from the hash dictionary.

        Returns:
            None
        """
        self.get(key)

    def __setitem__(self, key, value):
        """Sets the value associated with the given key.

        Rewrites '[]' operation.

        Args:
            key: A string to index the key/value pair.
            value: A Object instance to be stored in the dictionary.

        Returns:
            Returns a boolean value indicating success / failure of
            the operation.
        """
        return self.set(key, value)

    def set(self, key, value):
        """Sets the value associated with the given key.

        Stores the given key/value pair in the hash map. Returns a
        boolean value indicating success / failure of the operation.

        Args:
            key: A string to index the key/value pair.
            value: A Object instance to be stored in the dictionary.

        Returns:
            Returns a boolean value indicating success / failure of
            the operation.
        """
        slot_index = self._openAddressing(key)
        if slot_index is None:
            return False
        if self.container[slot_index] is None or self.container[slot_index][0] is self.DUMMY:
            self.occupied += 1
        self.container[slot_index] = (key, value)
        return True

    def get(self, key):
        """Gets the value associated with the given key.

        Returns the value associated with the given key, or null if no
        value is set.

        Args:
            key: A string to be retrieved from the hash dictionary.

        Returns:
            Returns the value associated with the given key if it
            exists in dictionary or null.
        """
        slot_index = self._getSlot(key)
        return None if slot_index is None else self.container[slot_index][1]

    def delete(self, key):
        """Deletes the value associated with the given key.

        Deletes the value associated with the given key, returning the
        value on success or null if the key has no value.

        Args:
            key: A string to be deleted from the hash dictionary.

        Returns:
            Returns the value if successfully deletes the key otherwise none.
        """
        slot_index = self._getSlot(key)
        if slot_index is None:
            return None
        ret_val = self.container[slot_index][1]
        self.container[slot_index] = (self.DUMMY, self.DUMMY)
        self.occupied -= 1
        return ret_val

    def load(self):
        """Returns a float value indicating data structure load.

        Returns a float value representing the load factor
        (`(items in hash map)/(size of hash map)`) of the data structure.
        Since the size of the dat structure is fixed, this should never
        be greater than 1.

        Returns:
            A float number to indicate the load factor.
        """
        return float(self.occupied) / float(self.size)

    def _getSlot(self, key):
        """Gets the address of the given key.

        Args:
            key: A string to be used to index key/value pair.

        Returns:
            If there's an index return it else none.
        """
        is_probing = False
        initial_index = hash(key) % self.size
        slot = initial_index
        while not self._isCircled(slot, initial_index, is_probing):
            pair = self.container[slot]
            if pair is None:
                return None
            if pair[0] is not self.DUMMY and (pair[0] is key or pair[0] == key):
                return slot
            slot = (slot + 1) % self.size
            is_probing = True
        return None

    def _isCircled(self, cur_index, initial_index, is_probing):
        """Check probing has traversed all the slots or not.

        Args:
            cur_index: int indicating the current probing index.
            initial_index: int indicating the starting index.
            is_probing: boolean indicating is probing or not.

        Returns:
            Boolean indicating probing has traversed all the slots or not.
        """
        return  is_probing and cur_index == initial_index

    def _openAddressing(self, key):
        """Gets the first available address for the given key or an available slot.

        Args:
            key: A string to be used to index key/value pair.

        Returns:
            Returns a int as the addressing index if possible. Otherwise returns none.
        """
        dummy_slot = None

        # A

        is_probing = False
        initial_index = hash(key) % self.size
        slot = initial_index

        # Probes the next slot until:
        # 1. We find a null slot inside the dictionary.
        # 2. We find a slot whose key is the same as the key.
        # 3. We have already traversed all the slots of the dictionary.
        while self.container[slot] is not None and self.container[slot][0] != key:
            if self._isCircled(slot, initial_index, is_probing):
                break
            if dummy_slot is None and self.container[slot][0] is self.DUMMY:
                dummy_slot = slot
            slot = (slot + 1) % self.size
            is_probing = True

        # If we don't find any slot to store the new key, which means:
        # 1. No dummy slot (slot which is deleted before) found.
        # 2. No null slot is found.
        # 3. No slot whose key is the same as the input key is found.
        # then return None.
        if dummy_slot is None and self.container[slot] is not None and self.container[slot][0] != key:
            return None

        if self.container[slot] is not None and dummy_slot is not None:
            return dummy_slot
        return slot
