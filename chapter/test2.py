a = ['foundation_type', 'max_load']
selectsql_foundation = "SELECT * FROM foundation_model WHERE %s in 扩展基础 and %s in 110000"
print(selectsql_foundation)


# turbine_list = ['GW3.3-155', 'MY2.5-145', 'GW3.0-140', 'GW3.4-140', 'GW2.5-140']
#
# sql_str = ''
#
# for i in range(len(turbine_list)):
#     if i == len(turbine_list) - 1:
#         sql_str = "(" + sql_str + '\'%s\')'
#     else:
#         sql_str = sql_str + '\'%s\','
#
# selectsql_tur = "SELECT * FROM tur_model WHERE tur_type_name in " + sql_str
# selectsql_power = "SELECT * FROM power_model WHERE tur_type_name in " + sql_str
# selectsql_efficiency = "SELECT * FROM efficiency_model WHERE tur_type_name in " + sql_str
#

def p(*turbine_list):
    return selectsql_foundation % turbine_list


selectsql_foundation = p(*a)
print(selectsql_foundation)
