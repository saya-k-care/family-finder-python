import json
from pickle import NONE

import web

from agent.server.address import Address
from agent.server.agent import Agent
from agent.server.donate import Donate
from agent.server.email_client import AgentEmail
from agent.server.user import User
from finder.server.finder_care_taker import FinderCareTaker
from finder.server.finder_kid import FinderKid
import pymysql as MySQLdb


class FinderDB:
    @staticmethod
    def login(id, password):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "select * from care_taker where care_taker_email = '" + str(id) + "' and care_taker_password = '" + str(password) + "'";
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data[0], indent=4, sort_keys=True, default=str)
    
            kid = json.loads(kid_json)

            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            return json.dumps(kid)

    @staticmethod
    def get_caretaker_by_id(id):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        
        sql = "SELECT c.care_taker_id, m.care_taker_msg, c.care_taker_email, m.datetime from care_taker AS c " + " LEFT JOIN care_taker_msg AS m ON c.care_taker_id = m.care_taker_id "  + " WHERE c.care_taker_id ='" +  str(id)  + "' ORDER BY m.DATETIME DESC LIMIT 1 "
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data[0], indent=4, sort_keys=True, default=str)
    
            kid = json.loads(kid_json)

            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            return json.dumps(kid)

    @staticmethod
    def get_gospel():
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "SELECT * FROM gospel WHERE order_ads = ROUND( RAND() * 3)  LIMIT 1";
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data[0], indent=4, sort_keys=True, default=str)
    
            kid = json.loads(kid_json)

            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            return json.dumps(kid)
        
    @staticmethod
    def get_caretaker_by_email(email):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "SELECT * from care_taker where care_taker_email = '" + str(email) + "'";
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        if str(myresult) == '()':
            print("result is None")
            return '{}'
        
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data[0], indent=4, sort_keys=True, default=str)
    
            kid = json.loads(kid_json)

            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            return json.dumps(kid)
        
    @staticmethod
    def get_location(id):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "SELECT kid_name,  max(kid_datetime) AS kid_datetime, care_taker_id,  kid_location, kid_response FROM kid  where care_taker_id =" + str(id) + "  group by kid_name ORDER BY kid_name"  ;
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()
        
        if str(myresult) == '()':
            print("result is None")
            return '{}'
        
        json_data=[]
        kid_list = [];
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data, indent=4, sort_keys=True, default=str)
            kid = json.loads(kid_json)
            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            kid_list.append(kid)
            json_data=[];
        print ('json_str list-->' , json.dumps(kid_list, indent=4, sort_keys=True, default=str))
        return json.dumps(kid_list)

    @staticmethod
    def update_caretaker_by_id(finderCareTaker: FinderCareTaker):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('finderCareTaker.email---->' + finderCareTaker.care_taker_email)
                print ('finderCareTaker.email str---->' + str(finderCareTaker.care_taker_email))
                mySql_insert_query = """ UPDATE care_taker SET care_taker_msg = %s WHERE care_taker_id = %s; """
                finderCareTaker: FinderCareTaker
                record = (str(finderCareTaker.care_taker_msg), str(finderCareTaker.care_taker_id))
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                care_taker_id = cursor.lastrowid
                print('care_taker_id-->' , care_taker_id)

                return care_taker_id

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to update record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
                
    @staticmethod
    def register(finderCareTaker: FinderCareTaker):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('finderCareTaker.email---->' + finderCareTaker.care_taker_email)
                print ('finderCareTaker.email str---->' + str(finderCareTaker.care_taker_email))
                mySql_insert_query = """INSERT INTO care_taker (`care_taker_email`, `care_taker_password`,`care_taker_hp`,`kid_name`) 
                                                   VALUES (%s, %s, %s, %s) """
                finderCareTaker: FinderCareTaker
                record = (str(finderCareTaker.care_taker_email), str(finderCareTaker.care_taker_password), str(finderCareTaker.care_taker_hp) , str(finderCareTaker.kid_name))
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                care_taker_id = cursor.lastrowid
                print('care_taker_id-->' , care_taker_id)

                return care_taker_id

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    @staticmethod
    def update(kid: FinderKid):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('kid.care_taker_id---->' + str(kid.care_taker_id))
                print ('kid.care_taker_id str---->' + str(kid.care_taker_id))
                mySql_insert_query = """INSERT INTO kid (`care_taker_id`,`kid_lat`,`kid_long`,`kid_location`,`care_taker_msg`,`kid_response`,`kid_name`) 
                                                   VALUES (%s, %s, %s, %s, %s , %s, %s) """
                                                   

                record = (str(kid.care_taker_id),str(kid.kid_lat),str(kid.kid_long),str(kid.kid_location),str(kid.care_taker_msg),str(kid.kid_response),str(kid.kid_name))
                
                print ('mySql_insert_query record->', record)
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                care_taker_id = cursor.lastrowid
                print('care_taker_id-->' , care_taker_id)

                #AgentEmail().register_email(user.email, user_id)
                return care_taker_id

        except conn.Error as error:
                print ('executed sql-->', cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")


    @staticmethod
    def insert_care_taker_msg(finderCareTaker: FinderCareTaker):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('finderCareTaker.id str---->' + str(finderCareTaker.care_taker_id))
                mySql_insert_query = """INSERT INTO care_taker_msg (`care_taker_id`, `care_taker_msg`) 
                                                   VALUES (%s, %s) """
                finderCareTaker: FinderCareTaker
                record = (str(finderCareTaker.care_taker_id), str(finderCareTaker.care_taker_msg))
                print ('mySql_insert_query->', mySql_insert_query)
                print ('mySql_insert_query str(finderCareTaker.care_taker_msg)->', str(finderCareTaker.care_taker_msg))
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                care_taker_id = cursor.lastrowid
                print('insert care_taker_id-->' , care_taker_id)

                return care_taker_id

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    @staticmethod
    def del_all_worries(id):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "delete FROM care_taker_msg AS c WHERE c.care_taker_msg = 'No Worries.' and c.care_taker_id='" + id + "'";
        print ('sql->', sql)
        cursor.execute(sql)
        deleted_row_count = cursor.rowcount
        conn.commit()

        return deleted_row_count
    
    @staticmethod
    def get_care_taker_msg_history(id, limit):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "SELECT * FROM  care_taker_msg WHERE care_taker_id = '" + id + "' ORDER BY DATETIME DESC limit " + limit +"";
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        kid_list = [];
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            kid_json = json.dumps(json_data, indent=4, sort_keys=True, default=str)
            kid = json.loads(kid_json)
            print ('json_str-->' , json.dumps(kid, indent=4, sort_keys=True, default=str))
            kid_list.append(kid)
            json_data=[];
        print ('json_str list-->' , json.dumps(kid_list, indent=4, sort_keys=True, default=str))
        return json.dumps(kid_list)