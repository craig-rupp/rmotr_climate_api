import requests
import json
import csv


from skywiseinsight import InsightResource

InsightResource.set_user('ebe2c339')
InsightResource.set_password('5c0bf7f167fbc08e79d6ba767abdefea')

precip = dp.location(35.4, -97.5)
print(json.dumps(precip.json()))