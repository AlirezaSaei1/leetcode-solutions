class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.lower().split('@')
            return f"{name[0]}*****{name[-1]}@{domain}"
        
        digits = [c for c in s if c.isdigit()]
        local = "***-***-" + "".join(digits[-4:])
        
        country_code = len(digits) - 10
        if country_code == 0:
            return local
        return f"+{ '*' * country_code }-" + local