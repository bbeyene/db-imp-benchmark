# Part 2

## System Research

1. _Storage Engines._ According to the official docs, "the choice of a transactional storage engine such as InnoDB or a nontransactional one such as MyISAM can be very important for performance and scalability." By default, the storage engine for new tables is InnoDB. It claims that InnoDB tables "outperform the simpler MyISAM tables, especially for a busy database." MyISAM has a small footprint and does table-level locking which reduces performances (relative to InnoDB) so "it is often used in read-only or read-mostly workloads in Web and data warehousing configurations." InnoDB tables arrange data using primary keys. Each table's primary key used to create a clustered index so that I/O is reduced when using the primary key. InnoDB tables also use "Adaptive Hash Indexing" to make lookups of frequently accessed rows faster (which we also benchmark). The documentation also states, you can create and drop indexes and perform other DDL operations with much less impact on performance and availability." InnoDB tables were "designed for CPU efficiency and maximum performance when processing large data volumes".

    Truncated Table 16.1 from MySQL docs: Storage Engines Features 
    | Feature | MyISAM | InnoDB |
    | :--- | :---: | :---: |
    | B-tree indexes | Yes | Yes |
    Clustered indexes | No | Yes |
    | Data caches | No | Yes |
    | Foreign key support | No | Yes |
    Hash indexes | No | No |
    Index caches | Yes | Yes |
    Locking granularity | Table | Row |
    Storage limits | 256TB | 64TB |
    Transactions | No | Yes |

2. _

## Performance Experiment Design 1
### Performance issue test: comparing read/write performance of two storage engines - InnoDB and MyISAM.
### Data sets included in the test 
We'll use TENKTUP1 and execute 'read-only' and 'write-only' queries using parallel connections that simulates 4 concurrent users.
- User 1: read then write
- User 2: write then read
- User 3: read then write
- User 4: write then read 

### Queries we will run
Since we don't want to be bottlenecked by disk write speeds, we will turn off 'autocommit', and instead group related commands sandwiched between a 'BEGIN TRANSACTION' and 'COMMIT'. 
Enable profiling to see execution time: `SET profiling = 1;`
Four concurrent read/write processes using 10% selection
```
SELECT count(*) FROM TENKTUP1
WHERE unique2 BETWEEN 0 AND 999

UPDATE TENKTUP1
SET string4 = 'x' where tenPercent = 0
```
Get query id from `SHOW PROFILES;`
Get query time from `SHOW PROFILE FOR QUERY <id>`

### Parameters used for this test and how the parameters will be set/varied
The command `SHOW ENGINES` tells us that the default engine is InnoDB, so to use other engines - we must specify explicitly. We'll create two tables: `CREATE TABLE ... ENGINE=InnoDB` and `CREATE TABLE ... ENGINE=MYISAM`
(Turn off AUTOCOMMIT)
To verify:
```
SELECT table_name, table_type, engine
FROM information_schema.tables
WHERE table_schema = 'database_name'
ORDER BY table_name;
```

### Results expected
InnoDB seems to have many of the features we learned about or used in Postgres. In InnoDB, clustered indexes are implemented when specifying the primary-key whereas MyISAM only has unclustered indexes. Having it means the data is stored in primary-key sorted order which would decrease I/O when rows are processed sequentially. Although, in these tests, the biggest difference could be the result of InnoDB's row-level locking vs. MyISAM's table-level locking. For these reasons, InnoDB should perform magnitudes better than MyISAM.


## Performance Experiment Design 2

### Performance issue test: the 10% rule of thumb

### Data sets included in the test 

### Queries we will run

### Parameters used/how parameters will be set/varied?

### Results expected

.  
.  
.  
## Lessons Learned/issues encountered
- The performance_schema engine and table would given a lot more information about execution time but only for systems N1 with 8 or more processors or with very high memory on GCP. We can't afford it. Instead, we have to use the deprecated 'show profiles' which has similar information.
- From an efficiency perspective, we should turn off autocommit - to avoid unnecessary I/O when issuing large numbers of consecutive INSERT, UPDATE, or DELETE statements. We got some transaction semantics practice. ("Even a SELECT statement opens a transaction, so after running some report or debugging queries in an interactive mysql session, either issue a COMMIT or close the mysql session.)
- Profiling is set to 'off' with each new session, so we have to turn it on with each new connection.