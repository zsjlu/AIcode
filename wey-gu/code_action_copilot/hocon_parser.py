import pyhocon

# 使用python解析HOCON文件
def parse_hocon_file(file_path):
    """
    解析指定路径的HOCON文件并返回解析后的配置对象。

    参数:
    file_path (str): HOCON文件的路径。

    返回:
    pyhocon.config_tree.ConfigTree: 解析后的配置对象。
    """
    # 打开指定的文件路径，使用UTF-8编码读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 使用pyhocon库的ConfigFactory解析读取的内容为配置对象
    config = pyhocon.ConfigFactory.parse_string(content)
    
    # 更新 database字段的值 
    config['database']['host'] = 'test'
    config['database']['port'] = 3306
    # 返回解析后的配置对象
    return config
    

# Example usage
if __name__ == "__main__":
    file_path = 'demo.conf' 
    config = parse_hocon_file(file_path)
    print(config)