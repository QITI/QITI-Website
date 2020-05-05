images = gimp.image_list()
radius = 120
for image in images:
    try:
        path_name = pdb.gimp_path_get_current(image)
        filename = pdb.gimp_image_get_filename(image)
        filename = filename.split(".")[0] + "-bubble.png"
        circle_origin = pdb.gimp_path_get_points(image, path_name)[3][0:2]
        pdb.gimp_image_select_ellipse(image, 0, circle_origin[0]-radius/2, circle_origin[1]-radius/2, radius, radius)
        copy_image = pdb.gimp_edit_copy_visible(image)
        bubble = pdb.gimp_edit_paste_as_new_image(copy_image)
        pdb.file_png_save_defaults(bubble, bubble.layers[0], filename, filename)
        display = pdb.gimp_display_new(bubble)
    except:
        print("err")
