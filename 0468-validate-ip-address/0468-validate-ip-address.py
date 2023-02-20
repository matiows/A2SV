class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            str_ip = list(queryIP.split('.'))
            count = 0
            
            for ip in str_ip:
                if not ip.isnumeric() or ip != str(int(ip)):
                    break
                if 0 <= int(ip) < 256:
                    count += 1

            if count == 4:
                return "IPv4"
            
        elif queryIP.count(':') == 7:
            count = 0
            str_ip = list(queryIP.split(':'))
            count = 0
            
            for ip in str_ip:
                if ip.isalnum() and 0 < len(ip) < 5:
                    f = 0
                    for ch in ip:
                        if 48 <= ord(ch) <= 57 or 97 <= ord(ch) <= 102 or 65 <= ord(ch) <= 70:
                            f += 1
                            
                    if f == len(ip):
                        count += 1
                    
            if count == 8:
                return "IPv6"
            
        
        return 'Neither'