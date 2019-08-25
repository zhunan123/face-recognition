import face_recognition

image = face_recognition.load_image_file('./img/group/team2.jpg')
face_locations = face_recognition.face_locations(image)

# print(face_locations)
print(f'there are {len(face_locations)} people in the image')
