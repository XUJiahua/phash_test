## 试验 phash 效果

https://github.com/JohannesBuchner/imagehash

微信头像链接很神奇，每次下载的头像看上去一样，其实是完全不同的文件。使用密码学上的hash算法，每次下载，文件的些许变化，导致hash都不一样。

初步试验过phash效果不错。加大剂量，本文试验在大数据下效果如何。

### 下载微信用户头像

随机抽了10万个微信头像链接，下载10次。大概花20分钟。

```
./download.sh
```

其中，头像并行下载工具`avatar_dl`(https://github.com/XUJiahua/avatar_dl)如果不是在Mac上就要自己重新编译。
`sample100k.csv`是头像链接，一行一个，考虑隐私，不作公开。

### 生成 phash

extract_feature_p.py 并行处理。大概花10分钟。

```
python extract_feature_p.py

echo "file,feature" > header.csv
cat header.csv download_1.csv download_2.csv download_3.csv download_4.csv download_5.csv download_6.csv download_7.csv download_8.csv download_9.csv download_10.csv > data.csv
```

数据量小，可以使用单进程的。

```
python extract_feature.py > data.csv

```

形成csv表格，第一列是文件名，第二列是hash值。

### 效果验证

本地使用`csvsql`这个工具分析结果。

定义两个指标。理论上，一个URL多次下载的图，其hash值应该是相同的。

```bash
csvsql --query "select avg(cnt) as expect1 from (select file, count(distinct feature) as cnt from 'data' group by file)" data.csv

expect1
1.1413604158721875
```

不同的URL对应的图（可能有相同图，不同URL），其hash值不同。

```bash
csvsql --query "select avg(cnt) as expect1 from (select feature, count(distinct file) as cnt from 'data' group by feature)" data.csv

expect1
1.0312553837783924
```

两个指标越接近1，说明效果越好。
