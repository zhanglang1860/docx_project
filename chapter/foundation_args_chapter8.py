def foundation_args_chapter8(**kwargs):
    sql_str = ''
    key_vaule = []
    for k, v in kwargs.items():
        if sql_str == '':
            sql_str = sql_str + '%s' + ' = ' + '\'%s\''
        else:
            sql_str = sql_str + ' and ' + '%s' + ' = ' + '\'%s\''
        key_vaule.append(k)
        key_vaule.append(v)
    foundation_sql = "SELECT * FROM foundation_model WHERE " + sql_str
    return foundation_sql, key_vaule
