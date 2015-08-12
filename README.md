# glskybox

A simple python tool for converting skysphere texture to skybox.

## Requirements

[PyOpenGL](http://pyopengl.sourceforge.net/) The Python OpenGL Binding

    pip install PyOpenGL

## Usage

    usage: glskybox.py [-h] [-o OUTPUT] [-s SIZE] [-f] FILE [FILE ...]
    
    Convert skydome texture to skybox
    
    positional arguments:
      FILE                  source file name
    
    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            destination path
      -s SIZE, --size SIZE  output image size
      -f, --overwrite       overwrite existing output

Example:

Use a photo taken by [PhotoSphere](https://maps.google.com/maps/about/contribute/photosphere/) app, then run:

`python glskybox.py your_sphere_photo.jpg`

Check out the result in output/ directory.

If you give a directory as input, it will traverse all files inside it and render them.