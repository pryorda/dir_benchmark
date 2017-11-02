### Running the benchmark
This will use 10 processes to create a total of 10000 directories. It will log the time and completion time to benchmark.log
```
./dir_benchmark.py -m 10 -t 10000 -d /mnt/fsstore/test/
```
### Example Log
```
2017-11-01 21:39:51,719 - INFO - creating path: /mnt/fsstore/test/16/920/924/895/844/ceb
2017-11-01 21:39:51,728 - INFO - created path: /mnt/fsstore/test//e3/bca/395/300/f43/aab in 10.505ms
2017-11-01 21:39:51,728 - INFO - creating path: /mnt/fsstore/test/f7/c06/00c/375/443/9cb
2017-11-01 21:39:51,735 - INFO - created path: /mnt/fsstore/test//16/920/924/895/844/ceb in 15.788ms
2017-11-01 21:39:51,742 - INFO - created path: /mnt/fsstore/test//f7/c06/00c/375/443/9cb in 13.385ms
2017-11-01 21:39:51,742 - INFO - creating path: /mnt/fsstore/test/ec/eda/5c1/f60/949/cd9
2017-11-01 21:39:51,750 - INFO - created path: /mnt/fsstore/test//ec/eda/5c1/f60/949/cd9 in 7.637ms
2017-11-01 21:39:51,751 - INFO - creating path: /mnt/fsstore/test/f8/cc7/86a/dbd/a43/82b
2017-11-01 21:39:51,775 - INFO - created path: /mnt/fsstore/test//f8/cc7/86a/dbd/a43/82b in 24.446ms
2017-11-01 21:39:51,777 - INFO - Created 10000 paths in 82 seconds
```
