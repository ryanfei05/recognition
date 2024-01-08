import face_recognition

ryan = face_recognition.load_image_file('./images/known/ryan.jpg')
face_locations = face_recognition.face_locations(ryan)

face_landmarks_list = face_recognition.face_landmarks(ryan)



known_ryan = face_recognition.load_image_file('./images/known/ryan.jpg')
unknown_image = face_recognition.load_image_file('./images/unknown/Bill Gates.jpg')
unknown_image2 = face_recognition.load_image_file('./images/unknown/unknown.jpg')
unknown_image3 = face_recognition.load_image_file('./images/unknown/ryan_pic.jpg')

ryan_encoding = face_recognition.face_encodings(known_ryan)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
unknown_encoding2 = face_recognition.face_encodings(unknown_image2)[0]
unknown_encoding3 = face_recognition.face_encodings(unknown_image3)[0]

result = face_recognition.compare_faces([ryan_encoding], unknown_encoding)[0]
result2 = face_recognition.compare_faces([ryan_encoding], unknown_encoding2)[0]
result3 = face_recognition.compare_faces([ryan_encoding], unknown_encoding3)[0]

results = []
results.append(result)
results.append(result2)
results.append(result3)

for result in results:
    if result:
        print('This is Ryan')
    else:
        print('This is not Ryan')

