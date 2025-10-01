import random
import string 
import time
import logging

#Setting up a loggin for erroe handling

logging.basicConfig(filename="log_generator_errors.log",level=logging.ERROR)

#List the level of the logs

LOG_LEVELS = ["INFO","DEBUG","ERROR","WARNING"]

ACTIONS=["Login","Logout","Data Request","File Upload","Download","Error"]

#Function to generate random Strings for logs

def generate_random_string(length=10):
    """
    Generates a random string of a given length (default length is 10 characters)
    """
    try:
        return ''.join(random.choices(string.ascii_letters + string.digits,k=length))
    except  Exception as e:
        logging.error(f"Error in generate_random_string: {e}")
        return "ERROR"
    
#Function to generste a random log entry

def generate_log_entry():
    """
    Generate a random log entry with a timestamp.log.level,action and user
    """    
    try:
        log_level=random.choice(LOG_LEVELS)
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
        action=random.choice(ACTIONS)
        user =generate_random_string(8)
        log_entry= f"{timestamp} - {log_level} - {action} - User {user}"

        return log_entry
    
    except Exception as e :
        logging.error(f"Error in generate log entry: {e}")
        return "Error"
    
    #Funtion to write logs to a file

def write_logs_to_file(logs_filename,num_entries=100):
    """
        Wtite a specifies number of the random logs to the given file
    """

    try:
        with open(logs_filename,'w') as file:
            for _ in range(num_entries):
                log=generate_log_entry()
                if log != "ERROR":
                   file.write(log+'\n')
        print(f"Logs have been successfully written to {logs_filename}")

    except Exception as e:
        logging.error(f"Error in write_logs to file: {e}")
        print("An error Occured while writing logs to the file")
    

#Generate and write 200 random entires
write_logs_to_file('Generated_logs.txt', num_entries=200) #CHange the number of the entries if required