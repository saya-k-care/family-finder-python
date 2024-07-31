import os

class GetAccessLog:

    @staticmethod
    def processAccessLog():
        filetorun = os.environ.get('NGINX_ACCESS_LOG_FILENAME')

        total_count = 0
        log_file_eyebot = ""
        print("filetorun-->" , filetorun)
        with open(str(filetorun)) as f:
            for line in f:
       # For Python3, use print(line)
                #print (line);
                if "eyebot" in line:
                    total_count = total_count + 1
                    #print(line)
                    log_file_eyebot = log_file_eyebot + line
        
        print ("total_count-->" , total_count)
        log_file_eyebot = "Total Count url with eyebot-->" + str(total_count) + "\n\n\n" + log_file_eyebot   
        return log_file_eyebot
if __name__ == '__main__':
    #n = len(sys.argv)
    #print("Total arguments passed:", n)

    # Arguments passed
    #print("\nFile to execute:", sys.argv[1])
    #filetorun = sys.argv[1]
    print ("log_file_eyebot-->" , str(GetAccessLog.processAccessLog()))



