"""
    Beth Harvey
    September 5, 2023
    This program prepares and sends a message from the Olympics dataset to a queue on the RabbitMQ server.

"""

# add imports at the beginning of the file
import logging
import csv
import time
import pika

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# declare program constants
HOST = "localhost"
INPUT_FILE_NAME = "dataset_olympics.csv"
QUEUE_NAME = "hello"

# define function to create and send messages from a csv
def get_message_from_row(input_file_name, host_name, queue_name):
    """Read from input file and send data."""
    logging.info(f"Starting to send data from {input_file_name}.")

    # create a blocking connection to the RabbitMQ server
    conn = pika.BlockingConnection(pika.ConnectionParameters(host_name))

    # use the connection to create a communication channel
    ch = conn.channel()

    # use the channel to declare a queue
    ch.queue_declare(queue=queue_name)

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")
        
        header = next(reader)  # Skip header row
        logging.info(f"Skipped header row: {header}")

        # For each data row in the reader
        for row in reader:
            
            # Join row elements into string
            MESSAGE = ','.join(row)
            logging.info(f"Prepared Message: {MESSAGE}.")

            # use the channel to publish a message to the queue
            ch.basic_publish(exchange="", routing_key=queue_name, body=f'{MESSAGE}')
            logging.info(f"Sent Message: {MESSAGE}")

            time.sleep(3) # wait 3 seconds between messages

    # close the connection to the server
    conn.close()


if __name__ == '__main__':
    try: 
        logging.info("===============================================")
        logging.info('Starting producing process')
        get_message_from_row(INPUT_FILE_NAME, HOST, QUEUE_NAME)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

