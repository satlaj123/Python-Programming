# WAP to mask the email id content keep only first and last char rest will be *.

emails_list= [
    "arjun.mehra@gmail.com",
    "sneha_k@outlook.com",
    "rahul.sharma@yahoo.com",
    "priya.verma@protonmail.com",
    "vivek.desai@zoho.com",
    "ananya.patil@rediffmail.com",
    "rohit.kapoor@icloud.com",
    "meena.nair@gmx.com",
    "akash.jain@aol.com",
    "divya.singh@mail.com"
]


for i in emails_list:
   name,domain = i.split('@')
   if len(name) > 2:
       mask = name[0] + '*'*(len(name)-2) + name[-1]
   else:
       mask = name
   mask_with_domain = mask + '@' + domain
   print(mask_with_domain)