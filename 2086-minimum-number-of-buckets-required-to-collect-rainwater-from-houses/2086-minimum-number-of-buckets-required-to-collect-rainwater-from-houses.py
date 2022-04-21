class Solution:
    def minimumBuckets(self, street: str) -> int:
        if street == '.':
            return 0
        if street == 'H' or street[-2:] == 'HH' or street[:2] == 'HH' or 'HHH' in street:
            return -1

        else:
            return street.count('H') - street.count('H.H')