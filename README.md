Hadoop Project


📌 Overview

This project demonstrates the setup and usage of Apache Hadoop (HDFS + MapReduce) using Bash and Python. It covers file management, automation, and distributed data processing.

⚙️ Technologies Used

Apache Hadoop 3.3.2

Ubuntu (WSL)

Java 11

Bash

Python 3

Snakebite (HDFS Python client)

🗂️ Project Structure
atlas-hadoop/
├── README.md
├── createdirectories.sh
├── lao.txt
├── salaries.csv
├── hadoop_project/
│   ├── mapper.py
│   ├── reducer.py
│   ├── lao.sh
│   ├── text.sh
│   ├── 4-createdir.py
│   ├── 5-deletedir.py
│   ├── 6-download.py
🚀 HDFS (Bash)

📁 Create directories
hdfs dfs -mkdir -p /holbies/input

📤 Upload file
hdfs dfs -put lao.txt /holbies/input/

📄 Read file
hdfs dfs -cat /holbies/input/lao.txt

🐍 HDFS (Python - Snakebite)
Create directories
def createdir(l):
    # creates directories in HDFS
Delete directories
def deletedir(l):
    # deletes directories in HDFS
Download files
def download(l):
    # downloads from HDFS to /tmp

🔁 MapReduce (Local)
Mapper

Transforms CSV into key-value pairs:

id    company,salary
Reducer

Processes mapper output to:

Aggregate data OR

Extract top 10 salaries

Run locally:
cat salaries.csv | ./mapper.py | sort -k2,2 | ./reducer.py
🌐 MapReduce (Hadoop Streaming)

1. Upload data to HDFS
hdfs dfs -mkdir -p /holbies/input
hdfs dfs -put -f salaries.csv /holbies/input/
2. Run job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
-input /holbies/input/salaries.csv \
-output /holbies/output \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-file mapper.py \
-file reducer.py
3. View output
hdfs dfs -cat /holbies/output/part-00000

📊 Final Output Example
id      Salary      company
11      450000.0    Salesforce
4       372000.0    Apple
3       310000.0    Amazon
...

🧠 Key Concepts

HDFS: Distributed file system for storing large data

Mapper: Transforms raw data into key-value pairs

Reducer: Aggregates and processes grouped data

Streaming: Run MapReduce jobs using scripts (Python)

🎯 Conclusion

This project demonstrates how to:

Set up and run Hadoop locally

Manage files in HDFS

Automate tasks with Bash and Python

Process data using MapReduce

👤 Author

Christopher
