# ====================================================
# PART 1 - connecting to Oracle with cx_Oracle
#          Let code speak for itself!
# ====================================================
import sys
import getpass
import platform
import cx_Oracle
 
# -----------------------------------------------------
# Display versions of python, cx_Oracle module
# and Oracle client being used...
# -----------------------------------------------------
print ("Python version: " + platform.python_version())
print ("cx_Oracle version: " + cx_Oracle.version)
print ("Oracle client: " + str(cx_Oracle.clientversion()).replace(', ','.'))


ip = '128.1.30.150'
port = 1521
SID = 'ccmdes'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)

connection = cx_Oracle.connect('CCM', 'desenv', dsn_tns)


print ("Oracle DB version: " + connection.version)
print ("Oracle client encoding: " + connection.encoding)
connection.close()
