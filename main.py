import csv
import numpy as np


def hamdist_helper(str1, str2, prevMin=None):
    diffs = 0
    if len(str1) != len(str2):
        return max(len(str1), len(str2))
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
            if prevMin is not None and diffs > prevMin:
                return None
    return diffs


def hamdist(trans):
    dmin = len(trans[0])
    for i in range(len(trans)):
        for j in range(i + 1, len(trans)):
            dist = hamdist_helper(trans[i][:-1], trans[j][:-1], dmin)  # is dmin needed here?
            if dist is not None and dist < dmin:
                dmin = dist
    return dmin


def encode(H, r, n, m, i_v, k):
    # creating w
    w = [0] * (n - k) + m

    # our goal is to create z
    # find z={0,1}^(n-k) s.t. z∙H_I= S0-Wi0,S1-Wi1...,Sn-Wiu,S1-Wiu

    # first create x = S0-Wi0,S1-Wi1...,Sn-Wiu,S1-Wiu
    x = [0] * len(i_v[0])
    for i in range(len(i_v[0])):
        Si = i_v[1][i]
        j = i_v[0][i]
        Wij = w[j]
        x[i] = Si - Wij

    # we want to solve zHi = x
    # H isn't invertible so:
    # zH = x <=> zH*H^T = x*H^T
    # H*H^T is invertible so:
    # <=> zH * H ^ T = x * H ^ T  <=> z = x * H ^ T * (H * H ^ T)^-1
    idx = i_v[0]
    Hi = np.array(H)[:, idx]

    Htranspose = np.transpose(Hi)
    xt = np.transpose(x)
    k = np.linalg.lstsq(Htranspose, xt, None)[0]
    kint = np.array(np.around(np.array(k)), dtype=int)
    Z0 = np.transpose(kint)

    y = list(map((lambda x: x % 2), (w + np.dot(Z0, np.array(H)))))
    # should be y = m+np.dot(Z0,np.array(H)) but size is wrong
    return y


def decode(H, y, n, k):
    """
    We take z={y0,y1,...,yn-k-1} from the given y.
    Then we get: w=y-z*H, which is the w from the encoder.
    The message is: m = {xn-k,...,xn}.
    """
    z = y[:n - k]
    last = list(map((lambda x: x % 2), y - np.dot(z, H)))
    m = last[n - k:n]
    return m


def initialization():
    # getting parity check matrix
    p_c_m = []
    with open('Parity checking matrix.csv') as p_c_m_file:
        p_c_m_Reader = csv.reader(p_c_m_file)
        for row in p_c_m_Reader:
            int_row = list(map(int, row))
            p_c_m.append(int_row)

    # getting r - number of rows & n - number of columns
    r = len(p_c_m)
    n = len(p_c_m[0])
    k = n - r

    # getting minimum hamming distance
    mhd = hamdist(p_c_m)

    # getting information vector, index locations, stuck at values

    m=[]
    i_v = []  # index locations & stuck at values of those locations
    with open('Encoding input file.csv') as inputfile:
        inputReader = csv.reader(inputfile)
        m = list(map(int, next(inputReader)))
        i_v.append(list(map(int, list(filter(None, next(inputReader))))))
        i_v.append(list(map(int, list(filter(None, next(inputReader))))))

    y_vec = []
    while True:
        try:
            decode_encode = input("Would you like to decode or encode? (enter d or e, or exit)\n")
            if decode_encode == 'd':
                if y_vec==[]:
                    print('To decode a code word, you need to enter a message first.')
                else:
                    code_word = y_vec[len(y_vec)-1]
                    m = decode(p_c_m, code_word, n, k)
                    print("The message that was received is: ",m)

            elif decode_encode == 'e':
                print('Encoding the following message: ', m)
                y = encode(p_c_m, r, n, m, i_v, k)
                y_vec.append(y)
                print('The code word for the above message: ',y)


            elif decode_encode == 'exit':
                print('Goodbye')
                break
            else:
                print("Invalid input entered")
        except Exception as e:
            print(e)


def main():
    initialization()


if __name__ == "__main__":
    main()
