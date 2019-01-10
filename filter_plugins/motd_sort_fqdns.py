#!/usr/bin/env python3

def motd_sort_fqdns(fqdns):
	reversed_fqdns = []
	for fqdn in fqdns:
		reversed_fqdn = '.'.join(fqdn.split('.')[::-1])
		reversed_fqdns.append(reversed_fqdn)
	reversed_fqdns.sort()
	sorted_fqdns = []
	for reversed_fqdn in reversed_fqdns:
		fqdn = '.'.join(reversed_fqdn.split('.')[::-1])
		sorted_fqdns.append(fqdn)
	return sorted_fqdns



class FilterModule(object):
    def filters(self):
        return {
            'motd_sort_fqdns': motd_sort_fqdns,
        }
