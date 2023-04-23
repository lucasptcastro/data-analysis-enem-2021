import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get(environment):
  return os.environ.get(environment)

def getSplit(environment, split):
  return [i for i in get(environment).split(split)]