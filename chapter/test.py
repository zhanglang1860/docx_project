import psycopg2
import numpy as np


def connect_sql(checklist):
    db = psycopg2.connect(host='localhost', user='zhangyicheng', password='12345', port=5432, database='Turbine')
    cur = db.cursor()
    # sql_str = ''
    #
    # for i in range(len(turbine_list)):
    #     if i == len(turbine_list) - 1:
    #         sql_str = "(" + sql_str + '\'%s\')'
    #     else:
    #         sql_str = sql_str + '\'%s\','

    # 第五章
    # selectsql_tur = "SELECT * FROM tur_model WHERE tur_type_name in " + sql_str
    # selectsql_power = "SELECT * FROM power_model WHERE tur_type_name in " + sql_str
    # selectsql_efficiency = "SELECT * FROM efficiency_model WHERE tur_type_name in " + sql_str
    #
    # print(selectsql_tur)

    # cur.execute(selectsql_tur % turbine_list)
    # data_tur = cur.fetchall()  # 所有
    # cur.execute(selectsql_power % turbine_list)
    # data_power = cur.fetchall()  # 所有
    # cur.execute(selectsql_efficiency % turbine_list)
    # data_efficiency = cur.fetchall()  # 所有
    print(checklist)
    cur.execute(checklist)
    data_foundation = cur.fetchall()  # 所有

    db.close()
    # data_tur_np = np.array(data_tur)
    # data_power_np = np.array(data_power)
    # data_efficiency_np = np.array(data_efficiency)
    data_foundationy_np = np.array(data_foundation)
    return data_foundationy_np


# turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']


def foundation_args(**kwargs):
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


def p(*turbine_list):
    return sql_foundation % turbine_list


sql_foundation, key_vaule = foundation_args(foundation_type='扩展基础', baseboard_r=11)
print(sql_foundation, key_vaule)
sql_foundation = p(*key_vaule)

foundation_np = connect_sql(sql_foundation)
print(foundation_np)
#
# for k in kwargs.keys():
#     a.append(str(k))
