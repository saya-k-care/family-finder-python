import json

class FinderCareTaker:
    
    care_taker_id = None
    care_taker_email = 'email'
    care_taker_password = 'password'
    care_taker_hp = 'HP'
    kid_name = 'Kids Name'
    care_taker_msg = 'msg'

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    @staticmethod
    def setCareTaker(json_data):
        print ('json_data ====' , json_data)
        careTaker = FinderCareTaker()
        careTaker = json.loads(json_data)

      #  print ('data received ====' , str(careTaker))

        # convert received person to local person Object
        careTakerLocal = FinderCareTaker()
        careTakerLocal.__dict__ = careTaker

        return careTakerLocal