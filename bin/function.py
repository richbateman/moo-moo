import string,random

#random generator


def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getfirstline(fileName):
    with open(fileName, 'r') as f:
        first_line = f.readline()
    return first_line


def filetoprocess(fileName):
    r = ''
    newline = getfirstline(fileName).strip('\n')
    headerRecord = str('[' + newline + '],')

    with open(fileName, 'r') as f:
        next(f)
        recordOpenBracket = str('[')
        for line in f:
            r += str('(' + line + '),')
        recordCloseBracket = str(']')
    f.close()

    convertedfile = 'job.upload(' + headerRecord + recordOpenBracket + r + recordCloseBracket + ')'

    return convertedfile