

col = Image.open("/home/ceinfo/PycharmProjects/pythonProject6/archive1/images/train/disgust/299.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("result_bw.png")