# show each of faces in the team2 individually
from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/group/team1.jpg')
face_locations = face_recognition.face_locations(image)

# loop through face locations
for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    # give us face image in a form of array and pass actually image using pillow lib
    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    # save each faces that we pulled
    pil_image.save(f'{top}.jpg')
