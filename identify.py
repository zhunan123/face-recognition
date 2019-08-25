import face_recognition
from PIL import Image, ImageDraw

image_of_aquaman = face_recognition.load_image_file('./img/known/aquaman.png')
aquaman_face_encoding = face_recognition.face_encodings(image_of_aquaman)[
    0]

image_of_adams = face_recognition.load_image_file('./img/known/adams.png')
adams_face_encoding = face_recognition.face_encodings(
    image_of_adams)[0]

# creating array of coding and names
known_face_encodings = [
    aquaman_face_encoding,
    adams_face_encoding
]

known_face_names = [
    "aquaman",
    "steven adams"
]

# load test image to find faces
test_image = face_recognition.load_image_file(
    './img/group/adams-aquaman.jpg')

# find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

#  convert to pil formet
pil_image = Image.fromarray(test_image)

# create imagedraw instance
draw = ImageDraw.Draw(pil_image)

# loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding)
    name = "Unknown Person"

    # if match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    # Draw Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),
                    (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5),
              name, fill=(255, 255, 255, 255))

del draw


# display image
pil_image.show()
