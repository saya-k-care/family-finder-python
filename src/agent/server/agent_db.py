import pymysql as MySQLdb
import json
import sys

import web
from agent.server.email_client import AgentEmail
from agent.server.donate import Donate
from agent.server.user import User
from agent.server.agent import Agent
from agent.server.address import Address
class AgentDB:
    @staticmethod
    def get_agent_db(id):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "select * from agent where agent_id = " + str(id);
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
            agent_json = json.dumps(json_data[0])
    
            agent = json.loads(agent_json)
            address_json = AgentDB.get_address_db(agent['address_id'])
            agent['address'] = json.loads(address_json)
            print ('json_str-->' , json.dumps(agent))
            return json.dumps(agent)
    
    @staticmethod
    def get_user_db(id):
    
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()
        sql = "select * from user where user_id = " + str(id);
        print ('sql->', sql)
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()

        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(row_headers,result)))
        user_json = json.dumps(json_data[0])
    
        user = json.loads(user_json)
        print ('user -->' , user)

        return user_json

    @staticmethod
    def get_address_db(address_id):
        conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
        cursor = conn.cursor()

        cursor.execute("select * from address where address_id=" + str(address_id))
        row_headers=[x[0] for x in cursor.description] #this will extract row headers
        myresult = cursor.fetchall()
        #print('myresult-->', myresult)
        #for x in myresult:
         #   print(x)

        json_data=[]
        for result in myresult:
                json_data.append(dict(zip(row_headers,result)))
        json_str = json.dumps(json_data[0])
        return json_str

    @staticmethod
    def createDonateDB(donate: Donate):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('donate.email---->' + donate.email)
                print ('donate.email str---->' + str(donate.email))
                mySql_insert_query = """INSERT INTO donate (`email`) 
                                                   VALUES (%s) """
                donate: Donate
                record = (str(donate.email))
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                user_id = cursor.lastrowid
                print('user_id-->' , user_id)

                return user_id

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    @staticmethod
    def createUserDB(user: User):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()
                print ('user.email---->' + user.email)
                print ('user.email str---->' + str(user.email))
                mySql_insert_query = """INSERT INTO user (`email`) 
                                                   VALUES (%s) """
                user: User
                record = (str(user.email))
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                user_id = cursor.lastrowid
                print('user_id-->' , user_id)

                AgentEmail().register_email(user.email, user_id)
                return user_id

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
                
    @staticmethod
    def insertDB(agent: Agent):
        try:
                conn=MySQLdb.connect(host="bayi",user="admin",passwd="password", db="eyebot_agent")
                cursor = conn.cursor()

                mySql_insert_query = """INSERT INTO address (`fullAddress`, `country`, `state`, `city`) 
                                                   VALUES (%s, %s, %s, %s) """
                address: Address
                address = agent.address
                
                record = (address.fullAddress, address.country, address.state, address.city)
                print ('mySql_insert_query->', mySql_insert_query)
                cursor.execute(mySql_insert_query, record)

                conn.commit()
                address_id = cursor.lastrowid
                print('address_id-->' , address_id)

                mySql_insert_query = """INSERT INTO agent (`fullName`, `contactNumber`, `email`,`gpsURL`,`address_id`, `url`, `desc`, `user_id`) 
                                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
                                                   
                record = (agent.fullName, agent.contactNumber, agent.email, agent.gpsUrl, address_id, agent.url, agent.desc, agent.user_id)

                cursor.execute(mySql_insert_query, record)
                print (cursor._executed)
                conn.commit()

                agent_id = cursor.lastrowid
                print('agent_id-->' , agent_id)
                
                user = AgentDB.get_user_db(agent.user_id)
                wjdata = json.loads(user)
                print('email->' + wjdata["email"]);

                AgentEmail().send_email(wjdata["email"], agent_id, agent.fullName)

        except conn.Error as error:
                print (cursor._executed)
                print("Failed to insert record into MySQL table {}".format(error))

        finally:
                print (cursor._executed)
                cursor.close()
                conn.close()
