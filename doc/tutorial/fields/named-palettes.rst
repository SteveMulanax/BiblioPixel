Named Palettes
------------------

You can use a named Palette anywhere you need a palette.

There are twenty named Built-In Palettes that come with BiblioPixel (listed `here
<https://github.com/ManiacalLabs/BiblioPixel/blob/master/bibliopixel/util/colors/palettes.py#L34-L56>`_).

You can also define Project Palettes in the `palettes` section of a Project,
which is a named dictionary of palettes.


The Default Palette
=====================

There's a special palette in the Project Palettes named "default" which is used
for animations in that Project that don't specify a palette.  You can specify


**Example 1**: Project Palettes and Built-in Palettes

.. bp-code-block:: palettes

    shape: [48, 32]

    palettes:
       lovely: ['lavender blush 1', 'lemon chiffon 1', 'light coral']
       hideous: [yellow, beige, maroon]
       default: lovely
       g: van_gogh      # Refers to a Built-in Palette

    animation:
      typename: sequence
      length: 2
      animations:
        - typename: $bpa.matrix.MathFunc  # Use the default Palette

        - typename: $bpa.matrix.MathFunc
          palette: hideous  # Use a project Palette

        - typename: $bpa.matrix.MathFunc
          palette: flag     # Use a built-in Palette

        - typename: $bpa.matrix.MathFunc
          palette: g     # Use a built-in Palette

.. bp-code-block:: footer

   shape: [64, 48]
   animation:
     typename: $bpa.matrix.MathFunc
     func: 10
     palette:
       colors: flag
       scale: 0.01
