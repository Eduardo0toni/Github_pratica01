def segment_esferic():#25 Eduardo O.
    print("Càlcul de l'àrea i del volum d'un segment esfèric ")
    h = float(input("Alçada de la zona o segment esfèric = "))
    R = float(input("Radi de l'esfera = "))
    r_gran = float(input("Radi gran del segment = "))
    r_petit = float(input("Radi petit del segment = "))
    area = 2 * PI * R * h
    volum = 1/6 * PI * h * (pow(h,2) + 3 * pow(r_gran,2) + 3 * pow(r_petit,2))
    return area, volum
  