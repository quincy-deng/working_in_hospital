# code-server 安装和使用
## 安装
### conda安装code-server到阿里云
Google搜索conda code-server
conda install -c conda-forge code-server
### 网络端口配置
- 打开端口
```bash
$ firewall-cmd --permanent --list-port
$ firewall-cmd --add-port=8080/tcp --permanent  
  # 提示success
$ firewall-cmd --reload
```
- 安全组添加8080端口
### 后台运行
- 编写运行脚本,code-server.sh
添加一行 code-server --host "0.0.0.0"
- 编写.bashrc
添加一行 export PASSWORD="{password}" 
- 后台运行
`nohup sh code-server.sh &`
> 安装完成
- 访问 ip:8080
---
## 同步到github

### 阿里云身份配置
```
$ git config --global user.name "dengqiuyang"
$ git config --global user.email "huanghujiandqy@gmail.com"
创建私钥
$ ssh-keygen
$ 添加id_rsa.pub到github
测试
$ ssh -T git@github.com
```
### 下载并同步
- 克隆远程库到阿里云,注意使用http开头,git开头有问题.
### 完成
