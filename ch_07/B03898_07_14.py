"""README======This file contains Python codes.======"""import pymongotry:    client = pymongo.MongoClient("localhost", 27017)    print "Connected successfully!!!"except pymongo.errors.ConnectionFailure, e:   print "Could not connect to MongoDB: %s" % e