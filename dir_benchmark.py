#!/usr/bin/python3
import os
from optparse import OptionParser
from multiprocessing import Pool
import sys
import logging
import time
import uuid
import re


processes = set()
max_processes = 10

# Usage
parser = OptionParser()

parser.add_option("-m", "--max-processes", dest="max_processes",
                  help="max number of processes", metavar="mp")

parser.add_option("-d", "--directory", dest="directory",
                  help="destination directory", metavar="dir")

parser.add_option("-t", "--total_paths", dest="total_paths",
                  help="total absolute paths to create", metavar="tpc")

(options, args) = parser.parse_args()

if not options.max_processes or not options.directory \
                            or not options.total_paths:
    parser.print_help()
    sys.exit()


# config
total_paths = int(options.total_paths)
directory = options.directory
max_processes = int(options.max_processes)

# logging
LOG_FILENAME = 'benchmark.log'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger("MyLogger")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
my_handler = logging.FileHandler(LOG_FILENAME)
my_handler.setFormatter(formatter)
my_logger.setLevel(logging.DEBUG)
my_logger.addHandler(my_handler)

uuid_array = []

# Functions:
# create_path based on path
def create_path(path, file_uuid):
    path = directory + "/" + path
    os.makedirs(path)

# generate_uuids(int)
def generate_uuid(num):
    for x in range(num):
        uuid_array.append(str(uuid.uuid4()))


def do_benchmark(file_uuid):
    stripped_uuid = re.sub('-', '', file_uuid)
    path = stripped_uuid[0:2] + "/" + stripped_uuid[2:5] + "/" + stripped_uuid[5:8] + "/" + \
           stripped_uuid[8:11] + "/" + stripped_uuid[11:14] + "/" + stripped_uuid[14:17]
    my_logger.info("creating path: " + path + " ")
    start = time.perf_counter()
    create_path(path, file_uuid)
    elapsed_time = time.perf_counter() - start
    my_logger.info("created path: " + path + " in " + '%.3f' % (elapsed_time * 1000) + "ms" )

generate_uuid(total_paths)
pool = Pool(processes=max_processes)
start_time = time.process_time()
pool.map(do_benchmark, uuid_array)
total_runtime = time.process_time() - start_time
my_logger.info("Created " + str(total_paths) + " in " + '%d' % (total_runtime) + " seconds" )
