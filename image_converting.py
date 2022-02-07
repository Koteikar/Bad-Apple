import cv2


def calc_symbol(num_of_white: int, num_of_pixels: int) -> int:
    for i in range(10):
        if (i + 1) * (num_of_pixels / 10) >= num_of_white:
            return i


def get_list(path: str, columns: int, rows: int) -> str:
    brightness_tuple = (' ', '*', '#', 'M', 'W', '8', '$', '&', '%', '@')
    image = cv2.imread(path, 0)
    (thresh, image) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # code below is used for splitting image into small pieces,
    # and then for replacing those pieces with determined ASCII symbol
    height, width = image.shape
    block_height = height // rows
    block_width = width // columns
    out = ''
    for i in range(rows):
        temp_out = ''
        for j in range(columns):
            crop_img = image[i * block_height:i * block_height + block_height, j * block_width:j * block_width + block_width]
            count_non_zero = cv2.countNonZero(crop_img)

            temp_out += (brightness_tuple[calc_symbol(count_non_zero, block_height * block_width)])
        out += ''.join(temp_out)
    return out
