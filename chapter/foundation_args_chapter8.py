def foundation_args_chapter8(**kwargs):
    """
    :param: dict 载入需要查询的字典key，以及对应的value。例如：
    args_chapter8 = {'foundation_type': '扩展基础', 'max_load': 110000}
    :returns: str, str foundation_sql, key_value
    SELECT * FROM foundation_model WHERE %s = '%s' and %s = '%s'
    key_value ['foundation_type', '扩展基础', 'maxload', 110000]

    """

    sql_str = ''
    key_value = []
    for k, v in kwargs.items():
        if sql_str == '':
            sql_str = sql_str + '%s' + ' = ' + '\'%s\''
        else:
            sql_str = sql_str + ' and ' + '%s' + ' = ' + '\'%s\''
        key_value.append(k)
        key_value.append(v)
    foundation_sql = "SELECT * FROM foundation_model WHERE " + sql_str
    return foundation_sql, key_value


def present(sql_foundation, *key_value):
    """
    :param key_value:
    :return: str sql 一条sql查询语句
    SELECT * FROM foundation_model WHERE
     foundation_type = '扩展基础'and maxload = '110000'

    """
    return sql_foundation % key_value

# ****************
#   测试调用
# args_chapter8 = {'foundation_type': '扩展基础', 'maxload': 110000}
# sql_foundation, key_value = foundation_args_chapter8(**args_chapter8)
# print(sql_foundation,key_value)
# sql_foundation=present(sql_foundation,*key_value)
# print(sql_foundation)
# ****************
