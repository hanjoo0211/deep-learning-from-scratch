import numpy as np
from PIL import Image
from ch08.deep_convnet import DeepConvNet
from common.functions import softmax


img = Image.open("capture.png").convert("L")
img = np.array(img) / 255 # normalize 해줘야함..
img = img * -1 + 1 # 흑백반전도 해줘야함.. 검은배경에 흰 글자로 나오도록!
imgArray = img.reshape(1,28,28,1).transpose(0,3,1,2)

# 흑백반전 이미지 확인
# img = Image.fromarray(np.uint8(img * 255))
# img.show()

network = DeepConvNet()
network.load_params("./ch08/deep_convnet_params.pkl")

y = network.predict(imgArray)
y = softmax(y)
print(y)
print(np.argmax(y, axis=1))

# 테스트용!