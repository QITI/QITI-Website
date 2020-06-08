def cut_circle():
    image = gimp.image_list()[-1]
    filename = pdb.gimp_image_get_filename(image)
    filename = filename.split(".")[0] + "-bubble.png"
    copy_image = pdb.gimp_edit_copy_visible(image)
    bubble = pdb.gimp_edit_paste_as_new_image(copy_image)
    pdb.file_png_save_defaults(bubble, bubble.layers[0], filename, filename)
    print(filename)
