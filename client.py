import numpy as np
import cv2

# Yüz
face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')  # Eklendi
eye_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_eye_tree_eyeglasses.xml')  # Eklendi
lefteye_2splits_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_lefteye_2splits.xml')  # Eklendi
righteye_2splits_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_righteye_2splits.xml')  # Eklendi
profileface_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_profileface.xml')  # Eklendi
smile_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_smile.xml')  # Eklendi

frontalface_alt_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')  # Eklendi
frontalface_alt_tree_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt_tree.xml')  # Eklendi
frontalface_alt2_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt2.xml')  # Eklendi

# Vücut
upper_body = cv2.CascadeClassifier('haarcascades\haarcascade_upperbody.xml')  # Eklendi
lower_body = cv2.CascadeClassifier('haarcascades\haarcascade_lowerbody.xml')  # Eklendi
full_body = cv2.CascadeClassifier('haarcascades\haarcascade_fullbody.xml')  # Eklendi

# Kedi
frontalcat_face = cv2.CascadeClassifier('haarcascades\haarcascade_frontalcatface.xml')  # Eklendi
frontalcatface_extended_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalcatface_extended.xml')  # Eklendi

# Lisan
licence_plate_rus_16stages_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_licence_plate_rus_16stages.xml')
russian_plate_number_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

# Tennis Topu
tennis_topu = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## Tennis Topu
    balls = tennis_topu.detectMultiScale(img, 11, 11)
    for (x, y, w, h) in balls:
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img, 'Tenis Topu', (x - 5, y - 5), font, 0.5, (102, 51, 0), 2, cv2.LINE_AA)
        cv2.rectangle(img, (x, y), (x + w, y + h), (102, 51, 0), 2)

    # Yüz Kısımları

    # Yüz
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  #MAVI
    #     # Gözler
    #     roi_gray = gray[y:y + h, x:x + w]
    #     roi_color = img[y:y + h, x:x + w]
    #     eyes = eye_cascade.detectMultiScale(roi_gray)
    #     for (ex, ey, ew, eh) in eyes:
    #         cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)  # SARI
    #         # Sol Göz
    #         lefteye_2splits_gray = gray[y:y + h, x:x + w]
    #         lefteye_2splits_color = img[y:y + h, x:x + w]
    #         lefteye_2splits = lefteye_2splits_cascade.detectMultiScale(lefteye_2splits_gray)
    #         for (lex, ley, lew, leh) in lefteye_2splits:
    #             cv2.rectangle(lefteye_2splits_color, (lex, ley), (lex + lew, ley + leh), (127, 255, 212), 2)  # Aquamarine
    #             # Sağ Göz
    #             righteye_2splits_gray = gray[y:y + h, x:x + w]
    #             righteye_2splits_color = img[y:y + h, x:x + w]
    #             righteye_2splits = righteye_2splits_cascade.detectMultiScale(lefteye_2splits_gray)
    #             for (rex, rey, rew, reh) in righteye_2splits:
    #                 cv2.rectangle(lefteye_2splits_color, (rex, rey), (rex + rew, rey + reh), (69, 139, 116), 2)  # Aquamarine3

    #    #Gülümseme
    #    smile = smile_cascade.detectMultiScale(gray,5,5)
    #    for(sx,sy,sw,sh) in smile:
    #        cv2.rectangle(img, (sx,sy), (sx+sw, sy+sh), (0,0,0), 2) # Siyah

    #    #Profil Yüz
    #    profileface = profileface_cascade.detectMultiScale(gray,1.3,5)
    #    for(pfx,pfy,pfw,pfh) in profileface:
    #        cv2.rectangle(img, (pfx,pfy), (pfx+pfw, pfy+pfh), (210,105,30), 2) # Chocolate
    #
    #
    #    #frontalface_alt_cascade
    #    frontalface_alt = frontalface_alt_cascade.detectMultiScale(gray,1.3,5)
    #    for(ffx,ffy,ffw,ffh) in frontalface_alt:
    #        cv2.rectangle(img, (ffx,ffy), (ffx+ffw, ffy+ffh), (184,134,11), 2) # DarkGoldenrod
    #
    #    #frontalface_alt_tree_cascade
    #    frontalface_alt_tree = frontalface_alt_tree_cascade.detectMultiScale(gray,1.3,5)
    #    for(ffax,ffay,ffaw,ffah) in frontalface_alt_tree:
    #        cv2.rectangle(img, (ffax,ffay), (ffax+ffaw, ffay+ffah), (238,173,14), 2) # DarkGoldenrod2
    #
    #    #frontalface_alt2_cascade
    #    frontalface_alt2 = frontalface_alt2_cascade.detectMultiScale(gray,1.3,5)
    #    for(pf2x,pf2y,pf2w,pf2h) in frontalface_alt2:
    #        cv2.rectangle(img, (pf2x,pf2y), (pf2x+pf2w, pf2y+pf2h), (139,101,8), 2) # DarkGoldenrod4

    # Vücut Kısımları

    # Turuncu Üst Vücut
    # upperbody = upper_body.detectMultiScale(gray, 1.3, 5)
    # for (ubx, uby, ubw, ubh) in upperbody:
    #     cv2.rectangle(img, (ubx, uby), (ubx + ubw, uby + ubh), (255, 69, 0), 2)

    # Yeşil Alt Vücut
    # lowerbody = lower_body.detectMultiScale(gray, 1.3, 5)
    # for (lbx, lby, lbw, lbh) in lowerbody:
    #     cv2.rectangle(img, (lbx, lby), (lbx + lbw, lby + lbh), (0, 255, 0), 2)

    # Mor Tüm Vücut
    # fullbody = full_body.detectMultiScale(gray, 1.3, 5)
    # for (fbx, fby, fbw, fbh) in fullbody:
    #     cv2.rectangle(img, (fbx, fby), (fbx + fbw, fby + fbh), (138, 43, 226), 2)

    # Renk Kedi Yüzü
    # frontalcatface = frontalcat_face.detectMultiScale(gray, 1.3, 5)
    # for (fcx, fcy, fcw, fch) in frontalcatface:
    #     cv2.rectangle(img, (fcx, fcy), (fcx + fcw, fcy + fch), (85, 26, 139), 2)

    # Mor Alternatif Kedi Yüzü
    # frontalcatface = frontalcatface_extended_cascade.detectMultiScale(gray, 1.3, 5)
    # for (facx, facy, facw, fach) in frontalcatface:
    #     cv2.rectangle(img, (facx, facy), (facx + facw, facy + fach), (238, 169, 184), 2)

    cv2.imshow('Kamera', img)
    k = cv2.waitKey(30) & 0xff
    if ((k == 27) or (k == 13) or (k == 32)):
        break

cap.release()
cv2.destroyAllWindows()
