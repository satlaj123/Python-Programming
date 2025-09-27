from loguru import logger

count = 0
paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

paragraph_lst = paragraph.lower().split(" ")

for letter in paragraph_lst:
    if letter == 'the':
        count += 1
    else:
        continue

logger.info(f"Total count of article 'the' is {count}.")