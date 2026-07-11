class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def process(email):
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            return local + '@' + domain

        rcv = set()
        for email in emails:
            rcv.add(process(email))
        
        return len(rcv)