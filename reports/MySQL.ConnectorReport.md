# MySQL.Conenctor Report

# Overview
MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the Python Database API Specification v2.0 (PEP 249). It also contains an implementation of the X DevAPI, an Application Programming Interface for working with the MySQL Document Store.
https://github.com/mysql/mysql-connector-python

# License
MySQL.Connector uses GNU General Public License, version 2 (https://github.com/mysql/mysql-connector-python/blob/master/LICENSE.txt). 

If we modify any files we must we must make prominent notices signifying the changes

You are allowed to sell copies of the modified program commercially, but only under the terms of the GNU GPL. Thus, for instance, you must make the source code available to the users of the program as described in the GPL, and they must be allowed to redistribute and modify it as described in the GPL.

These requirements are the condition for including the GPL-covered code you received in a program of your own.

You cannot incorporate GPL-covered software in a proprietary system. 

# Our Use
We utilize the mysql_connector file (https://github.com/mysql/mysql-connector-python/blob/master/src/mysql_connector.c). We create an mysql.connector instance and call .connect to connect our website to the server. Our query is then constructed where a cursor executes the query and then the query is commited to the database. A return value is retrieved using cursor.lastrowid() or cursor.fetchall(). The mysql.connector instance is then closed