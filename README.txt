# Django 学生信息管理系统

## 安装步骤

1. 解压缩项目文件

2. 创建并激活虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Unix/Mac
venv\Scripts\activate  # Windows

3. 安装必要依赖\此步也可单安装django环境：pip install django

pip install -r requirements.txt

4. 进行数据库迁移

在本页面执行终端命令

python manage.py makemigrations
python manage.py migrate

5. 创建管理员账户\也可使用默认账户：admin,admin

python manage.py createsuperuser

6. 启动开发服务器：注意要挂起不要关闭终端页面

python manage.py runserver

7. 打开浏览器并访问 http://127.0.0.1:8000


