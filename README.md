# learning_log
Django项目学习笔记

## Django项目搭建

# 创建目录（learning_log）
	cmd learning_log

# 建立虚拟环境
	python -m venv ll_env

# 激活虚拟环境
	source ll_env/bin/activate（linux）
	ll_env\Scripts\activate（windows）

# 停止虚拟环境
	deactivate

# 安装Django
	pip install Django==3.1.3

# Django升级命令
	pip install -U Django

# 创建项目
	django-admin.py startproject learning_log .（linux）
	django-admin startproject learning_log .（windows）

# 创建SQLite数据库
	python manage.py migrate

# 启动项目
	python manage.py runserver

# 修改数据库（python manage.py shell命令模式下：）
	python manage.py makemigrations learning_logs

# 迁移项目
	python manage.py migrate


# 管理员账号：
	admin/P@ssw0rd
	coisini/maggieq8324.