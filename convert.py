import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rgb_to_gray(image):
    if len(image.shape) == 3 and image.shape[2] in [3, 4]:
        # RGB 또는 RGBA 이미지인 경우
        if image.shape[2] == 4:
            # 알파 채널이 있는 경우 무시하고 RGB 값만 사용
            image = image[:, :, :3]
        # RGB 값을 평균하여 grayscale로 변환
        gray_image = np.mean(image, axis=-1)
    else:
        # 이미 grayscale 이미지인 경우 그대로 사용
        gray_image = image

    return gray_image

# 이미지 파일 읽기
image_path = '/mnt/c/Users/Sammy/Desktop/frame_0.png'  # 이미지 파일 경로 지정
img = mpimg.imread(image_path)

# RGB 또는 RGBA를 grayscale로 변환
gray_img = rgb_to_gray(img)

# grayscale 이미지 출력
plt.imshow(gray_img, cmap='gray')
plt.axis('off')

# 변환된 이미지를 파일로 저장
output_dir = '/mnt/c/Users/Sammy/Desktop'  # 저장할 디렉토리 경로 지정
os.makedirs(output_dir, exist_ok=True)

# 파일 이름 생성 (원본 파일 이름에 'gray_'를 추가)
output_filename = os.path.join(output_dir, 'gray_' + os.path.basename(image_path))

# 이미지를 파일로 저장
plt.savefig(output_filename, bbox_inches='tight', pad_inches=0)

# 저장한 이미지를 다시 불러와서 보여주기 (저장할 때 axis를 끄기 위해 저장한 이미지를 불러와서 출력)
saved_gray_img = mpimg.imread(output_filename)
plt.imshow(saved_gray_img, cmap='gray')
plt.axis('off')
plt.show()
