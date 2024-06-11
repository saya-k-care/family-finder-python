import json

class FinderKid:
    
    kid_id = None
    care_taker_id = 'care_taker_id'
    kid_lat = 'care_taker_lat'
    kid_long = 'kid_long'
    kid_location = 'kid_location'
    kid_datetime = "kid_datetime"
    care_taker_msg = 'care_taker_msg'
    kid_response = 'kid_response'
    kid_name = 'kid_name'
    

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setKid(json_data):
        print ('json_data ====' , json_data)
        kid = FinderKid()
        kid = json.loads(json_data)

        print ('data received ====' , kid)

        # convert received person to local person Object
        kidLocal = FinderKid()
        kidLocal.__dict__ = kid

        return kidLocal