import face_recognition

image_of_chris = face_recognition.load_image_file('./img/known/chriswu.jpg')
chriswu_face_encoding = face_recognition.face_encodings(image_of_chris)[0]
# give us a array of possible chriswu we want the first one

unknown_image = face_recognition.load_image_file(
    './img/unknown/习近平.jpeg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]


# compare faces

result = face_recognition.compare_faces(
    [chriswu_face_encoding], unknown_face_encoding)

if result[0]:
    print('This is chris wu')
else:
    print('This is NOT chriswu')
