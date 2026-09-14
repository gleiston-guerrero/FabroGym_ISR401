#!/usr/bin/env python3
from pathlib import Path
import hashlib, re, sys
ROOT=Path(__file__).resolve().parents[2]
MAN=ROOT/'checksums.sha256'
LFS_OID=re.compile(r'^oid sha256:([0-9a-f]{64})$',re.M)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
def main():
 ok=bad=0
 for line in MAN.read_text(encoding='utf-8').splitlines():
  if not line.strip(): continue
  expected, rel=line.split('  ',1); p=ROOT/rel
  if not p.exists(): print('FALTA',rel); bad+=1; continue
  raw=p.read_bytes() if p.stat().st_size<4096 else b''
  if raw.startswith(b'version https://git-lfs.github.com/spec/v1'):
   m=LFS_OID.search(raw.decode('utf-8','replace'))
   actual=m.group(1) if m else ''
   label='OK-LFS' if actual==expected else 'FALLO-LFS'
  else:
   actual=sha(p); label='OK' if actual==expected else 'FALLO'
  print(f'{rel}: {label}')
  if actual==expected: ok+=1
  else: bad+=1
 print(f'RESUMEN: {ok} correctos; {bad} fallos')
 return 0 if bad==0 else 2
if __name__=='__main__': sys.exit(main())
