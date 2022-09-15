import pickle


def getKEYchar(a, KEY):
    # MAKE SURE YOU ARE IN KEY INDEX
    a = a % len(KEY)
    # CHECK FOR INT OR CHAR A DO AS PER THAT
    try:
        a = int(a)
        tmpVAR = int(KEY[a - 1]) * 1923
    except ValueError:
        tmpVAR = ord(KEY[a - 1]) * 125
    # RETURN INTEGRAL VALUE
    return tmpVAR



def getReminderPLUS(i, c):
    # IT USES SOME ALGO && CHECK CONDITION
    try:
        C = int(c) + 2
    except ValueError:
        C = ord(c) - 3
    if (C % i) == 0:
        return True
    else:
        return False



def encryptARRAY(array, KEY):
    # GET SOME VALUABLE VARIABLES
    encryptedARRAY = [[] for tmp in range(4)]
    totalContacts = len(array[0])
    for i in range(4):
        for j in range(totalContacts):
            encryptedARRAY[i].append([])
            # GET STRING LENGTH FOR LOOPING
            Slen = len(array[i][j])
            for k in range(Slen):
                # GET SPACE FOR STORING DENCRYPTED VALUES
                encryptedARRAY[i][j].append([])
                # ENCRYPTION RULES
                try:
                    tmpVAR3 = int(array[i][j][k])
                    if (i + j*2 - k) % 3 == 0:
                        tmpVAR04 = tmpVAR3 * getKEYchar(i + j - k, KEY) - 245 * (i + j + 7)
                    elif (i + j**2 - 7) % 2 == 0:
                        tmpVAR04 = tmpVAR3 * 2 - (i + 2*k) * j + getKEYchar(12, KEY)
                    else:
                        tmpVAR04 = tmpVAR3 ** 2 + i * getKEYchar(tmpVAR3, KEY) - (j + k) ** 2 + getKEYchar(i, KEY)
                    # SAVE TMPVAR04 IN ENCRYPTED ARRAY
                    encryptedARRAY[i][j][k] = chr(tmpVAR04)
                # FOR CHAR CHARACTERS
                except ValueError:
                    tmpVAR3 = ord(array[i][j][k])
                    if (i + j*2 - k) % 3 == 0:
                        tmpVAR04 = tmpVAR3 + 11 + getKEYchar(i + k, KEY) + (i + 5 - k)
                    else:
                        tmpVAR04 = tmpVAR3 + (i * j * k) * 54 - 32 * getKEYchar(i * k / (j + 1), KEY)
                    encryptedARRAY[i][j][k] = int(tmpVAR04)
    return encryptedARRAY



def decryptARRAY(array, KEY):
    # GET SOME VALUABLE VARIABLES
    decryptedARRAY = [[] for tmp in range(4)]
    totalContacts = len(array[0])
    # LOOP FOR ALL TYPES
    for i in range(4):
        for j in range(totalContacts):
            decryptedARRAY[i].append([])
            # GET STRING LENGTH TO MAKE LOOP
            Slen = len(array[i][j])
            for k in range(Slen):
                # GET SPACE FOR STORING DENCRYPTED VALUES
                decryptedARRAY[i][j].append(array[i][j][k])
                # ENCRYPTION RULES
                try:
                    tmpVAR3 = int(array[i][j][k])
                    if (i + j*2 - k) % 3 == 0:
                        tmpVAR04 = tmpVAR3 - (i + 5 - k) - 11 - getKEYchar(i + k, KEY)
                    else:
                        tmpVAR04 = tmpVAR3 - (i * j * k) * 54 + 32 * getKEYchar(i * k / (j + 1), KEY)
                    # PUT VALUE OF TMPVAR04 IN DECRYPTED BUT CHR() WON'T WORK ON BIG VALUES SO MAKE SURE
                    try:
                        decryptedARRAY[i][j][k] = chr(tmpVAR04)
                    except ValueError:
                        return 'ERRORx379'
                except ValueError:
                    tmpVAR3 = ord(array[i][j][k])
                    if (i + j*2 - k) % 3 == 0:
                        tmpVAR04 = int(tmpVAR3 + 245 * (i + j + 7)) / getKEYchar(i + j - k, KEY)
                    elif (i + j**2 - 7) % 2 == 0:
                        tmpVAR04 = (tmpVAR3 - getKEYchar(12, KEY) + (i + 2*k) * j) / 2
                    else:
                        tmpVAR04 = (tmpVAR3 - getKEYchar(i, KEY) + (j + k) ** 2 - i * getKEYchar(tmpVAR3, KEY)) ** 0.5
                    decryptedARRAY[i][j][k] = int(tmpVAR04)
    # CONVERT DECRYPTED ARRAY TO STRINGS WHERE IT NEEDS AND RETURN NEW ARRAY
    finalARRAY = [[] for i in range(4)]
    for i in range(4):
        for j in range(totalContacts):
            finalARRAY[i].append([])
            finalARRAY[i][j] = ''
            Slen = len(decryptedARRAY[i][j])
            for k in range(Slen):
                finalARRAY[i][j] += str(decryptedARRAY[i][j][k])
    return finalARRAY



def getArray(KEY):
    # GET ENCRYPTED ARRAY FROM STORAGE USING PICKLE
    infile = open('data/pickle-main', 'rb')
    # DEFINE ARRAY
    array = pickle.load(infile)
    infile.close()
    # CHECK IF THERE IS ANY ENCRYPTION
    if KEY == 'noENCRYPTION':
        return array
    # IF IT IS GO ON YOUR WORK
    else:
        return decryptARRAY(array, KEY)



def saveData(array, KEY):
    # CHECK ENCRYPTION STATUS
    if KEY == 'noENCRYPTION':
        encryptedARRAY = array
    else:
        encryptedARRAY = encryptARRAY(array, KEY)
    # SAVE ENCRYPTED ARRAY USING PICKLE
    outfile = open('data/pickle-main', 'wb')
    pickle.dump(encryptedARRAY, outfile)
    outfile.close()
