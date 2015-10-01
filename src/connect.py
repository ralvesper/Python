import cx_Oracle

con = cx_Oracle.connect('CCM/desenv@128.1.30.150/ccmdes');  # @UndefinedVariable
print(con.version)

con.close()
