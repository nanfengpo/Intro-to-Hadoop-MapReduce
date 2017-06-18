
you can use the format to test in local machine if Hadoop is not avaiable

```
cat datafilename | python *_mapper.py | sort | python *_reducer.py
```

For the complete data set, please refer [here](http://content.udacity-data.com/course/hadoop/forum_data.tar.gz)