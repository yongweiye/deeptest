### git的使用

- 1、window上安装git（过程略）

- 2、git全局初始化用户名和邮箱

$ git config --global user.name "Your Name"

$ git config --global user.email "email@example.com"

- 3、查看本机git配置
#### 命令 
$ git config --list

### 修改git的邮箱和用户名
$ git config --global --replace-all user.email "输入你的邮箱"

$ git config --global --replace-all user.name "输入你的用户名"

### Github上fork后，保持和源项目同步
- 先把源项目fork到自己的github上，
- 然后下载到自己的电脑本地， 

$ git clone https://github.com/username/project.git

- 进入自己本地的项目，输入git remote -v  查看对应的路径
- 如果没有upstream路径，则$ git remote add upstream 项目地址
- 更新源项目到本地，$ git fetch upstream 然后$ git checkout master
- 合并master和upstream两个分支，$ git merge upstream/master

- 完成了和源项目的同步