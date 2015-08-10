import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/relative')
import color
import assertMy
import relativeRequireIced_model

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		sourceFileContent = """replicaSetConfig = require './replicaSetConfig.iced'
mdb_replicaSet = require 'mdb/util/mdb_replicaSet.iced'
th = require 'throw'

module.exports = (autocb)->

    [hostPortArr, replicaSetName, dbname, localPort, useLocalDb] = replicaSetConfig()

    await mdb_replicaSet hostPortArr, replicaSetName, dbname, localPort, useLocalDb, defer result
    [err, db] = result
    th.err err
   
    return [err, db]

    """
		result = relativeRequireIced_model.getPositionInSourceWhereToPaste_bySourceFileContent(sourceFileContent)
		expected = 129
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()