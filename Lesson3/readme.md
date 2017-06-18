To run the program locally, if you do not have Hadoop installed, you can run the program

```
cat datafile | *_mapper.py | sort | *._reducer.py
```

I have included a small data file in the folder, for the large complete data set, you need to refer [purchase data set](https://www.google.com/url?q=http://content.udacity-data.com/courses/ud617/access_log.gz&sa=D&ust=1497817472420000&usg=AFQjCNFcne5yC2iQa6SOOvG2PnavanQrQw) and [web log data set](http://content.udacity-data.com/courses/ud617/purchases.txt.gz).