import json
class Donate:
    
    email = 'email@com'
    donate_id = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setUser(json_data):
        print ('json_data ====' , json_data)
        donate = Donate()
        donate = json.loads(json_data)

        print ('donate received ====' , donate)

        # convert received person to local person Object
        donateLocal = Donate()
        donateLocal.__dict__ = donate

        return donateLocal 
