# kart_image_batch_tool
Decided to remake this because I needed it.

* Splits images in folder into rgb and alpha png and places them into rgb and alpha folder
* Merge images from rgb and alpha folder and places them in the merged folder.
* Allows sub-folder structure
* If image has no alpha channel, it just passes through into the rgb folder, and later into the merged folder.
* Auto grayscales alpha image on merge.
* Supports whatever image type you add to the extensions list @ line 26.     
    default: `extensions = ['png', 'tga', 'jpg', 'dds']`
    

Requires python, and pillow.

`pip install pillow`

Command Arguments:
* First argument is your folder.
* Second argument is your mode. split or merge.
* Third argument is optional, output image format.
 

Use:
* Place your image folder in kart_image_batch_tool.
* Open terminal in kart_image_batch_tool.
* `python run.py folder mode format`

Example:

Running `python run.py architecture split` will read files and folders from 'architecture' folder and create
'architecture_rgb' and 'architecture_alpha' folders and populate with the sub-folders if they exist, and the split
images respectively.
Now you can perform different operations. 

Later when you are finished with your edits, run `python run.py architecture merge tga`. This will merge the rgb and
alpha folders, and create 'architecture_merged', with the merged images having a TGA file-type.