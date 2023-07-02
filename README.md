# easySearch

## 1. 介绍

- 针对批量搜索语法进行搜索
  - [x] google搜索：返回搜索结果的 `标题|URL|域名`
  - [ ] fofa搜索
  - [ ] zoomeye搜索

## 2. 安装依赖

- pip install -r requirements.txt

## 3. 生成key和cx

> [参考](https://zhuanlan.zhihu.com/p/174666017)

- [生成key地址](https://link.zhihu.com/?target=https%3A//developers.google.com/custom-search/v1/overview%23api_key)

- [生成cx地址](https://link.zhihu.com/?target=https%3A//programmablesearchengine.google.com/cse/create/new)

- 填入`Key`和`cx`，并设置代理

  ![image-20230703033755527](https://pic-go1.oss-cn-guangzhou.aliyuncs.com/image-20230703033755527.png)

## 4. 运行实例

- 将搜索语法放到`in.txt`文件中，例如

  ```
  site:edu.cn 北京
  site:org.cn 北京
  site:gov.cn 北京
  ```

- 批量搜索，并将搜索结果输出到`out.txt`

  - python google_search.py in.txt out.txt

![image-20230703034717252](https://pic-go1.oss-cn-guangzhou.aliyuncs.com/image-20230703034717252.png)

## 5. 参考

- [如何使用谷歌搜索API来获取结果 [知乎]](https://zhuanlan.zhihu.com/p/174666017)
