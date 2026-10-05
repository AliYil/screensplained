"""Letter frequencies of Turkish text and where each letter sits on Turkish Q and F.

Usage: python3 freq.py <Leipzig *-sentences.txt files>
"""
import collections, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layouts as L
parts=[]
for f in sys.argv[1:]:
    with open(f,encoding='utf-8') as fh:
        for line in fh: parts.append(line.split('\t',1)[-1])
text=L.letters_tr("".join(parts))
ws=collections.Counter(L.words(text,L.TR_ALPHA))
cnt=collections.Counter()
for w,c in ws.items():
    for ch in w: cnt[ch]+=c
n=sum(cnt.values())
q=L.build('trq'); fk=L.build('trf')
FN={'LP':'L pinky','LR':'L ring','LM':'L middle','LI':'L index','RI':'R index','RM':'R middle','RR':'R ring','RP':'R pinky'}
RN={'AD':'top','AC':'home','AB':'bottom'}
print(f"{'ch':3}{'%':>6}  {'Q: row/finger':22}{'F: row/finger':22}")
for ch,c in cnt.most_common():
    a=q[ch]; b=fk[ch]
    print(f"{ch:3}{100*c/n:6.2f}  {RN[a['row']]+' '+FN[a['finger']]:22}{RN[b['row']]+' '+FN[b['finger']]:22}")
# vowel share
V=set('aeıioöuü')
print('vowels %', round(100*sum(cnt[v] for v in V)/n,1))
# top10 on home keys
top10=[ch for ch,_ in cnt.most_common(10)]
for name,m in (('Q',q),('F',fk)):
    hk=[ch for ch in top10 if m[ch]['row']=='AC' and m[ch]['col']==L.HOME_COL[m[ch]['finger']]]
    hr=[ch for ch in top10 if m[ch]['row']=='AC']
    print(name,'top10 on home keys:',hk,'| on home row:',hr)
# CV alternation in text: share of within-word bigrams that are vowel<->consonant
cv=tot=0
for w,c in ws.items():
    for x,y in zip(w,w[1:]):
        tot+=c
        if (x in V)!=(y in V): cv+=c
print('vowel/consonant alternating bigrams %', round(100*cv/tot,1))
print('total letters', n, 'distinct words', len(ws), 'tokens', sum(ws.values()))
