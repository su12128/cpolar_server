from django.test import TestCase
import sqlite3

# Create your tests here.

# 创建与数据库的连接
conn = sqlite3.connect('./test.db')
print("ok")