#! /usr/bin/python

import timeit
import msgpack
import umsgpack
import json

my_object = {"array":[1,2,3],"boolean":True,"null":None,"number":123,"object":{"a":"b","c":"d","e":"f"},"string":"Hello World"}
packed = msgpack.packb(my_object)
upacked = umsgpack.packb(my_object)

def test_a(packed):
    unpacked = msgpack.unpackb(packed, use_list=True)

def test_b(packed):
    unpacked = msgpack.unpackb(packed, use_list=False)

def test_c(packed):
    unpacked = umsgpack.unpackb(packed)

if __name__ == '__main__':

    assert msgpack.unpackb(packed, use_list=True) == my_object
    assert umsgpack.unpackb(upacked) == my_object
    assert umsgpack.unpackb(packed) == my_object

    # Not identical output - use_list false uses tuples internally which results in non-symmertical output
    #assert msgpack.unpackb(packed, use_list=False) == my_object

    print "Functional comparison succeeded. Checking t_10^6 operations..."

    print (timeit.timeit('test_a(packed)', setup="from __main__ import test_a, packed"))
    print (timeit.timeit('test_b(packed)', setup="from __main__ import test_b, packed"))
    print (timeit.timeit('test_c(upacked)', setup="from __main__ import test_c, upacked"))
