# Part II<!-- omit in toc -->

- [System Research](#system-research)
- [Performance Experiment Design 1](#performance-experiment-design-1)
	- [Performance issue test](#performance-issue-test)
	- [Data sets included in the test](#data-sets-included-in-the-test)
	- [Queries we will run](#queries-we-will-run)
	- [Parameters used/how parameters will be set/varied?](#parameters-usedhow-parameters-will-be-setvaried)
	- [Results expected](#results-expected)
- [Performance Experiment Design 2](#performance-experiment-design-2)
	- [Performance issue test](#performance-issue-test-1)
	- [Data sets included in the test](#data-sets-included-in-the-test-1)
	- [Queries we will run](#queries-we-will-run-1)
	- [Parameters used/how parameters will be set/varied?](#parameters-usedhow-parameters-will-be-setvaried-1)
	- [Results expected](#results-expected-1)
- [Performance Experiment Design 3](#performance-experiment-design-3)
	- [Performance issue test](#performance-issue-test-2)
	- [Data sets included in the test](#data-sets-included-in-the-test-2)
	- [Queries we will run](#queries-we-will-run-2)
	- [Parameters used/how parameters will be set/varied?](#parameters-usedhow-parameters-will-be-setvaried-2)
	- [Results expected](#results-expected-2)
- [Performance Experiment Design 4](#performance-experiment-design-4)
	- [Performance issue test](#performance-issue-test-3)
	- [Data sets included in the test](#data-sets-included-in-the-test-3)
	- [Queries we will run](#queries-we-will-run-3)
	- [Parameters used/how parameters will be set/varied?](#parameters-usedhow-parameters-will-be-setvaried-3)
	- [Results expected](#results-expected-3)
- [Lessons Learned/issues encountered](#lessons-learnedissues-encountered)
##  System Research

1. _Storage Engines._ According to the official docs, "the choice of a transactional storage engine such as InnoDB or a nontransactional one such as MyISAM can be very important for performance and scalability." By default, the storage engine for new tables is InnoDB. It claims that InnoDB tables "outperform the simpler MyISAM tables, especially for a busy database." MyISAM has a small footprint and does table-level locking which reduces performances (relative to InnoDB) so "it is often used in read-only or read-mostly workloads in Web and data warehousing configurations." InnoDB tables arrange data using primary keys. Each table's primary key used to create a clustered index so that I/O is reduced when using the primary key. InnoDB tables also use "Adaptive Hash Indexing" to make lookups of frequently accessed rows faster (which we also benchmark). The documentation also states, you can create and drop indexes and perform other DDL operations with much less impact on performance and availability." InnoDB tables were "designed for CPU efficiency and maximum performance when processing large data volumes".

    Truncated Table 16.1 from MySQL docs: Storage Engines Features 
    | Feature | MyISAM | InnoDB |
    | :--- | :---: | :---: |
    | B-tree indexes | Yes | Yes |
    | Clustered indexes | No | Yes |
    | Data caches | No | Yes |
    | Foreign key support | No | Yes |
    | Hash indexes | No | No |
    | Index caches | Yes | Yes |
    | Locking granularity | Table | Row |
    | Storage limits | 256TB | 64TB |
    | Transactions | No | Yes |

2. _Index Condition Pushdown._ The most frequently used storage engine is InnoDB - when a primary-key is specified, rows are inserted ordered according to the primary-key and a clustered index is created and entire rows can be read in quickly. Index Condition Pushdown (ICP) is an optimization setting that can be toggled for use when a secondary index is created. If it is toggled off, "the storage engine traverses the (secondary) index to locate rows" and "returns them to the MySQL server which evaluates the WHERE condition for the rows." If enabled, and the WHERE condition in the query only needs the indexed column, then it can push it to the storage engine which evaluates the condition using the index entry "and only if this is satisfied is the row read from the table." This makes queries that use only the secondary index column more performant.

3. _

## Performance Experiment Design 1
### Performance issue test
Comparing read and write performance of two storage engines - InnoDB and MyISAM.
### Data sets included in the test
We'll use TENKTUP1 and execute 'read-only' and 'write-only' queries using parallel connections that simulates 4 concurrent users.
- User 1: read then write
- User 2: write then read
- User 3: read then write
- User 4: write then read 

### Queries we will run
Four concurrent read/write processes using 10% selection with no index:
```
SELECT count(*) FROM TENKTUP1
WHERE tenPercent = 0

UPDATE TENKTUP1
SET string4 = 'x' where tenPercent = 0
```
Get `query_id` from `SHOW PROFILES;`
Get query time from `SHOW PROFILE FOR QUERY <id>`

### Parameters used/how parameters will be set/varied?
Enable profiling to see execution time: `SET profiling = 1;`
Disable `AUTOCOMMIT`
The command `SHOW ENGINES` tells us that the default engine is InnoDB, so to use other engines - we must specify explicitly. We'll create two tables: `CREATE TABLE ... ENGINE=InnoDB` and `CREATE TABLE ... ENGINE=MYISAM`
To verify:
```
SELECT table_name, table_type, engine
FROM information_schema.tables
WHERE table_schema = 'database_name'
ORDER BY table_name;
```

### Results expected
InnoDB seems to have many of the features we learned about or used in Postgres. In InnoDB, clustered indexes are implemented when specifying the primary-key whereas MyISAM only has unclustered indexes. Having it means the data is stored in primary-key sorted order which would decrease I/O when rows are processed sequentially. Although, in these tests, the biggest difference would be the result of InnoDB's row-level locking vs. MyISAM's table-level locking. InnoDB should perform magnitudes better than MyISAM.


## Performance Experiment Design 2

### Performance issue test
Improvement when enabling Index Condition Pushdown in an InnoDB table with a secondary index. The `WHERE` condition will use the secondary index and check the second `WHERE` condition before returning the full row. The docs say enabling ICP should reduce execution time.

### Data sets included in the test
TENKTUP1 with its original primary-key (and clustered index) but now add a secondary index on tenPercent.

### Queries we will run
`CREATE INDEX tenPercent_index ON TENKTUP1 (tenPercent)`
To verify index: `ANALYZE TABLE`
```
SELECT * FROM TENKTUP1
WHERE tenPercent = 0
AND ten = 0
```
Get `query_id` from `SHOW PROFILES;`
Get query time from `SHOW PROFILE FOR QUERY <id>`

### Parameters used/how parameters will be set/varied?
Enable profiling to see execution time: `SET profiling = 1;`
Disable `AUTOCOMMIT`

Disabled run: SET optimizer_switch = 'index_condition_pushdown=off';
Enabled run: SET optimizer_switch = 'index_condition_pushdown=on';

### Results expected
When disabled, the query will do 10% selectivity using the secondary index (retreiving full rows) then filter 10% of those.
When enabled, the query will use the index to find each "tenPercent == 0" - for each, "use the index tuple to locate and read the full table row."
Reading only 1 column out of all 16 should mean the enabled option performs better.

## Performance Experiment Design 3
### Performance issue test
### Data sets included in the test
### Queries we will run
### Parameters used/how parameters will be set/varied?
### Results expected

## Performance Experiment Design 4
### Performance issue test
### Data sets included in the test
### Queries we will run
### Parameters used/how parameters will be set/varied?
### Results expected
## Lessons Learned/issues encountered
- The performance_schema engine and table would given a lot more information about execution time but only for systems N1 with 8 or more processors or with very high memory on GCP. We can't afford it. Instead, we have to use the deprecated 'show profiles' which has similar information.
- Profiling is set to 'off' with each new connection, so we have to turn it on every time we start a session.
- We should turn off autocommit to avoid unnecessary I/O when issuing large numbers of consecutive INSERT, UPDATE, or DELETE statements. We got some transaction semantics practice and saw how commiting should be grouped otherwise queries in loops take longer.