from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':

    # 参数配置
    width, height = 60, 40
    background_color = (255, 59, 48)  # 白底
    border_color = (255, 59, 48)  # 钉钉红
    text_color = (255, 255, 255)  # 文字红
    border_width = 2
    corner_radius = 20

    # 创建画布
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 绘制带边框的圆角矩形
    draw.rounded_rectangle(
        [(border_width, border_width),
         (width - border_width, height - border_width)],
        radius=corner_radius,
        fill=background_color,
        outline=border_color,
        width=border_width
    )

    # 添加文字（需提前下载阿里普惠体）
    try:
        font = ImageFont.truetype('AlibabaPuHuiTi-Heavy.ttf', 20)
    except:
        font = ImageFont.truetype('DIN Alternate Bold.ttf', 18)  # 备用粗体

    text = "99+"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 居中定位（考虑椭圆形留白）
    x = (width - text_width) // 2 - 2
    y = (height - text_height) // 2 - 4

    draw.text((x, y), text, fill=text_color, font=font)

    img.save('dingtalk_unread.png')