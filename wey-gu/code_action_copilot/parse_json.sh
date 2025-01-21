# !/bin/bash

# 写一个shell解析json文件的脚本
# {
#     "app": {
#       "name": "MyApp",
#       "version": "1.0.0",
#       "features": {
#         "feature1": {
#           "enabled": true,
#           "description": "This is feature 1"
#         },
#         "feature2": {
#           "enabled": false,
#           "description": "This is feature 2"
#         }
#       }
#     },
#     "database": {
#       "url": "jdbc:mysql://localhost:3306/mydb",
#       "user": "dbuser",
#       "password": "dbpassword"
#     },
#     "server": {
#       "host": "localhost",
#       "port": 8080
#     }
#   }

# 从server.json中获取host字段的值
cat server.json | jq '.server.host'

# 使用bat脚本获取host字段的值
#!/bin/bash
# 从server.json中获取host字段的值
host=$(bat demo.json --value-only --object server.host)