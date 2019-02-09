import os

"""
source: https://www.youtube.com/watch?v=ve2pmm5JqmI
rename the file so they start with the sequence number which is at the end of file name.
For example rename "Mars - Our Solar System - #5.mp4" 
  -> "#5-Our Solar System-Mars.mp4"
  -> "5-Our Solar System-Mars.mp4"
  -> "05-Our Solar System-Mars.mp4"
"""

## both of following will work (change directory)
#os.chdir(r'C:\Users\SKung.HUNTER\Desktop\Sam\YouTube')
#os.chdir('C:/Users/SKung.HUNTER/Desktop/Sam/YouTube')
path = r'C:\Users\SKung.HUNTER\Desktop\Sam\Programming\Python\Exercise_Hunter_PC\current\How_To\Automate_Parsing_and_Renaming_of_Multiple_Files\files_to_rename'
os.chdir( path )

## get current working directory
os.getcwd()

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split('-')
    
    # remove space and white spaces
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()
    #f_num = f_num.strip()[1:]  # remove the first character '#'
    #f_num = f_num.strip()[1:].zfill(2)  # 4->04, 7->07, 10->10
    new_name = '{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext)
    
    # take out course name if not necessary
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    
    print(new_name)
    
    ## update name
    os.rename(f, new_name)
    
    