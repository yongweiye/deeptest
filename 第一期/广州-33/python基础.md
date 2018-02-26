## 目录<br> ##
[String](#1)<br>
[元组tuple](#2)<br>
[列表](#3)<br>
[字典](#4)<br>
[函数](#5)<br>
[迭代器和生成器](#6)<br>
[INI文件读写](#7)<br>
[目录与文件操作](#8)<br>
[XML解析处理-Element Tree](#9)<br>
[SMTP发送邮件](#10)<br>
[PyMySQL库](#11)<br>
[遗留问题](#n)<br>

<h3 id='1'>String</h3>
1.String（字符串）中判断字符串类型的方法，isdigit和isnumric都是判断字符串是否都是数字，是则返回true，否则返回false，那么它们有什么不同之处呢？

<h3 id='2'>元组tuple</h3>
1. 元组可以通过下标索引的方式来读取元素，注意索引下标从0开始<br>
2. 元组可以通过负数下标索引的方式反向读取元素<br>
3. 元组可以通过  起始:终止  方式截取一段元素，其中终止是不包含的开括号<br>
4. 元组的元素不可修改，但可删除<br>

<h3 id='3'>列表</h3>
1. 元组与列表可互相转换<br>
2. 列表拷贝的意思是，将A列表的值拷贝到B列表中去<br>
3. 列表清空，不影响<br>
4. python具有切片机制，可运用在序列中<br>
5. 元组不能修改元素,可删除;列表可修改元素可删除<br>

<h3 id='4'>字典</h3>
1. 用get获取指定key的value，如果参数不是key，则获取不到，在获取不到的情况下，回传一个默认值<br>
2. 字典不能修改key，只能修改value，找不到key时，就使用新的value插入到字典中去<br>
3. 字典不能删除value，因为是通过key去找的<br>

<h3 id='5'>函数</h3>
1. 在python中一切皆为对象，在python中不能说是值传递或引用传递，而是分为可变对象和不可变对象。<br>
可变对象举例：list、dict、set<br>
不可变对象举例：strings、tuples、numbers<br>
2. 模块是比包更大的范围，模块是包的集合<br>
3. 模块和包体现的是一种组织思想，有好的组织才能有好的架构设计

<h3 id='6'>迭代器和生成器</h3>
1.生成器是功能更强大的迭代器，返回的是一个迭代器的函数。

<h3 id='7'>INI文件读写</h3>
1.option也就是key

<h3 id='8'>目录与文件操作</h3>
1. os模块的删除目录方法，目标删除目录必须存在且无子目录、子文件<br>
2. path模块获取文件大小单位为字节<br>
3. os模块所提供的目录遍历方法walk，返回值为一个迭代器对象，它的每个部分包含一个元组，即(目录X, [目录X下的目录列表], [目录X下的文件列表])

<h3 id='9'>XML解析处理-Element Tree</h3>
1. 1.python中解析xml的方法有很多，ElementTree是其中之一<br>
ElementTree中每个节点（即Element）具有如下属性：<br>
 - tag:string对象，标识该元素类型<br>
 - attrib:dictionary对象，标识该元素属性<br>
 - text:string对象，标识该元素的文本<br>
 - tail：string对象，标识该元素可选的尾字符串<br>
 - child elements：标识子节点<br>
注意：Element类型是一种灵活的**容器对象**，用于在内存中存储**结构化数据**。<br><br>
2. 使用ET.fromstring("xml格式字符串")即可实现对xml格式的字符串进行遍历读取、新增、修改和删除。<br>

<h3 id='10'>SMTP发送邮件</h3>
1. 使用smtplib进行文本格式、HTML格式和带附件的邮件发送<br>
 - 导入smtplib模块<br>
   <font color=grey>import smtplib</font><br>
 - 关键函数说明<br>
	1)创建smtp对象<br>
   <font color=grey>smtp = smtplib.SMTP([host [, port[, localhost]]])</font><br>
   参数说明：<br>
   host：smtp服务地址，例如126邮箱的是：smtp.126.com<br>
   port：smtp服务端口<br>
   localhost：如果你的smtp服务在本机，则只需指定localhost即可<br><br>
	2)发送邮件函数<br>
   <font color=grey>SMTP.sendmail(from\_addr, to\_addrs, msg[, mail\_options, rcpt\_options])</font><br>
   参数说明：<br>
   from_addr：邮件发送地址<br>
   to_addrs：邮件接收地址列表<br>
   msg：邮件内容<br>
   mail\_options,rcpt\_options：可选参数<br>
<br>
2. 发送内容的构建中，将plain改为html标识邮件内容为html格式，邮件内容采用html语言来格式化<br><br>
3. 附件格式邮件需要导入新的类：<font color=grey>from email.mime.multipart from MIMEMultipart</font><br>
   需要使用MIMIMultipart构建内容结构，关键代码如下：<br><br>
   # 发送内容构建 # html标识发送内容为文本格式<br>
   <font color=grey>
   msg = MIMEMultipart()<br>
   msg["From"] = "sender@163.com"<br>
   msg["To"] = receivers<br>
   </font><br>
   # 构建邮件标题<br>
   <font color=grey>
   msg["Subject"] = Header("附件格式邮件", "utf-8")<br>
   </font><br>
   # 构建邮件正文内容<br>
   <font color=grey>
   msg.attach(MIMEText("附件格式邮件", "plain", "utf-8"))<br>
   </font><br>
   # 构造附件，多个附件同理<br>
   <font color=grey>
   attach1 = MIMEText(open("smtp_attach.py", 'rb').read(), "base64", "utf-8")<br>
   attach1["Content-Type"] = "application/octet-stream"<br>
   </font><br>
   # 这里filename随意写，将会在邮件中显示<br>
   <font color=grey>
   attach1["Content-Disposition"] = "attachment;filename=code.py"<br>
   </font><br>
   # 关联附件到邮件中<br>
   <font color=grey>
   msg.attach(attach1)<br>
   </font><br>
4. 构建文本和html格式的邮件使用MIMEText构建，使用plain标识文本内容格式，使用html标识html内容格式<br>
5. 对于附件格式则需要使用MIMEMultipart

<h3 id='10'>SMTP发送邮件</h3>
1. 安装pymysql:	pip install PyMySQL
2. 在pymysql中提供了Connection和Cursor对象来管理操作MySQL
 - Connection<br>
   代表一个与MySQL Server的socket连接，使用connect方法来创建一个连接实例<br><br>
   connect()-------创建一个数据库连接实例<br>
   begin()----------开始一个事务<br>
   close()----------发送一个退出消息，并关闭连接<br>
   commit()--------提交修改至数据库<br>
   cursor()---------创建一个cursor（游标）实例<br>
   ping()------------检测服务器是否在允许<br>
   rollback()--------回滚当前事务<br>
   select_db(db)---设置当前db<br>
   show_warning---显示警告信息<br><br>
 - Cursor<br>
   代表一个与MySQL数据库交互对象，使用Connection.Cursor()在当前socket连接上交互对象<br>
   close()-------------关闭当前cursor<br>
   execute()----------执行一个sql语句<br>
   executemany()---执行批量sql语句<br>
   fetchall()-----------取所有数据<br>
   fetchone()---------取一条数据

<h3 id='n'>遗留问题</h3>
1. 利用生成器函数去读大文件，例如10G的文件，你可以利用生成器函数，每次只读100M进行处理，处理完后再读取下一个100M，如此迭代下去<br>
2. 提问：os_walk.py为什么最后两个for是平级的？不平级的效果为什么遍历不到部分文件最深层？<br>
3. 提问：字符串存储中文时如何转换<br>
4. 用类封装一个通用的ini文件操作类<br>
5. 提问：格式化日期时间函数strftime为什么后面要加上time.loacltime()<br>
6. 使用ET.fromstring（"xml格式字符串"）实现对xml格式的字符串进行遍历读取、新增、修改和删除动作<br>