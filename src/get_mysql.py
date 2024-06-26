import json
import os
import sys

import web

from agent.server.address import Address
from agent.server.agent import Agent
from agent.server.agent_db import AgentDB
from agent.server.donate import Donate
from agent.server.user import User
from finder.server.finder_care_taker import FinderCareTaker
from finder.server.finder_db import FinderDB
from finder.server.finder_kid import FinderKid

sys.path.append('../')
sys.path.append('../../')

URLS = (
    '/json/get', 'JsonGet',
    '/json/getUser', 'JsonGetUser',
    '/json/post', 'JsonPost',
    '/register/post', 'CreatePost',
    '/donate/post', 'DonatePost',
    '/finder/location/get', 'FinderGetLocation',
    '/finder/register', 'FinderRegister',
    '/finder/update', 'FinderUpdate',
    '/finder/login', 'FinderLogin',
    '/finder/caretaker/get', 'FinderGetCareTakerByID',
    '/finder/caretaker/update', 'FinderUpdateCareTakerByID',
    '/finder/kid/get', 'FinderGetCareTakerByEmail',
    '/finder/gospel/get', 'FinderGospel',
    '/finder/caretaker/insertmsg', 'FinderInsertCareTakerMsg',
    '/finder/caretaker/getmsgHistory', 'FinderGetCareTakerMsgHistory',
     '/finder/caretaker/delAllWorries', 'FinderDelAllWorries',

)

class DonatePost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('CreatePost starting' )

        json_data = web.data()
        
        donate = Donate.setUser(json_data)
        print('donate-->' , donate )
        print('donate email-->' , donate.email )
        # need to convert to List Object to Json String else Angular cannot process it 
        user_id = AgentDB.createDonateDB(donate)
        return user_id
        
        #return jsonString
    def OPTIONS(self):
        
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('OPTIONS starting' )
        
class CreatePost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        
        print('CreatePost starting' )

        json_data = web.data()
        
        user = User.setUser(json_data)
        print('user-->' , user )
        print('user email-->' , user.email )
        # need to convert to List Object to Json String else Angular cannot process it 
        user_id = AgentDB.createUserDB(user)
        return user_id
        
        #return jsonString
    def OPTIONS(self):

        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('OPTIONS starting' )

class JsonPost(object):

    def POST(self):
        
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        
        print('JsonPost starting' )

        json_data = web.data()
        
        agent = Agent.setAgent(json_data)
        print('agent-->' , agent )
        # need to convert to List Object to Json String else Angular cannot process it 
        AgentDB.insertDB(agent)
        
        #return jsonString
    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin','*')
        web.header('Access-Control-Allow-Methods', 'content-type');
        print('OPTIONS starting' )

class Redirect(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        print ('here')
        user_input = web.input()

class FinderRegister(object):

    def POST(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        
        json_data = web.data()
        finderCareTaker = FinderCareTaker.setCareTaker(json_data)
        print('finderCareTaker-->' , finderCareTaker )
        return FinderDB.register(finderCareTaker);

class FinderUpdate(object):

    def POST(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        
        json_data = web.data()
        finderKid = FinderKid.setKid(json_data)
        print('finderKid-->' , finderKid )
        return FinderDB.update(finderKid);

class FinderGetLocation(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        return FinderDB.get_location(user_input.id)

class FinderLogin(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        print('user_input--->' , user_input)
        return FinderDB.login(user_input.care_taker_email, user_input.care_taker_password)
    
class FinderGetCareTakerByID(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        return FinderDB.get_caretaker_by_id(user_input.id)

class FinderUpdateCareTakerByID(object):

    def POST(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        
        json_data = web.data()
        finderCareTaker = FinderCareTaker.setCareTaker(json_data)
        print('update finderCareTaker json_data-->' , json_data )
        FinderDB.insert_care_taker_msg(finderCareTaker);
        return FinderDB.update_caretaker_by_id(finderCareTaker);

class FinderGetCareTakerByEmail(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        user_input = web.input()
        return FinderDB.get_caretaker_by_email(user_input.email)

class FinderGospel(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        return FinderDB.get_gospel()

class FinderGetCareTakerMsgHistory(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        
        user_input = web.input()
        print('user_input id-->' , user_input.id )
        print('user_input limit-->' , user_input.limit )
        return FinderDB.get_care_taker_msg_history(user_input.id, user_input.limit);

class FinderDelAllWorries(object):

    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        web.header('strict-origin-when-cross-origin', 'true')
        
        user_input = web.input()
        print('user_input id-->' , user_input.id )
        return FinderDB.del_all_worries(user_input.id);
    
def get_agent():
        agent = Agent()
        agent.fullName = "Testing"
        agent.contactNumber ="000"
        agent.email = "a.com"
        address = Address()
        address.fullAddress = "address";
        address.country = "MY"
        address.state = "1212"
        address.city = "KL"
        
        agent.address = address

        print ('agent ====' , agent.toJSON())
        return agent.toJSON()
    
def main():
    """
    Main function starting app
    """
    print (sys.path)
    from cheroot.server import HTTPServer
    from cheroot.ssl.builtin import BuiltinSSLAdapter
    
    ssl_cert = 'cert.crt'
    ssl_key = 'key.key'

    #HTTPServer.ssl_adapter = BuiltinSSLAdapter(certificate=ssl_cert,private_key=ssl_key)

    #get_agent()
    #user = User()
    #user.email = 'pcyuen98@gmail.com'
    #user_id = createUserDB(user)

    #print ('user_id-->' , str(user_id))
    http_app = web.application(URLS, globals());
    os.environ["PORT"] = "8880";
    http_app.run()
if __name__ == "__main__":
    main()

