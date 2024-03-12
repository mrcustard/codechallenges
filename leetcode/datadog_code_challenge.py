#!/usr/bin/env python

from collections import defaultdict, Counter

class Solution:
    def getTagCounts(self, stream: []) -> defaultdict:
        count = defaultdict(int)
        for line in stream:
            split = line.split('|')
            if len(split) > 1:
                tags = split[2].split(',')
                for tag in tags:
                    count[tag] += 1



        return count


stream = [
    'system.load.1|1|host:a,role:web,availability-zone:us-east-1a',
    'system.load.15|1|host:b,role:web,availability-zone:us-east-1b',
    'system.cpu.user|20|host:a,role:web,availability-zone:us-east-1a',
    'postgresql.locks|12|host:c,role:db,db_role:master,availability-zone:us-east-1e',
    'postgresql.db.count|2|host:d,role:db,db_role:replica,availability-zone:us-east-1a',
    'kafka.consumer.lag|20000|host:e,role:intake,availability-zone:us-east-1a',
    'kafka.consumer.offset'
]

s = Solution()
for key, value in s.getTagCounts(stream).items():
    print(key, value)