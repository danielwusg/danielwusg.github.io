from PIL import Image

def resize_image_to_width(image_path, target_width, save_path):
    # 打开图片
    with Image.open(image_path) as img:
        # 计算新的高度，保持宽高比
        w_percent = (target_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))

        # 调整图片大小
        img_resized = img.resize((target_width, h_size), Image.Resampling.LANCZOS)

        # 展示图片，或者可以选择保存
        img_resized.save(save_path)

# 使用函数，输入图片路径和目标宽度
resize_image_to_width('images/nju-logo.svg', 360, 'images/nju-logo-360.svg')
