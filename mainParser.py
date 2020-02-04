#
#   @author - Christopher Lewis
#   @date = 2/3/2020
#   @note - python program that scans a given file for certain atttributes, in this case it was for
#       file changes, insertions and deletions from the git command below.
#
#        git log --author= <authorName> --oneline --shortstat --no-merges --before="2017-01-01" --until="2017-06-30" > output.txt
#
#
import re

path = "/Users/clew1/Desktop/Repository/CS472/brew/output.txt"


with open(path,encoding="utf8" ) as fp:

    count = 0
    final_fileDeletions = 0
    final_fileInsertions = 0
    final_fileChanges = 0

    fileDeletions = 0
    for line in fp:
        count = count + 1
        if ( count % 2 == 0 ):
            print(line)
            currLine1 = re.findall('\d+' , line)
            fileChanges = currLine1[0]
            fileInsertions = currLine1[1]
            if (len(currLine1) == 3):
                fileDeletions= currLine1[2]

            int_FileChanges = (int)(fileChanges)
            int_fileDeletions = (int)(fileDeletions)
            int_fileInsertions = (int)(fileInsertions)

            final_fileDeletions += int_fileDeletions
            final_fileInsertions += int_fileInsertions
            final_fileChanges += int_FileChanges




print("Total File changes = " , final_fileChanges)
print("Total file insertions = ", final_fileInsertions)
print("Total file deletions = " , final_fileDeletions)