from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import subprocess
import argparse
import sys

path = None

def your_job(path):
        logging.info("executing " , str('python3 ' + path))
        subprocess.call(['sh', str('python3 ' + path)])

if __name__ == '__main__':
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nFile to execute:", sys.argv[1])
    path = sys.argv[1]
    print("\nMinutes:", sys.argv[2])
    minute = int(sys.argv[2])
    logging.basicConfig(filename='schedule',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

    logger = logging.getLogger('urbanGUI')

    logging.info("Starting scheduler")
    scheduler = BlockingScheduler()
    scheduler.add_job(your_job(path), 'interval', minutes=minute)
    scheduler.start()

