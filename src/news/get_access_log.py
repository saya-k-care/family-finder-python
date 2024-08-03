import os
import re
import json

class GetAccessLog:

    @staticmethod
    def getUser(log_entry, access_set):
        # Split the log entry by spaces
        log_parts = log_entry.split()

        # Extract the last string (IP address)
        ip_address = log_parts[-1]

        # Extract the date and time using regular expression
        datetime_pattern = r'\[(.*?)\]'
        match = re.search(datetime_pattern, log_entry)
        
        if match:
            date_and_time = match.group(1)
            date_time_str = date_and_time[12:17]  # Extract characters between positions 12 and 17
            #print(f'Extracted Date and Time: {date_time_str}')
        else:
            print('Date and Time not found in the log entry.')
            return

        start_index = log_entry.find("http")
        http_string = None

        # Find the position of the closing double quote after "http"
        if start_index != -1:
            end_index = log_entry.find('"', start_index)
            if end_index != -1:
                http_string = log_entry[start_index:end_index]
                if "undefined" in http_string or "news" in http_string or "gospel" in http_string:
                    isUser = True
                else:
                    http_string = None

        if http_string is not None:
            user = f"[TIME]={date_time_str} [URL]={http_string} [IP]={ip_address}"

            access_set.add(user)
            #print("User-->", user)
        return access_set
    
    @staticmethod
    def processAccessLog():
        filetorun = os.environ.get('NGINX_ACCESS_LOG_FILENAME')

        total_count = 0
        print("filetorun-->" , filetorun)
        with open(str(filetorun)) as f:
            
            access_set = set()
            for line in f:
                total_count = total_count + 1
                access_set = GetAccessLog.getUser(line,access_set)                    
        
        #print ("total_count-->" , total_count)
        sorted_list = sorted(access_set)
        json_data = json.dumps(list(sorted_list))  # Convert set to list before JSON serialization

        log_file_eyebot = "Total Website Hits-->" + str(total_count) + " Total Users Count -->" + str(len(access_set)) + "\n\n\n" + str(json_data)
        return log_file_eyebot
if __name__ == '__main__':
    #n = len(sys.argv)
    #print("Total arguments passed:", n)

    # Arguments passed
    #print("\nFile to execute:", sys.argv[1])
    #filetorun = sys.argv[1]
    print ("log_file_eyebot-->" , str(GetAccessLog.processAccessLog()))



