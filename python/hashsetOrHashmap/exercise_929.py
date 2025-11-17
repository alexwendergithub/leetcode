class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailList = []
        count = 0
        for email in emails:
            emailsplit = email.split('@')
            emailsplit[0] = emailsplit[0].replace(".", "")
            email = emailsplit[0].split("+")[0]+'@'+emailsplit[1]
            print(email)
            if email not in emailList:
                count+=1
                emailList.append(email)
        return count