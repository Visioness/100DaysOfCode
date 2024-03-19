from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageDraw, ImageTk, ImageOps


# Colors
LIGHT_BLUE = '#D4F1F4' 
DARK = '#4C5270'
GREEN = '#ECF87F'
RED = '#ED7377'
photo = None
photo_watermark = None
resized_photo = None
resized_photo_watermark = None

saved_label = None

# Upload image file
def upload_image():
    global photo, photo_watermark, resized_photo, resized_photo_watermark, save_button
    image_path = askopenfilename()

    if saved_label:
        saved_label.destroy()

    with Image.open(image_path).convert('RGBA') as im:
        # Original image size
        img_width, img_height = im.size

        # Resized Operations for GUI
        resized_im = im
        resized_im_width, resized_im_height = resized_im.size
        while resized_im_width > 800 or resized_im_height > 800:
            resized_im = im.resize(size=(int(img_width // 2), int(img_height // 2)))
            resized_im = ImageOps.exif_transpose(resized_im)
            resized_im_width, resized_im_height = resized_im.size
        
        resized_photo = ImageTk.PhotoImage(resized_im)
        canvas1 = Canvas(width=resized_im_width, height=resized_im_height, bg=LIGHT_BLUE, highlightthickness=0)
        canvas1.create_image(resized_im_width // 2, resized_im_height // 2, image=resized_photo)
        canvas1.grid(row=4, column=1)
        
        txt = Image.new('RGBA', resized_im.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt)
        draw_width = 0
        while draw_width < resized_im_width: 
            draw_height = 0
            while draw_height < resized_im_height:
                draw.text((draw_width, draw_height), '@Visioness', fill=(255, 255, 255, 100), font_size=25)
                draw_height += (resized_im_height // 4)
            draw_width += (resized_im_width // 4)
        
        out = Image.alpha_composite(resized_im, txt)

        resized_photo_watermark = ImageTk.PhotoImage(out)
        canvas2 = Canvas(width=resized_im_width, height=resized_im_height, bg=LIGHT_BLUE, highlightthickness=0)
        canvas2.create_image(resized_im_width // 2, resized_im_height // 2, image=resized_photo_watermark)
        canvas2.grid(row=4, column=3)


        # Original Size Operations   
        txt = Image.new('RGBA', im.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt)
        draw_width = 0
        while draw_width < img_width: 
            draw_height = 0
            while draw_height < img_height:
                draw.text((draw_width, draw_height), '@Visioness', fill=(255, 255, 255, 100), font_size=25)
                draw_height += (img_height // 5)
            draw_width += (img_width // 5)
        
        out_to_save = Image.alpha_composite(im, txt)

        save_button = Button(text='Save the watermarked image with original size!', font=('Arial', 15, 'italic'), fg=RED, bg=DARK, width=45, command=lambda: save_image(out_to_save, image_path))
        save_button.grid(row=6, column=1, columnspan=3, pady=10)


def save_image(im, image_path):
    global saved_label
    save_button.destroy()
    image_name = 'watermarked_' + image_path.split('/')[-1].split('.')[0] + '.png'
    im.save(f'/mnt/c/Users/VISIONESS/Downloads/{image_name}')
    saved_label = Label(text='Successfully saved the watermarked image in your downloads folder!', font=('Arial', 18, 'normal'), fg=DARK, bg=LIGHT_BLUE, width=75)
    saved_label.grid(row=7, column=1, columnspan=3, pady=20)

# UI Setup
window = Tk()
window.title('Watermarker')
window.geometry("+350+0")
window.config(padx=50, bg=LIGHT_BLUE)

label = Label(text='WATERMARKER', font=('Arial', 25, 'bold'), fg=DARK, bg=LIGHT_BLUE, width=25)
label.grid(row=1, column=1, columnspan=3, pady=20)

explanation_label = Label(text='- - Upload an image to add watermark to it - -', font=('Arial', 18, 'normal'), fg=DARK, bg=LIGHT_BLUE, width=75)
explanation_label.grid(row=3, column=1, columnspan=3)

button = Button(text='Upload an image!', font=('Arial', 15, 'italic'), fg=RED, bg=DARK, width=15, command=upload_image)
button.grid(row=5, column=1, columnspan=3, pady=10)

window.mainloop()