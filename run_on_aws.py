'''
programmatically runs word_count.py on aws
'''

import mrjob.util
import sys

from word_count import MRWordCounter

mrjob.util.log_to_stream(stream=sys.stdout)

mr_job = MRWordCounter(args=['-r', 'emr', 'README.md'])
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        print line
