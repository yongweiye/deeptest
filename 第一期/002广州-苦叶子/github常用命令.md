怎么使用github来管理你在开源优测-积微速成计划的文档

首先你需要下载安装git客户端，并添加到命令行，可以使用git命令

---

clone github项目到本地

现在命令行进入你的目标目录，例如D盘

cd D:

clone远程项目

git clone https://github.com/small99/deeptest

在本地会创建一个deeptest的目录

如何提交在deeptest项目下的文件到github

先进入deeptest目录

cd deeptest

先add一下   
git add .

然后commit一下，添加日志说明   
git commit -m "这是你的日志，请把这串文字改为实际的日志说明"

再push一下
git push

这个命令后，会提示你输入github的账号和密码，按提示即可

---

怎么更新最近的git到本地

git pull
