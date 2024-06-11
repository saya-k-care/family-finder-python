import json
from agent.server.address import Address
class Agent:
    
    name = 'A Name'
    address = 'An Address'
    postcode = 'An postcode'
    gpsUrl = None;
    fullName = None
    email = None
    contactNumber = None 
    address = Address();
    address_id = None
    url = None
    desc = None
    user_id = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setAgent(json_data):
        print ('json_data ====' , json_data)
        agent = Agent()
        agent = json.loads(json_data)

        print ('data received ====' , agent)

        # convert received person to local person Object
        agentLocal = Agent()
        agentLocal.__dict__ = agent

        addressLocal = Address()
        addressLocal.__dict__ = agent['address'] 

        agentLocal.address = addressLocal
        
        return agentLocal 