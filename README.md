# individual-project-SerbyRo

<h2>Project Description</h2>

<p>The Android Things Semaphore Countdown demonstrates how the mechanism of waiting at the traffic light works by the perspective of the pedestrians. The sample captures a button which is pressed by a user to change the color of the semaphore in green. After an amount of seconds, the semaphore turns back red. Everytime a pedestrian wants to cross the road , he has to press the button. The two colors are represented by two lights , one red and one green which act alternatively.</p>


<h2>Screenshots</h2>
<br><br>

<img src="media/Presentation.gif">

<h2>Schematics</h2>
<br><br>


<img src="media/rp2_pinout.png">
<p>I used pins number 23,24,27. 23 is for the switch, 27 for the green light and 24 for red light.</p>


<h2>R-requisites</h2>
<br>

<ul>
<li>
Android Things compatible board – Raspberry Pi model 3 B
</li>
<li>
The following individual components:

 - 2 coolers
 - 2 lights
 - 1 push button/switch
 - jumper wires
</li>
<li>PyCharm</li>
</ul>


<h2>Setup and Build</h2>

<p>To setup, follow these steps below.</p>

<ol>
<li>Ensure that the raspberry is plugged in</li>
<li>Connect the computer to the same network as the raspberry</li>
<li>Establish a connection between computer and Raspberry OS through putty</li>
<li>Transfer your files from your OS to raspberry(if you are using Windows you can use WinSCP)teams</li>
</ol>



<br>
<h2>Running</h2>

<p>In order to run the app you have to follow these steps:</p>

<ol>
<li>Connect the switch and 2 ligths to the raspberry through jump wires</li>

<li>Run the application with the following command sudo python “filename.py”</li>
<li>Press the button to see the result</li>
<li>
Enjoy :smirk:
</li>
</ol>









