# Hadoop Project - Atlas School

##  Description
This project demonstrates the setup and usage of Hadoop (HDFS) using Ubuntu and WSL.  
We configured a single-node Hadoop cluster and performed basic HDFS operations.

---

## ⚙️ Setup

- Ubuntu (WSL)
- Hadoop 3.3.2
- Java 11
- SSH configured

---

## Project Structure

---

##  Tasks

### 0. HDFS with Bash

Script: `createdirectories.sh`

Creates directories in HDFS:
- `/holbies`
- `/holbies/input`

---

## Commands Used

```bash
start-dfs.sh
hdfs dfs -mkdir -p /holbies/input
hdfs dfs -ls -R /

Data Processing

Uploaded text file (lao.txt)

Uploaded CSV file (salaries.csv)

Performed basic analysis:

hdfs dfs -cat /holbies/input/lao.txt | wc -l
hdfs dfs -cat /holbies/input/lao.txt | tr

Key Concepts

HDFS file system

Hadoop cluster setup

SSH configuration

Data ingestion

Basic MapReduce logic (word count)
