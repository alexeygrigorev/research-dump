"""Local-only inspection/export. No remote admin route, refunds or emails."""
from __future__ import annotations
import argparse
import json
from contextlib import closing
import server

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('command', choices=['summary','export'])
args=parser.parse_args()
with closing(server.connect()) as con:
    applications=con.execute('SELECT * FROM applications ORDER BY created_at').fetchall()
    if args.command=='summary':
        print('Applications:',len(applications))
        print('Recorded paid sessions:',con.execute("SELECT COUNT(*) FROM payments WHERE payment_status='paid'").fetchone()[0])
        print('Flagged payments:',con.execute("SELECT COUNT(*) FROM payments WHERE flag<>'' OR payment_status='needs_review'").fetchone()[0])
        print('These counts do not imply accepted members or confirmed seats.')
    else:
        for row in applications:
            item=dict(row)
            item.pop('submission_key',None)
            item.pop('payload_hash',None)
            item['answers']=json.loads(item['answers'])
            item['payments']=[dict(p) for p in con.execute('SELECT * FROM payments WHERE application_id=?',(item['id'],))]
            print(json.dumps(item,ensure_ascii=False))
        unmatched=[dict(p) for p in con.execute('SELECT * FROM payments WHERE application_id IS NULL')]
        if unmatched: print(json.dumps({'unmatched_payments':unmatched},ensure_ascii=False))
