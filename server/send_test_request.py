#!/usr/bin/env python

import beanstalkc
import json
import sys

print "Getting build details from jenkins"
beanstalk_host = sys.argv[1]
image_details = {}
image_details['name_space'] = sys.argv[2]
image_details['name'] = sys.argv[3]
image_details['tag']  = sys.argv[4]
image_details['action'] = "start_test"
print "Pushing image details in the tube"
bs = beanstalkc.Connection(host=beanstalk_host)
bs.use("master_tube")
bs.put(json.dumps(image_details))
print "image details is pushed to tube for testing"
