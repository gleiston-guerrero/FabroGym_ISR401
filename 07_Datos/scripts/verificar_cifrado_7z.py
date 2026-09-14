#!/usr/bin/env python3
"""Verifica cifrado AES en contenedores 7z accesibles y documenta punteros Git LFS."""
from pathlib import Path
import lzma, re, struct, sys
ROOT=Path(__file__).resolve().parents[2]
AES=bytes.fromhex('06f10701')

def read_u64(d,pos):
    first=d[pos]; pos+=1; mask=0x80; val=0
    for i in range(8):
        if first & mask == 0:
            val |= (first & (mask-1)) << (8*i); return val,pos
        val |= d[pos] << (8*i); pos+=1; mask >>=1
    return val,pos

def lfs_pointer(b):
    if not b.startswith(b'version https://git-lfs.github.com/spec/v1'): return None
    s=b.decode('utf-8','replace'); oid=re.search(r'^oid sha256:([0-9a-f]{64})$',s,re.M); size=re.search(r'^size (\d+)$',s,re.M)
    return (oid.group(1) if oid else '', int(size.group(1)) if size else 0)

def has_aes_7z(path):
    b=path.read_bytes()
    if b[:6] != bytes.fromhex('377abcaf271c'): return False,'NO_ES_7Z'
    off=struct.unpack('<Q',b[12:20])[0]; sz=struct.unpack('<Q',b[20:28])[0]
    nh=b[32+off:32+off+sz]
    if AES in nh: return True,'AES_EN_CABECERA'
    if nh and nh[0]==0x17: # encoded header
        pos=1
        if nh[pos]!=0x06: return False,'CABECERA_CODIFICADA_NO_INTERPRETABLE'
        pos+=1; packpos,pos=read_u64(nh,pos); nstreams,pos=read_u64(nh,pos)
        if nstreams!=1 or nh[pos]!=0x09: return False,'STREAMS_NO_SOPORTADOS'
        pos+=1; packsize,pos=read_u64(nh,pos)
        # locate LZMA properties in encoded-header folder (this archive shape is standard/simple)
        marker=bytes.fromhex('03010105')
        m=nh.find(marker)
        if m<0: return False,'CODER_CABECERA_NO_LZMA'
        props=nh[m+4:m+9]
        p0=props[0]; lc=p0%9; r=p0//9; lp=r%5; pb=r//5; dsz=int.from_bytes(props[1:5],'little')
        packed=b[32+packpos:32+packpos+packsize]
        dec=lzma.LZMADecompressor(format=lzma.FORMAT_RAW,filters=[{'id':lzma.FILTER_LZMA1,'dict_size':dsz,'lc':lc,'lp':lp,'pb':pb}])
        decoded=dec.decompress(packed)
        return (AES in decoded, 'AES_EN_CABECERA_DECODIFICADA' if AES in decoded else 'AES_NO_DETECTADO')
    return False,'AES_NO_DETECTADO'

def main():
    targets=[
      ROOT/'10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z',
      ROOT/'02_Evidencias/00_Restringido/evidencias_restringidas.7z',
    ]
    bad=0
    for p in targets:
        rel=p.relative_to(ROOT).as_posix(); b=p.read_bytes(); l=lfs_pointer(b)
        if l:
            print(f'{rel}: GIT_LFS oid={l[0]} size={l[1]} bytes')
            continue
        ok,detail=has_aes_7z(p)
        print(f'{rel}: {"CIFRADO_AES_VERIFICADO" if ok else "CIFRADO_AES_NO_VERIFICADO"} ({detail})')
        if not ok: bad+=1
    return 0 if bad==0 else 2
if __name__=='__main__': sys.exit(main())
