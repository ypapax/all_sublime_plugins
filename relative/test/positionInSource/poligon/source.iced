replicaSetConfig = require './replicaSetConfig.iced'
mdb_replicaSet = require 'mdb/util/mdb_replicaSet.iced'
th = require 'throw'

module.exports = (autocb)->

    [hostPortArr, replicaSetName, dbname, localPort, useLocalDb] = replicaSetConfig()

    await mdb_replicaSet hostPortArr, replicaSetName, dbname, localPort, useLocalDb, defer result
    [err, db] = result
    th.err err
   
    return [err, db]