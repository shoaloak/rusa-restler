# Copyright (c) Axel Koolhaas.
# Licensed under the MIT License.

import json
import threading
import queue

import zmq

from meta.singleton import Singleton

START_TAG = "RUSA"
STOP_TAG = "HALT"
EMPTY_OBJ = "{}"

""" Implements a queue using ZeroMQ logic for dynamic fuzzing. """
# class ZmqClient(threading.Thread, metaclass=Singleton):
class ZmqClient(metaclass=Singleton):
    """ ZMQ client class for instrumentation communication
    """
    def __init__(self, host=None, port=None):
        # threading.Thread.__init__(self)

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.host = host
        self.port = port

    # def abort(self):
    #     self.should_run = False

    # def run(self):
    #     """ Thread entrance - communicate with ZMQ server
    #     """
    #     self.socket.connect('tcp://' + self.host + ':' + str(self.port))

        # receiving messages
        # while self.should_run:
        #     try:
        #         message = self.socket.recv(flags=zmq.NOBLOCK).decode('utf-8')
        #         self.q.put(message)
        #         # self.socket.send("gottem");
        #         # print(f"Received reply {message}")
        #     except zmq.Again as e:
        #         pass

    def connect(self):
        self.socket.connect('tcp://' + self.host + ':' + str(self.port))
        # Handshake
        self.send(START_TAG)
        if ''.join(self.recv_all()) != START_TAG:
            return False
        return True

    def disconnect(self):
        self.send(STOP_TAG)
        self.socket.disconnect('tcp://' + self.host + ':' + str(self.port))
        # term() could theoretically hang
        self.context.destroy()

    def send(self, msg):
        """ Send message to ZMQ server
        """
        self.socket.send(msg.encode('utf-8'))

    def recv_all(self):
        """ Receive all messages from ZMQ server
        """
        messages = []
        while True:
            try:
                messages.append(self.socket.recv().decode('utf-8'))
            except zmq.ZMQError as e:
                if e.errno == zmq.EAGAIN:
                    # No more messages to receive
                    break
                else:
                    # Handle other ZeroMQ errors
                    # raise
                    break
        return messages

    def recv_json(self):
        return json.loads(''.join(self.recv_all()))

    def hit(self):
        """ Helper method to verify if there was a hit """
        if not self.q.empty():
            self.q.queue.clear()
            return True
        else:
            return False

    def calc_distance(self):
        """ Get the minimum distance from the queue and clear the queue
        """
        if self.q.empty():
            return None

        min_dist = None
        while not self.q.empty():
            msg = self.q.get()
            dist = int(msg)
            print(dist)
            if min_dist is None or dist < min_dist:
                min_dist = dist
        return min_dist
