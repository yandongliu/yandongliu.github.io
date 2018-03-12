---
layout: post
title:  "SQL on Hadoop Comparison"
date:   2017-08-27 17:12:22 -0800
categories: hadoop sql big_data
---

SQL on Hadoop Comparison

The contestants: Hive, Spark, HBase, Impala, Presto, Kylin.

Contestant | Purpose | Latency | Scalability | Query Engine| Use cases | s
-- | -- | --
Hive | SQL engine on HDFS | Medium | High | MapReduce | xx | Read Only | Pre-defined table schemas|
Spark | Low | Low
Presto |
HBase | Key-Value Store on HDFS | Real-time
Impala |
Kylin | OLAP

Cassandra |
MongoDB |

There is no view/controller components. All such work should happen on frontend.

### An example Python backend structure:

#### Handler
aa
