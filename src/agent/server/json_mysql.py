from mysql.server.agent import Agent
class JsonMySQL:
    
    agent = [];
    
    @staticmethod
    def get_agent():
        
        #print ('returning persons--->' , JSONServerClass.persons) 
        return JsonMySQL.agent

    @staticmethod
    def setPerson(json_data):
        
        import json
        agent = json.loads(json_data)
        print ('data received ====' , agent)        
        
        # convert received person to local person Object
        local = Agent()
        local.__dict__ = agent
        #print ('received person--->' , person)
                    
        #print ('personLocal Name--->' , personLocal.name)
        #print ('personLocal address--->' , personLocal.address)
        
        JsonMySQL.persons.append(agent)       
         
        #print ('after add persons--->' , JSONServerClass.persons)
        return JsonMySQL.persons