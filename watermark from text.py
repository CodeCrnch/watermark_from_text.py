from PIL import Image, ImageDraw, ImageFont

image = Image.open("pic.jpg")

text = "martin_py"
font = ImageFont.truetype("arial.ttf", 36)

draw = ImageDraw.Draw(image)
textwidth, textheight = draw.textsize(text, font)
x = image.width - textwidth - 10
y = image.height - textheight - 10
draw.text((x, y), text, font=font, fill=(0,0,255))

image.save("markedpic.jpg")
