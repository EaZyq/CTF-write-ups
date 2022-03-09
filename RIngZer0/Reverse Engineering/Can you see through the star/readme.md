# Can you see through the star

### First sight

![2.png](2.png)

![1.png](1.png)


A .net binary, load it in dnspy and read the code

### Solve it

![3.png](3.png)


Here we can see all the strings for the GUI above

Scroll down a little bit we got this


![4.png](4.png)


Function `button1_Click` is the func that we need

`this.maskedTextBox1.Name` = `maskedTextBox1`

`this.button1.Name`        = `button1`


So the flag is `FLAG-maskedTextBox1vcbutton1`





