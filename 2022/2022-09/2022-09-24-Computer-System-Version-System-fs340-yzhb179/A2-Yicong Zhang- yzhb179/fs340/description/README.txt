【工作目录在versionfs.py同目录】
1/ 新建文件将新建版本
		$ echo "1" > mount/test1
2/ 移入文件将新建版本
		$ echo "test" > move
		$ mv move ./mount/
3/ 版本管理
	1. 修改并保存文件将新增版本
		$ echo "2" > mount/test1
		$ echo "3" > mount/test1
		$ echo "4" > mount/test1
	2. 未修改保存文件将不新增版本
		$ echo "4" > mount/test1
	3. 超过6个版本时，最旧的版本将被删除
		$ echo "5" > mount/test1
		$ echo "6" > mount/test1
		$ echo "7" > mount/test1
		$ echo "8" > mount/test1
	4. 隐藏文件不纳入版本管理
		$ echo "hidden" > mount/.hidden
		$ ls -lh .versionsdir
	5. 移除文件后，文件历史由学生决定如何处理（这里全部删除）
		$ rm -f mount/move
4/ mount目录查看文件只能看到最新文件，不能看到文件历史
		$ ls -lh mount
5/ catversion
	1. 合法版本将打印对应版本内容
		$ ./catversion test1 1
		$ ./catversion test1 6
		$ ./catversion test1 2
	2. 不合法版本数将打印错误
		$ ./catversion test1 0
		$ ./catversion test1 18
6/ mkcurrent
	1. 不合法版本数提示错误或不操作
		$ ./mkcurrent test1 0
		$ ./mkcurrent test1 18
	2. 最新版本将设为给定版本
		$ ./mkcurrent test1 1
		$ ./mkcurrent test1 2
	3. 若选定版本与给定版本内容一致，则【作业未提及】（这里不过滤，但选定版本就是最新的就不操作）
		$ ./mkcurrent test1 6
	4. 若版本少于6个，则追加版本，否则删除最旧的版本
		$ ./rmversions test1
		$ echo "2" > mount/test1
		$ ./mkcurrent test1 1
7/ listversions
	1. 显示所有版本
		$ ./listversions test1
8/ rmversions
	1. 删除所有版本，只留最新的
		$ ./rmversions test1
	2. 若只有1个版本，不操作
		$ ./rmversions test1
9/ shutdownversions
	1. 删除.versiondir
	2. umount mount
		$ ./shutdownversions
		$ ls -al


