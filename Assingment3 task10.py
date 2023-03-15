n=input()
s1,s2=n.split(", ")
m_l=min(len(s1),len(s2))
m_s=""
for i in range(m_l):
    m_s+=s1[i]+s2[i]
if len(s1)>len(s2):
    m_s+=s1[m_l:]
else:
    m_s+=s2[m_l:]
print(m_s)