BY NOOP LION===================0=====================
<p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>
<code>Rectangle</code>
<ul>
<li>You are not allowed to import any module</li>
</ul>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
&lt;class '0-rectangle.Rectangle'&gt;
{}
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
&lt;class '0-rectangle.Rectangle'&gt;
{}
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================1=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>0-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>0-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================2=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>1-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>1-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter is equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================3=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>2-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>2-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
--
##########
##########
##########
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
--
##########
##########
##########
&lt;3-rectangle.Rectangle object at 0x7f92a75a2eb8&gt;
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>Object address can be different</strong></p>
<strong>Object address can be different</strong>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================4=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>3-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>3-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: (see example below)

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> (see example below)</li>
<code>repr()</code>
<code>eval()</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================5=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>4-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>4-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<code>repr()</code>
<code>eval()</code>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<code>Rectangle</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================6=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>5-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>5-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<code>number_of_instances</code>
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul>
<li>Initialized to <code>0</code></li>
<code>0</code>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<code>repr()</code>
<code>eval()</code>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<code>Rectangle</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================7=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>6-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>6-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<code>number_of_instances</code>
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul>
<li>Initialized to <code>0</code></li>
<code>0</code>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<code>print_symbol</code>
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul>
<li>Initialized to <code>#</code></li>
<code>#</code>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<code>repr()</code>
<code>eval()</code>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<code>Rectangle</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&amp;"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&amp;"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
&amp;&amp;&amp;&amp;&amp;&amp;&amp;&amp;
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================8=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>7-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>7-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<code>number_of_instances</code>
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul>
<li>Initialized to <code>0</code></li>
<code>0</code>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<code>print_symbol</code>
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul>
<li>Initialized to <code>#</code></li>
<code>#</code>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<code>repr()</code>
<code>eval()</code>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<code>Rectangle</code>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<code>def bigger_or_equal(rect_1, rect_2):</code>
<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<code>rect_1</code>
<code>Rectangle</code>
<code>TypeError</code>
<code>rect_1 must be an instance of Rectangle</code>
<br/>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<code>rect_2</code>
<code>Rectangle</code>
<code>TypeError</code>
<code>rect_2 must be an instance of Rectangle</code>
<br/>
<li>Returns <code>rect_1</code> if both have the same area value</li>
<code>rect_1</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================9=====================
<p>Write a class <code>Rectangle</code> that defines a rectangle by: (based on <code>8-rectangle.py</code>)</p>
<code>Rectangle</code>
<code>8-rectangle.py</code>
<ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<li>You are not allowed to import any module</li>
</ul>
<li>Private instance attribute: <code>width</code>:

<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>width</code>
<ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def width(self):</code> to retrieve it</li>
<code>def width(self):</code>
<li>property setter <code>def width(self, value):</code> to set it:

<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul></li>
<code>def width(self, value):</code>
<ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
</ul>
<li><code>width</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>width must be an integer</code><br/></li>
<code>width</code>
<code>TypeError</code>
<code>width must be an integer</code>
<br/>
<li>if <code>width</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>width must be &gt;= 0</code></li>
<code>width</code>
<code>0</code>
<code>ValueError</code>
<code>width must be &gt;= 0</code>
<li>Private instance attribute: <code>height</code>:

<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul></li>
<code>height</code>
<ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
</ul>
<li>property <code>def height(self):</code> to retrieve it</li>
<code>def height(self):</code>
<li>property setter <code>def height(self, value):</code> to set it:

<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul></li>
<code>def height(self, value):</code>
<ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
</ul>
<li><code>height</code> must be an integer, otherwise raise a <code>TypeError</code> exception with the message <code>height must be an integer</code><br/></li>
<code>height</code>
<code>TypeError</code>
<code>height must be an integer</code>
<br/>
<li>if <code>height</code> is less than <code>0</code>, raise a <code>ValueError</code> exception with the message <code>height must be &gt;= 0</code></li>
<code>height</code>
<code>0</code>
<code>ValueError</code>
<code>height must be &gt;= 0</code>
<li>Public class attribute <code>number_of_instances</code>:

<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul></li>
<code>number_of_instances</code>
<ul>
<li>Initialized to <code>0</code></li>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
</ul>
<li>Initialized to <code>0</code></li>
<code>0</code>
<li>Incremented during each new instance instantiation</li>
<li>Decremented during each instance deletion</li>
<li>Public class attribute <code>print_symbol</code>:

<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul></li>
<code>print_symbol</code>
<ul>
<li>Initialized to <code>#</code></li>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
</ul>
<li>Initialized to <code>#</code></li>
<code>#</code>
<li>Used as symbol for string representation</li>
<li>Can be any type</li>
<li>Instantiation with optional <code>width</code> and <code>height</code>: <code>def __init__(self, width=0, height=0):</code></li>
<code>width</code>
<code>height</code>
<code>def __init__(self, width=0, height=0):</code>
<li>Public instance method: <code>def area(self):</code> that returns the rectangle area</li>
<code>def area(self):</code>
<li>Public instance method: <code>def perimeter(self):</code> that returns the rectangle perimeter:

<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul></li>
<code>def perimeter(self):</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to <code>0</code>, perimeter has to be equal to <code>0</code></li>
<code>width</code>
<code>height</code>
<code>0</code>
<code>0</code>
<li><code>print()</code> and <code>str()</code> should print the rectangle with the character <code>#</code>: 

<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul></li>
<code>print()</code>
<code>str()</code>
<code>#</code>
<ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
</ul>
<li>if <code>width</code> or <code>height</code> is equal to 0, return an empty string</li>
<code>width</code>
<code>height</code>
<li><code>repr()</code> should return a string representation of the rectangle to be able to recreate a new instance by using <code>eval()</code> </li>
<code>repr()</code>
<code>eval()</code>
<li>Print the message "Bye rectangle..." when an instance of <code>Rectangle</code> is deleted</li>
<code>Rectangle</code>
<li>Static method <code>def bigger_or_equal(rect_1, rect_2):</code> that returns the biggest rectangle based on the area

<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul></li>
<code>def bigger_or_equal(rect_1, rect_2):</code>
<ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<li>Returns <code>rect_1</code> if both have the same area value</li>
</ul>
<li><code>rect_1</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_1 must be an instance of Rectangle</code><br/></li>
<code>rect_1</code>
<code>Rectangle</code>
<code>TypeError</code>
<code>rect_1 must be an instance of Rectangle</code>
<br/>
<li><code>rect_2</code> must be an instance of <code>Rectangle</code>, otherwise raise a <code>TypeError</code> exception with the message <code>rect_2 must be an instance of Rectangle</code><br/></li>
<code>rect_2</code>
<code>Rectangle</code>
<code>TypeError</code>
<code>rect_2 must be an instance of Rectangle</code>
<br/>
<li>Returns <code>rect_1</code> if both have the same area value</li>
<code>rect_1</code>
<li>Class method <code>def square(cls, size=0):</code> that returns a new Rectangle instance with <code>width == height == size</code></li>
<code>def square(cls, size=0):</code>
<code>width == height == size</code>
<li>You are not allowed to import any module</li>
<pre><code>guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code></pre>
<code>guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 
</code>
<p><strong>No test cases needed</strong></p>
<strong>No test cases needed</strong>
===================10=====================
<p>Write a blog post describing how object and class attributes work.</p>
<ul>
<li>What's a class attribute</li>
<li>What's an instance attribute</li>
<li>What are all the way to create them and what is the Pythonic way of doing it</li>
<li>What are the differences between class and instance attributes</li>
<li>What are the advantages and drawbacks of each of them</li>
<li>How does Python deal with the object and class attributes using the <code>__dic__</code></li>
</ul>
<li>What's a class attribute</li>
<li>What's an instance attribute</li>
<li>What are all the way to create them and what is the Pythonic way of doing it</li>
<li>What are the differences between class and instance attributes</li>
<li>What are the advantages and drawbacks of each of them</li>
<li>How does Python deal with the object and class attributes using the <code>__dic__</code></li>
<code>__dic__</code>
<p>Your posts should have examples and at least one picture, at the top. 
Publish your blog post on Medium or LinkedIn, and share it at least on Twitter and LinkedIn.</p>
<p>When done, please add all urls below (blog post, tweet, etc.)</p>
<div class="blog_post_div">
<h4> Add URLs here:</h4>
<div class="form-group row">
<div class="col-sm-11">
<input class="form-control" id="input_1220" type="text" value=""/>
</div>
<div class="col-sm-1">
<button class="add_task_url" data-task-id="1220" data-task-requesting="0" data-user-id="149" type="button">
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
</button>
</div>
</div>
<ul class="list_1220">
</ul>
</div>
<h4> Add URLs here:</h4>
<div class="form-group row">
<div class="col-sm-11">
<input class="form-control" id="input_1220" type="text" value=""/>
</div>
<div class="col-sm-1">
<button class="add_task_url" data-task-id="1220" data-task-requesting="0" data-user-id="149" type="button">
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
</button>
</div>
</div>
<div class="col-sm-11">
<input class="form-control" id="input_1220" type="text" value=""/>
</div>
<input class="form-control" id="input_1220" type="text" value=""/>
<div class="col-sm-1">
<button class="add_task_url" data-task-id="1220" data-task-requesting="0" data-user-id="149" type="button">
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
</button>
</div>
<button class="add_task_url" data-task-id="1220" data-task-requesting="0" data-user-id="149" type="button">
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
</button>
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
<ul class="list_1220">
</ul>
<div data-position="99" data-role="task1209">
<div class=" clearfix gap" id="task-1209">
<span data-id="149" id="user_id"></span>
<div class="student_task_controls">
<!-- button Done -->
<button class="student_task_done btn btn-default no" data-task-id="1209">
<span class="no"><i class="fa fa-square-o"></i></span>
<span class="yes"><i class="fa fa-check-square-o"></i></span>
<span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
</button>
<br/>
<!-- button Help! -->
<button class="users_done_for_task btn btn-default btn-default" data-project-id="250" data-target="#task-1209-users-done-modal" data-task-id="1209" data-toggle="modal">
        Help
      </button>
<div class="modal fade users-done-modal" data-project-id="250" data-task-id="1209" id="task-1209-users-done-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
</div>
</div>
</div>
<h4 class="task">
    11. N queens
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4>
<!-- Progress vs Score -->
<!-- Task Body -->
<p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br></p>
<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>
<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
<p>Read: <a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>, <a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a></p>
<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>
<!-- Task URLs -->
<!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x08-python-more_classes</code></li>
<li>File: <code>101-nqueens.py</code></li>
</ul>
<div class="student_correction_requests">
<!-- Button test code -->
<button class="task_correction_modal btn btn-default " data-target="#task-test-correction-1209-correction-modal" data-task-id="1209" data-toggle="modal">
        Check your code?
      </button>
<div class="modal fade task_correction_modal" id="task-test-correction-1209-correction-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Correction of "N queens"</h4>
</div>
<div class="modal-body">
<div class="actions">
<center>
<input class="btn btn-primary correction_request_test_admin" data-task-id="1209" name="commit" type="submit" value="Start a new test"/>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
<div class="info"></div>
</center>
</div>
<div class="result"></div>
</div>
</div><!-- /.modal-content -->
</div><!-- /.modal-dialog -->
</div>
<!-- Button containers -->
</div>
</div>
</div>
<div class=" clearfix gap" id="task-1209">
<span data-id="149" id="user_id"></span>
<div class="student_task_controls">
<!-- button Done -->
<button class="student_task_done btn btn-default no" data-task-id="1209">
<span class="no"><i class="fa fa-square-o"></i></span>
<span class="yes"><i class="fa fa-check-square-o"></i></span>
<span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
</button>
<br/>
<!-- button Help! -->
<button class="users_done_for_task btn btn-default btn-default" data-project-id="250" data-target="#task-1209-users-done-modal" data-task-id="1209" data-toggle="modal">
        Help
      </button>
<div class="modal fade users-done-modal" data-project-id="250" data-task-id="1209" id="task-1209-users-done-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
</div>
</div>
</div>
<h4 class="task">
    11. N queens
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4>
<!-- Progress vs Score -->
<!-- Task Body -->
<p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br></p>
<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>
<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
<p>Read: <a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>, <a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a></p>
<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>
<!-- Task URLs -->
<!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
<li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
<li>Directory: <code>0x08-python-more_classes</code></li>
<li>File: <code>101-nqueens.py</code></li>
</ul>
<div class="student_correction_requests">
<!-- Button test code -->
<button class="task_correction_modal btn btn-default " data-target="#task-test-correction-1209-correction-modal" data-task-id="1209" data-toggle="modal">
        Check your code?
      </button>
<div class="modal fade task_correction_modal" id="task-test-correction-1209-correction-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Correction of "N queens"</h4>
</div>
<div class="modal-body">
<div class="actions">
<center>
<input class="btn btn-primary correction_request_test_admin" data-task-id="1209" name="commit" type="submit" value="Start a new test"/>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
<div class="info"></div>
</center>
</div>
<div class="result"></div>
</div>
</div><!-- /.modal-content -->
</div><!-- /.modal-dialog -->
</div>
<!-- Button containers -->
</div>
</div>
<span data-id="149" id="user_id"></span>
<div class="student_task_controls">
<!-- button Done -->
<button class="student_task_done btn btn-default no" data-task-id="1209">
<span class="no"><i class="fa fa-square-o"></i></span>
<span class="yes"><i class="fa fa-check-square-o"></i></span>
<span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
</button>
<br/>
<!-- button Help! -->
<button class="users_done_for_task btn btn-default btn-default" data-project-id="250" data-target="#task-1209-users-done-modal" data-task-id="1209" data-toggle="modal">
        Help
      </button>
<div class="modal fade users-done-modal" data-project-id="250" data-task-id="1209" id="task-1209-users-done-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
</div>
</div>
</div>
<button class="student_task_done btn btn-default no" data-task-id="1209">
<span class="no"><i class="fa fa-square-o"></i></span>
<span class="yes"><i class="fa fa-check-square-o"></i></span>
<span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
</button>
<span class="no"><i class="fa fa-square-o"></i></span>
<i class="fa fa-square-o"></i>
<span class="yes"><i class="fa fa-check-square-o"></i></span>
<i class="fa fa-check-square-o"></i>
<span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
<i class="fa fa-spinner fa-pulse"></i>
<span class="no pending">?</span>
<span class="yes">!</span>
<br/>
<button class="users_done_for_task btn btn-default btn-default" data-project-id="250" data-target="#task-1209-users-done-modal" data-task-id="1209" data-toggle="modal">
        Help
      </button>
<div class="modal fade users-done-modal" data-project-id="250" data-task-id="1209" id="task-1209-users-done-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
</div>
</div>
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
</div>
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
</div>
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Students who are done with "N queens"</h4>
</div>
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<span aria-hidden="true">×</span>
<h4 class="modal-title">Students who are done with "N queens"</h4>
<div class="modal-body">
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="error"></div>
</div>
<div class="list-group">
</div>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
<div class="error"></div>
<h4 class="task">
    11. N queens
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4>
<span class="alert alert-info mandatory-optional">
        #advanced
      </span>
<p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br></p>
<img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/>
<br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small>
<a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>
<br>
<br/></br>
<br/>
<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>
<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
<code>Usage: nqueens N</code>
<code>1</code>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<code>N must be a number</code>
<code>1</code>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
<code>4</code>
<code>N must be at least 4</code>
<code>1</code>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
<li>You are only allowed to import the <code>sys</code> module</li>
<code>sys</code>
<p>Read: <a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>, <a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a></p>
<a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>
<a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a>
<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>
<code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code>
===================11=====================
<p><img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/><br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br></p>
<img src="http://www.crestbook.com/files/Judit-photo1_602x433.jpg"/>
<br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small><br>
<br/></br></br>
<small>Chess grandmaster <a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>, the strongest female chess player of all time</small>
<a href="https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r">Judit Polgár</a>
<br>
<br/></br>
<br/>
<p>The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.</p>
<ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<li>You are only allowed to import the <code>sys</code> module</li>
</ul>
<li>Usage: <code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul></li>
<code>nqueens N</code>
<ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
</ul>
<li>If the user called the program with the wrong number of arguments, print <code>Usage: nqueens N</code>, followed by a new line, and exit with the status <code>1</code></li>
<code>Usage: nqueens N</code>
<code>1</code>
<li>where N must be an integer greater or equal to <code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul></li>
<code>4</code>
<ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
</ul>
<li>If N is not an integer, print <code>N must be a number</code>, followed by a new line, and exit with the status <code>1</code></li>
<code>N must be a number</code>
<code>1</code>
<li>If N is smaller than <code>4</code>, print <code>N must be at least 4</code>, followed by a new line, and exit with the status <code>1</code> </li>
<code>4</code>
<code>N must be at least 4</code>
<code>1</code>
<li>The program should print every possible solution to the problem

<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul></li>
<ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
</ul>
<li>One solution per line</li>
<li>Format: see example</li>
<li>You don't have to print the solutions in a specific order</li>
<li>You are only allowed to import the <code>sys</code> module</li>
<code>sys</code>
<p>Read: <a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>, <a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a></p>
<a href="https://en.wikipedia.org/wiki/Queen_(chess)">Queen</a>
<a href="https://en.wikipedia.org/wiki/Backtracking">Backtracking</a>
<pre><code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code></pre>
<code>julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
</code>
