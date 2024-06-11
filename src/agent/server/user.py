import json
class User:
    
    email = 'email@com'
    user_id = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setUser(json_data):
        print ('json_data ====' , json_data)
        user = User()
        user = json.loads(json_data)

        print ('user received ====' , user)

        # convert received person to local person Object
        userLocal = User()
        userLocal.__dict__ = user

        return userLocal 
