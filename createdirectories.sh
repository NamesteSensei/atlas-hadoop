#!/usr/bin/env bash

# Create /holbies directory in HDFS
hdfs dfs -mkdir /holbies

# Create /holbies/input directory in HDFS
hdfs dfs -mkdir -p /holbies/input
