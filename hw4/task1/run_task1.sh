#!/usr/bin/

MAPPER_FILE_PATH=./mapper_task1.py
REDUCER_FILE_PATH=./reducer_task1.py
HDFS_INPUT_FILE=/user/warandpeace.txt
HDFS_OUTPUT_PATH=/user/output

#make sure the output directory in hdfs is not existed:
hadoop fs -rm -r $HDFS_OUTPUT_PATH
#run the job
echo 'mapper file path: '$MAPPER_FILE_PATH
echo 'reducer file path: '$REDUCER_FILE_PATH
echo 'input file: '$HDFS_INPUT_FILE
echo 'output file: '$HDFS_OUTPUT_PATH

echo 'running map-reduce job ...'
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.5.jar -files $MAPPER_FILE_PATH,$REDUCER_FILE_PATH -mapper $MAPPER_FILE_PATH -reducer $REDUCER_FILE_PATH -input $HDFS_INPUT_FILE -output $HDFS_OUTPUT_PATH

#show word -- count
echo 'results...'
hadoop fs -text $HDFS_OUTPUT_PATH/part* > ~/sample_codes/task1/task1_output.txt
