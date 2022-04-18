import pdf2image
import img2pdf
import os
import sys
import tempfile

def pagenumber_to_string(pagenumber):
    if pagenumber >= 0 and pagenumber <=9:
        return f"000{pagenumber}"
    elif pagenumber >= 10 and pagenumber <= 99:
        return f"00{pagenumber}"
    elif pagenumber >= 100 and pagenumber <= 999:
        return f"0{pagenumber}"
    elif pagenumber >= 1000 and pagenumber <= 9999:
        return str(pagenumber)

def crop_pdf(src_file, dest_file, cf_left, cf_right, cf_top, cf_bottom):

    with tempfile.TemporaryDirectory() as path:

        pdf_pages = pdf2image.convert_from_path(src_file, output_folder=path)
        
        image_names = []

        for i,page in enumerate(pdf_pages):

            w,h = page.size
           
            left_border = int(w * cf_left)
            right_border = int(w * (1 - cf_right))
            top_border = int(h * cf_top)
            bottom_border = int(h * (1 - cf_bottom))

            output_img = page.crop((left_border, top_border, right_border, bottom_border))

            file_name, file_extension = os.path.splitext(page.filename)
            output_img.save(f"{file_name}_{pagenumber_to_string(i)}{file_extension}")

            image_names.append(f"{file_name}_{pagenumber_to_string(i)}{file_extension}")


        with open(dest_file, "wb") as output_file:
            output_file.write(img2pdf.convert(image_names))


crop_pdf(sys.argv[1], 
        sys.argv[2], 
        float(sys.argv[3]), 
        float(sys.argv[4]), 
        float(sys.argv[5]), 
        float(sys.argv[6]))

