---
title: "Snowflake Lahman Baseball Database Hall of Fame Inductees"
excerpt: "ETL process to create a data set of MLB player's career statistics"
collection: portfolio
---

# Using Snowflake to extract, load and transform using Lahman Database from a S3 Bucket

## For this project, I wanted to create a table to predict Hall Of Fame inductees using the Lahman Database. The database includes all participating players in Major League Baseball from 1871 to 2023. Statistics such as on base percentage, birth country, height, weight, and career totals in hits, homeruns as well as hall of fame inducted status are incorporated in the final data set. I was able to extract the data from a S3 bucket, load it into Snowflake and transform the columns using snowflake functions. 

## After the ETL process, I was able to export my data using Snowflake integration to the S3 bucket used.

### First, I set up my snowflake environment by creating a database, warehouse for loading and querying data, and adding database tables

``` sql
-----------------------------
-----------------------------
-- CREATE THE DATABASE
-----------------------------
-----------------------------

-- Select the role to use.
USE ROLE sysadmin;

-- Create the database.
CREATE OR REPLACE DATABASE lahman_db;

-----------------------------
-----------------------------
-- CREATE WAREHOUSES
-----------------------------
-----------------------------

-- Create a new warehouse for loading data.
CREATE OR REPLACE WAREHOUSE lahman_loading_wh WITH
    WAREHOUSE_SIZE='SMALL'
    AUTO_RESUME = TRUE
    AUTO_SUSPEND = 300;

-- Create a new warehouse for loading data.
CREATE OR REPLACE WAREHOUSE lahman_query_wh WITH
    WAREHOUSE_SIZE='SMALL'
    -- MIN_CLUSTER_COUNT = 3
    -- MAX_CLUSTER_COUNT = 3
    AUTO_RESUME = TRUE
    AUTO_SUSPEND = 300;

USE WAREHOUSE lahman_loading_wh;
```

### Next, I created the tables to upload the data from an AWS S3 bucket

``` sql
-----------------------------
-----------------------------
-- CREATE TABLES
-----------------------------
-----------------------------

-- Reset the context.
USE ROLE sysadmin;
USE DATABASE lahman_db;
USE WAREHOUSE lahman_loading_wh;

-- Create the database tables.
CREATE OR REPLACE TABLE batting (
    playerID string,
    yearID integer,
    stint integer,
    teamID string,
    lgID string,
    G integer,
    G_batting integer,
    AB integer,	
    R integer,
    H integer,
    doubles	integer,
    triples integer,	
    HR integer,
    RBI	integer,
    SB integer,
    CS integer,	
    BB integer,	
    SO integer,	
    IBB integer,	
    HBP integer,	
    SH integer,	
    SF integer,
    GIDP integer,
    G_old integer
);

CREATE OR REPLACE TABLE appearances (
    yearID integer,
    teamID string,	
    lgID string,
    playerID string,
    G_all integer,
    GS integer,
    G_batting integer,	
    G_defense integer,	
    G_p integer,	
    G_c integer,	
    G_1b integer,	
    G_2b integer,	
    G_3b integer,	
    G_ss integer,	
    G_lf integer,	
    G_cf integer,	
    G_rf integer,	
    G_of integer,	
    G_dh integer,	
    G_ph integer,	
    G_pr integer
);

CREATE OR REPLACE TABLE people (
    ID integer,
    playerID string,
    birthYear integer,
    birthMonth integer,
    birthDay string,
    birthCity string,
    birthCountry string,
    birthState string,
    deathYear integer,
    deathMonth integer,
    deathDay integer,
    deathCountry string,
    deathState string,
    deathCity string,
    nameFirst string,
    nameLast string,
    nameGiven string,
    weight integer,
    height integer,
    bats string,
    throws string,
    debut date,
    bbrefID	string,
    finalGame date,
    retroID string
);

CREATE OR REPLACE TABLE halloffame (
    playerID string,
    yearid integer,
    votedBy	string,
    ballots	integer,
    needed integer,
    votes integer,
    inducted string,
    category string,
    needed_note string
);
```

### After creating the tables, I prepared the staging environment to load the data into the tables

``` sql
-----------------------------
-----------------------------
-- PREPARE FOR DATA LOADING
-----------------------------
-----------------------------

-- Create the staging environment.
CREATE OR REPLACE STAGE lahman_stage
    url = 's3://lahman*****/lahman_1871-2023_csv/';

LIST @lahman_stage;

-- Create new file formats for csv files
CREATE OR REPLACE FILE FORMAT lahman_csv
    type='csv'
    skip_header = 1
    null_if = ('')
    field_optionally_enclosed_by = '\042'
;

-- Create file format for people table because of accents in string
CREATE OR REPLACE FILE FORMAT lahman_people_csv
    type='csv'
    skip_header = 1
    null_if = ()
    field_optionally_enclosed_by = '\042'
    ENCODING = 'ISO-8859-1'
;
```

### Loading the data into the tables from the S3 bucket

``` sql
-----------------------------
-----------------------------
-- LOAD THE DATA
-----------------------------
-----------------------------

-- Copy into batting table (comma-delimited).
COPY INTO batting
    FROM @lahman_stage/Batting.csv
    file_format = lahman_csv
    -- VALIDATION_MODE = RETURN_ERRORS -- checks all rows
    -- VALIDATION_MODE = RETURN_10_ROWS -- checks first 10 rows  
    ON_ERROR = ABORT_STATEMENT -- will not load it any errors (default)
    -- ON_ERROR = SKIP_FILE_5 -- will not load if 5 or more errors
;

-- Copy into appearances table (comma-delimited).
COPY INTO appearances
    FROM @lahman_stage/Appearances.csv
    file_format = lahman_csv
    -- VALIDATION_MODE = RETURN_ERRORS -- checks all rows
    -- VALIDATION_MODE = RETURN_10_ROWS -- checks first 10 rows  
    ON_ERROR = ABORT_STATEMENT -- will not load it any errors (default)
    -- ON_ERROR = SKIP_FILE_5 -- will not load if 5 or more errors
;

-- Copy into people table (comma-delimited).
COPY INTO people
    FROM @lahman_stage/People.csv
    file_format = lahman_people_csv
    -- VALIDATION_MODE = RETURN_ERRORS -- checks all rows
    -- VALIDATION_MODE = RETURN_10_ROWS -- checks first 10 rows  
    ON_ERROR = ABORT_STATEMENT -- will not load it any errors (default)
    -- ON_ERROR = SKIP_FILE_5 -- will not load if 5 or more errors
;

-- Copy into people table (comma-delimited).
COPY INTO halloffame
    FROM @lahman_stage/HallOfFame.csv
    file_format = lahman_csv
    -- VALIDATION_MODE = RETURN_ERRORS -- checks all rows
    -- VALIDATION_MODE = RETURN_10_ROWS -- checks first 10 rows  
    ON_ERROR = ABORT_STATEMENT -- will not load it any errors (default)
    -- ON_ERROR = SKIP_FILE_5 -- will not load if 5 or more errors
;
```

### Transforming the data after loading. I used zero-copy cloned tables for efficiency, saving time and storage space

``` sql
-----------------------------
-----------------------------
-- TRANSFORM DATA (AFTER LOADING)
-----------------------------
-----------------------------

USE WAREHOUSE lahman_query_wh;

-- BATTING table
-- Create a development table to avoid impacting production
CREATE OR REPLACE TABLE batting_dev 
CLONE batting;

-- Explore development (“dev”) table looking at all of Hank Aaron's seasons
SELECT *
FROM batting_dev
WHERE playerID = 'aaronha01'
;

-- Explore development (“dev”) table looking at Hank Aaron's total At-bats, Runs, Hits, On base percentage,
-- Stolen bases, caught stealing and steal percentage
SELECT playerID,
        SUM(ZEROIFNULL(AB)) as total_AB,
        SUM(ZEROIFNULL(H)) as total_H,
        SUM(ZEROIFNULL(BB)) as total_BB,
        SUM(ZEROIFNULL(HBP)) as total_HBP,
        SUM(ZEROIFNULL(SF)) as total_SF,
        DIV0((total_H + total_BB + total_HBP), (total_AB + total_BB + total_SF + total_HBP)) as on_base_percent,
        SUM(ZEROIFNULL(SB)) as total_SB,
        SUM(ZEROIFNULL(CS)) as total_CS,
        DIV0(total_SB, (total_SB + total_CS)) as steal_percent
FROM batting_dev
WHERE playerID = 'aaronha01'
GROUP BY playerID
;

-- CREATE VIEW for career statistics for each player by playerID
CREATE OR REPLACE VIEW batting_view AS
SELECT playerID,
        MAX(yearID) as last_year_played,
        SUM(ZEROIFNULL(G)) as total_games,
        SUM(ZEROIFNULL(AB)) as total_AB,
        SUM(ZEROIFNULL(R)) as total_R,
        SUM(ZEROIFNULL(H)) as total_H,
        SUM(ZEROIFNULL(doubles)) as total_doubles,
        SUM(ZEROIFNULL(triples)) as total_triples,
        SUM(ZEROIFNULL(HR)) as total_HR,
        SUM(ZEROIFNULL(RBI)) as total_RBI,
        SUM(ZEROIFNULL(SB)) as total_SB,
        SUM(ZEROIFNULL(CS)) as total_CS,
        SUM(ZEROIFNULL(BB)) as total_BB,
        SUM(ZEROIFNULL(SO)) as total_SO,
        SUM(ZEROIFNULL(IBB)) as total_IBB,
        SUM(ZEROIFNULL(HBP)) as total_HBP,
        SUM(ZEROIFNULL(SH)) as total_SH,
        SUM(ZEROIFNULL(SF)) as total_SF,
        SUM(ZEROIFNULL(GIDP)) as total_GIDP,
        DIV0((total_H + total_BB + total_HBP), (total_AB + total_BB + total_SF + total_HBP)) as on_base_percent,
        DIV0(total_SB, (total_SB + total_CS)) as steal_percent
FROM batting_dev
GROUP BY playerID
;

-- Confirm the calculations is correct.
SELECT * 
FROM batting_view
WHERE playerID = 'aaronha01'
;
```

``` sql
-- Appearances table is needed to get players primary position played
-- Create a development table for appearances to avoid impacting production
CREATE OR REPLACE TABLE appearances_dev 
CLONE appearances;

-- Using CASE statement from Appearances table to get player position
-- Window function to group the games played by playerID
CREATE OR REPLACE VIEW position_view AS
SELECT playerID,
    CASE GREATEST(G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_of, G_dh, G_ph, G_pr)
        WHEN G_p THEN 'p'
        WHEN G_c THEN 'c'
        WHEN G_1b THEN '1b'
        WHEN G_2b THEN '2b'
        WHEN G_3b THEN '3b'
        WHEN G_ss THEN 'ss'
        WHEN G_of THEN 'of'
        WHEN G_p THEN 'dh'
        WHEN G_p THEN 'ph'
        WHEN G_p THEN 'pr'
    END player_position
FROM (
SELECT playerID, SUM(G_p) as G_p, SUM(G_c) as G_c, SUM(G_1b) as G_1b, SUM(G_2b) G_2b, SUM(G_3b) as G_3b, SUM(G_ss) as G_ss, 
SUM(G_of) as G_of, SUM(G_dh) as G_dh, SUM(G_ph) as G_ph, SUM(G_pr) as G_pr
FROM appearances_dev
GROUP BY playerID
)
;

-- Confirming CASE statement is correct
SELECT *
FROM position_view
WHERE playerID = 'aaronha01'
;
```

``` sql
-- People Table to get name, weight, height, birth country, 
-- Create a development table to avoid impacting production
CREATE OR REPLACE TABLE people_dev 
CLONE people;

-- CREATE VIEW for group by playerID
CREATE OR REPLACE VIEW people_view AS
SELECT playerID, 
        CONCAT_WS(' ',nameFirst, nameLast) as name,
        birthCountry,
        weight, 
        height, 
        bats, 
        throws
FROM people_dev
;

-- Confirm the people view is correct.
SELECT *
FROM people_view;
```

``` sql
-- Hall of Fame table to get inducted status
-- Create a Hall of fame development table to avoid impacting production
CREATE OR REPLACE TABLE hof_dev 
CLONE halloffame;

-- Creating view for all hall of fame inducted status for each playerID
CREATE OR REPLACE VIEW hof_view AS
SELECT playerid, 
        MAX(inducted) as inducted
FROM hof_dev
GROUP BY playerid
;

-- Confirm Hall of fame table is correct
SELECT *
FROM hof_view
ORDER BY playerid
;
```

### Finally, I joined the tables together for the final view

``` sql
-- Create a View to JOIN the tables together 
CREATE OR REPLACE VIEW final_view AS
SELECT *
FROM batting_view
LEFT JOIN people_view
USING (playerid)
LEFT JOIN position_view
USING (playerid)
LEFT JOIN hof_view
USING (playerid)
ORDER BY playerid;

-- confirm final view is correct
SELECT *
FROM final_view;

```

### Unloading the data to my S3 bucket using Snowflake integration

``` sql
----------------------------------
-- UNLOADING DATA
----------------------------------

-- SETTING UP S3 intergration

USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$GET_SNOWFLAKE_PLATFORM_INFO();

-- Create INTERGRATION TO S3 bucket
CREATE STORAGE INTEGRATION s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::**************:role/mysnowflakerole'
  STORAGE_ALLOWED_LOCATIONS = ('s3://lahman****/lahman_1871-2023_csv/', 's3://lahman****/lahman_1871-2023_csv/');

-- describe integration 
DESC INTEGRATION s3_int;

-- Create a stage for exporting data
USE ROLE sysadmin;
CREATE OR REPLACE STAGE lahman_export_stage
    URL = 's3://lahman****/lahman_1871-2023_csv/'
    STORAGE_INTEGRATION = s3_int;

-- copy final view into staging
COPY INTO @lahman_export_stage
FROM final_view;

-- Examine the files in the NAMED STAGE.
LIST @lahman_export_stage;

-- Verify there is data in the file.
SELECT $1, $2, $3, $4 FROM @lahman_export_stage/data_0_0_0.csv.gz LIMIT 10;

```

### Removing clones and staging after use.

``` sql
-- Remove the file from staging, and drop the stage.
REMOVE @lahman_export_stage/data_0_0_0.csv.gz;
LIST @lahman_export_stage;
DROP STAGE lahman_export_stage;

-- Drop the development tables (no longer needed).
DROP TABLE batting_dev;
DROP TABLE appearances_dev;
DROP TABLE people_dev;
DROP TABLE hof_dev;
```

### Sample of the final data set

|PLAYERID|LAST_YEAR_PLAYED|TOTAL_GAMES|TOTAL_AB|TOTAL_R|TOTAL_H|TOTAL_DOUBLES|TOTAL_TRIPLES|TOTAL_HR|TOTAL_RBI|TOTAL_SB|TOTAL_CS|TOTAL_BB|TOTAL_SO|TOTAL_IBB|TOTAL_HBP|TOTAL_SH|TOTAL_SF|TOTAL_GIDP|ON_BASE_PERCENT|STEAL_PERCENT|NAME|BIRTHCOUNTRY|WEIGHT|HEIGHT|BATS|THROWS|PLAYER_POSITION|INDUCTED|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|aardsda01|2015|331|4|0|0|0|0|0|0|0|0|0|2|0|0|1|0|0|0|0|David Aardsma|USA|215|75|R|R|p|N|
|aaronha01|1976|3298|12364|2174|3771|624|98|755|2297|240|73|1402|1383|293|32|21|121|328|0.373949|0.766773|Hank Aaron|USA|180|72|R|R|of|Y|
|aaronto01|1971|437|944|102|216|42|6|13|94|9|8|86|145|3|0|9|6|36|0.291506|0.529412|Tommie Aaron|USA|190|75|R|R|1b|N|


```python

```
