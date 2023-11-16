from elastic import *
from gt_generate import *

img = plt.imread("/mnt/c/dl/frame_0.png")
rows, cols = img.shape[0], img.shape[1]

x_beg = int(rows / 2)
y_beg = -1

needle_angle = (np.random() - 0.5) * np.pi / 2
needle_length = np.random() * 60

x_end = x_beg + needle_length * np.sin(needle_angle)
y_end = y_end + needle_length * np.cos(needle_angle)

result = trajectory(img, x_beg, x_end, y_beg, y_end)
result2 = vector_field(img, x_beg, x_end, y_beg, y_end)

plt.figure()
plt.imshow(result)

plt.figure()
plt.imshow(result2)
plt.show()