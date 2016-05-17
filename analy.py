from __future__ import division
name = raw_input("Enter file:")
f = open(name)
counter = {'http':0,
			'ftp':0,
			'arp':0,
            'dhcp':0}
for line in f:
    for p in counter.keys():
        counter[p]+= line.count(p) > 0
total = counter['http'] + counter['ftp'] + counter['arp'] + counter['dhcp']

print '***************************************'
print '      $$ Analysis and numbers $$\n'
print 'We have a total of ',total,' packets sniffed\n'
print 'Numbers:\n'
print 'HTTP protocol: ', counter['http']
print 'FTP protocol: ', counter['ftp']
print 'ARP protocol: ', counter['arp']
print 'DHCP protocol: ', counter['dhcp']
print '\nAnalysis and percentage:\n'
print 'HTTP protocol: ', (int(counter['http'])/total)*100,'%'
print 'FTP protocol: ', (int(counter['ftp'])/total)*100,'%'
print 'ARP protocol: ', (int(counter['arp'])/total)*100,'%'
print 'DHCP protocol: ', (int(counter['dhcp'])/total)*100,'%'
