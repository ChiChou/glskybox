# glskybox

A simple python tool for converting skysphere texture to skybox.

## Requirements

[PyOpenGL](http://pyopengl.sourceforge.net/) The Python OpenGL Binding

    pip install PyOpenGL

## Usage

     usage: glskybox.py [-h] -i INPUT [-s SIZE] [-o OUTPUT] [-f OVERWRITE]
     
     Convert skydome texture to skybox
     
     optional arguments:
       -h, --help            show this help message and exit
       -i INPUT, --input INPUT
                             source file name
       -s SIZE, --size SIZE  output image size
       -o OUTPUT, --output OUTPUT
                             destination path
       -f OVERWRITE, --overwrite OVERWRITE
                             overwrite existing output

Example:

Use a photo taken by [PhotoSphere](https://maps.google.com/maps/about/contribute/photosphere/) app, then run:

`python glskybox.py --input=your_sphere_photo.jpg`

Check out the result in output/ directory.

If you give a directory as input, it will traverse all files inside it and render them.