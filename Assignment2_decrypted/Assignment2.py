import math


def get_all_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors


def gcdExtended(a, b, x, y):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1  # To store results of recursive call
    gcd = gcdExtended(b % a, a, x1, y1)

    # Update x and y using results of recursive
    # call
    x = y1 - (b/a) * x1
    y = x1

    return gcd


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 1, 1, 1, 1

    #Can print out the whole table if we like 
    # print(["A", "B", "Q", "R", "X_1", "Y_1", "X_2", "Y_2"])
    # print([aa, bb, lastx, "", "", lastx, lasty, x, y])
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
        # print([x, y, lastx, quotient, remainder, lastx, lasty, x, y])
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def main():
    N_hint = None
    e_hint = None
    d_hint = None
    p = None
    q = None

    with open("a2-hint.pubkeys", 'r') as f:
        N_hint = int(f.readline())
        e_hint = int(f.readline())
        f.close()

    print('N_hint = %d' % N_hint)
    print('e_hint = %d' % e_hint)

    # we know that each digit of phi is a line of a2-hint.cipher therefore there are repetitions
    # we can calculate the list of encrypted digits, then match to them
    symbols = []

    for x in range(0, 255):
        y = pow(x, e_hint, N_hint)
        symbols.append(y)


    phi_digits = []
    with open("a2-hint.cipher", 'r') as f:
        for _, line in enumerate(f):
            phi_digits.append(chr(symbols.index(int(line.strip()))))
        # print("phi_digits: %s" % (str(phi_digits)))
        phi = int("".join(phi_digits))
        print("Phi = %d" % (phi))

        # obtain d
        e = 3
        _, d_hint, _ = extended_gcd(e, phi)
        # d_hint = gcdExtended(phi, e, 1, 1)
        d_hint = (d_hint % phi) - 1
        print("d = %d" % (d_hint))
        print("Check, ed = 1 mod phi: %s" % (str((e * d_hint) % phi == 1)))

        N = 510707667416675506846591343019303432700653056242930887117928539997020656791639003017255411250780739698296565125749038942170774338967617079867430662230497829653103504007801366984846426865656207589436329790174626213883277304396809950368056195415437126984638579414897339221304063888711683494564981380590793361552602956479857388082808865512991274927097219862165475507660724587615124456080340087038814721228620169983098820508474203945142967382165197736925900128206783126351332392771856423741055231868315596591313413591944233663461266936766809156285598360572628333387934113906614404663244151816574428782828643593240854414042027405461338038241892616497534345797641369725211660385921047231518072167175265163400701325904033531164175618253184413729441364012686951666986991641012876770420065171409537557521819965778502632925414538575903306370975947268130231052221179252113706390264106564263903684998345658879288583125009053651160403527617110590282419550392624550199558345609487966324132126354946902201269438946325241547608208509968279129537028873666986416229951380362455440844495737276040669981453524635579391109638571368424200358993493737352299097393465449472453681948299295869745181156529926927712550149894287398666973718887142110834793859093904036582038663798123131422367717816907185233925067807182465943051395187791088400232869279139671381400806136391444419047486859956426339827121220382677499193641903870981961846892139367870816487596926618723730754217185362993711226070122422456313788769130266635576784984350082437676346020339619632763372196558888688741694059124675090070783007928412924720759991367370341149108407296608227971115266206892904471315670567161595105018861136741710863549884090257572308284375339072196222483999197745717684916292890442293234898051693684568908722957607677938224962909898043674104144896501158768999119782483618644859687619186182155760255098066232965418450811174245227582990422154228051846834312202624891474782309046568965601852496978899352079754116314109505071132757616061870330338215497080871055334963044318745924174271351743774383251679815437765482383427510739913878897025497979503874059784016699439651300055475652551205365705766500078804367766092286264965023447707351338947112854713707521826835262718037961259743777018499897054602224719583787874854248939723377838894047803108809350869812898278234915016695004061592344287794797777821955165885441488997429723399644987113778086832693777087113997983327036566034635911095809004028885152282272020751

        plaintext = []
        with open("a2.cipher", 'r') as f: #Need to give full file path if on Windows
            for line_number, line in enumerate(f):
                print("a2.cipher line number: %d" % (line_number))
                line = int(line)
                x = pow(line, d_hint, N)
                bin_x = "0" + str(bin(x))[2:]

                for char in map(''.join, zip(*[iter(bin_x)]*8)):
                    num = int(char, 2)
                    plaintext.append(chr(num))

        for c in reversed(plaintext):
            print(c, end='')


if __name__ == "__main__":
    main()
