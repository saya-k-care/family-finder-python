from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import subprocess
import argparse
import sys

filetorun = None

def your_job(filetorun):
        logging.info("executing " + "test")
        subprocess.Popen('python3 ' + filetorun, shell=True)

def your_job2():
        logging.info("executing " + "test" + filetorun)
        subprocess.Popen('python3 ' + filetorun, shell=True)

if __name__ == '__main__':
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nFile to execute:", sys.argv[1])
    filetorun = sys.argv[1]
    print("\nMinutes:", sys.argv[2])
    minute = int(sys.argv[2])
    logging.basicConfig(filename='schedule.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

    logger = logging.getLogger('urbanGUI')

    logging.info("Starting scheduler")
    scheduler = BlockingScheduler()
    scheduler.add_job(your_job2, 'interval', minutes=minute)
    scheduler.start()

