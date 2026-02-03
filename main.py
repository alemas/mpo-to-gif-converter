from PIL import Image, ImageFile, ImageSequence

filename = "HNI_0057.MPO"
image_file = Image.open(filename)

print(image_file.format, f"{image_file.size} {image_file.mode}")

images = ImageSequence.all_frames(image_file)

left_image = images[0]
right_image = images[1]

width = float(image_file.size[0])
crop_width = width * 0.885
height = float(image_file.size[1])

left_box = (width - crop_width, 0, width, height)
right_box = (0, 0, crop_width, height)

cropped_left_image = left_image.crop(right_box)
cropped_right_image = right_image.crop(left_box)

images = [cropped_left_image, cropped_right_image]

cropped_left_image.save("stereoscopic.gif", append_images=[cropped_right_image], loop=50, duration=97, disposal=2)

# jpg = Image.new(mode=left_image.mode, size=[int(crop_width), int(height*2)])
# jpg.paste(cropped_left_image)
# jpg.paste(cropped_right_image, (0, int(height)))
# jpg.save("stereoscopic.jpg")