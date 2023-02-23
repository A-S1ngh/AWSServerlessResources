import os

def hello(event, context):
    return "Memory Capacity: " + os.environ["MEM_VERSION"]
