# CSS.py

A simple way of making CSS code in Python.

## Your CSS.py installation

### Installing CSS.py

```
pip install cssdotpy
```
### Updating CSS.py

```
pip install --upgrade cssdotpy
```

## Links

- [CODE OF CONDUCT](https://github.com/BLUEAMETHYST-Studios/CSS.py/blob/main/CODE_OF_CONDUCT.md)
- [CONTRIBUTORS](https://github.com/BLUEAMETHYST-Studios/CSS.py/blob/main/CONTRIBUTORS.md)
- [CONTRIBUTING POLICY](https://github.com/BLUEAMETHYST-Studios/CSS.py/blob/main/CONTRIBUTING.md)
- [SECURITY POLICY](https://github.com/BLUEAMETHYST-Studios/CSS.py/blob/main/SECURITY.md)

## Using it

### NOTICE: CSS.PY IS IN ALPHA DEVELOPMENT STAGES AND DOES NOT HAVE MANY FEATURES YET

### Creating a CSS instance

```py
import cssdotpy

MyCSS = cssdotpy.CSS()
```

### Adding HTML elements to the CSS and styling them

```py
import cssdotpy

MyCSS = cssdotpy.CSS()

MyCSS.addElement(element="p", style=["color:red", "font-family:roboto"])
```

### Adding HTML classes to the CSS and styling them

```py
import cssdotpy

MyCSS = cssdotpy.CSS()

MyCSS.addClass(name="MyClassName", style=["color:red", "font-family:roboto"])
```

### Adding Events to elements and/or classes and styling those

```py
import cssdotpy

MyCSS = cssdotpy.CSS()

MyCSS.addElement(element="p", style=["color:red", "font-family:roboto"])
MyCSS.addClass(name="MyClassName", style=["color:red", "font-family:roboto"])

MyCSS.addEventToElement(element="p", event="hover", style=["color:blue", "transform: scale(1.1)"])
MyCSS.addEventToClass(name="MyClassName", event="hover", style=["color:blue", "transform: scale(1.1)"])
```

### Getting your CSS

```py
import cssdotpy

MyCSS = cssdotpy.CSS()

MyCSS.addElement(element="p", style=["color:red", "font-family:roboto"])
MyCSS.addClass(name="MyClassName", style=["color:red", "font-family:roboto"])

MyCSS.addEventToElement(element="p", event="hover", style=["color:blue", "transform: scale(1.1)"])
MyCSS.addEventToClass(name="MyClassName", event="hover", style=["color:blue", "transform: scale(1.1)"])

# Print CSS
print(MyCSS.returnCSS())

# Output to file
open("output.css", "w").write(MyCSS.returnCSS())
```
