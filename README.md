# streaming-03-bonus-harvey

* Beth Harvey
* Streaming Data
* Module 3 Bonus
* September 5, 2023

The goal of this bonus section is to read individual lines from a CSV file, use RabbitMQ to send and receive the messages, and write the messages to a new CSV file.

CSV Data Source: https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data

## My Process
1. Create and activate virtual environment .venv
    `python3 -m venv .venv`
    `.venv/bin/activate`
2. Install required third-party libraries from requirements.txt
    `python3 -m pip install -r requirements.txt`
3. Add 'dataset_olympics.csv' dataset from Kaggle (source listed above). This dataset contains information for over 35,000 Olympics entries between 1896 and 2016. Many athletes are listed more than once, because they competed in more than one event.
4. Create new file 'produce_message.py' to produce messages.
5. Use a combination of 'v1_emit_message.py' from the main part of the Module 3 assignment and 'process_streaming_0.py' from the Module 2 assignment to create a function to create messages from individual rows of the CSV file and send them to a RabbitMQ queue. This function creates a blocking connection, a communication channel, and declares a queue for RabbitMQ use. It then opens the CSV file for reading and creates a message from each row. Then, it sends the message to the RabbitMQ queue. This process is repeated every 3 seconds for the next row. If the process is not interrupted, the connection is closed after the entire file is sent.
6. Use a combination of 'v1_listen_for_message.py' from the main part of the Module 3 assignment and 'process_streaming_0.py' from the Module 2 assignment to listen for messages in the queue and write messages to an output CSV file. This function also creates a blocking connection, a communication channel, and declares a quque for RabbitMQ use. When a message is received, it is added as a new line to the output file.

![sending and receiving messages](/send_and_receive_messages.png)


## Bonus Section Instructions

1. Create  your own custom project. Create a new repo named streaming-03-bonus-yourname. (e.g., streaming-03-bonus-case)
2. Create a new producer that reads from your earlier CSV file and writes messages to a new queue every 1-3 seconds.
3. Create a new consumer that reads your messages from this queue, and writes the messages to a new file as they are received.
4. Your README.md must include your name, the date.
5. Your README.md must provide a link to the original data.
6. Your README.md must clearly describe what you did, telling the story of your data, your producer, and your consumer,
7. Your README.md must display a screenshot of the two windows running concurrently. 
8. Add a .gitignore (telling which files and directories NOT to push up to GitHub).  Recommendation:  copy .gitignore from an earlier repo. 
9. These are the important skills you want to demonstrate. Create unique streaming projects, using professional communication. I encourage you to give it a try. 