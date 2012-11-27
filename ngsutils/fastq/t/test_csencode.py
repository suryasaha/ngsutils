#!/usr/bin/env python
'''
Tests for bedutils reduce
'''

import unittest
import StringIO

from ngsutils.fastq import FASTQ
import ngsutils.fastq.csencode


class EncodeTest(unittest.TestCase):
    def testEncode(self):
        ret = ngsutils.fastq.csencode.encoded_seq('0123456.')

        self.assertEqual('ACGTNNNN', ret)

    def testFQRead(self):
        fq = StringIO.StringIO('''\
@foo
T0000111122223333....
+
....................
''')
        out = StringIO.StringIO('')
        ngsutils.fastq.csencode._fastq_csencode(FASTQ(fileobj=fq), out=out)

        self.assertEqual('''@foo
AAACCCCGGGGTTTTNNNN
+
...................
''', out.getvalue())


if __name__ == '__main__':
    unittest.main()
