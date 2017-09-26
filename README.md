<h1 class="gap">0x04. Loops, conditions and parsing</h1>



<h4 class="task">
    0. Create a SSH RSA key pair
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Read for this task:</p><ul>
<li><a href="http://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys">Linux and Mac OS users</a></li>
<li><a href="https://support.rackspace.com/how-to/generating-rsa-keys-with-ssh-puttygen/">Windows users</a></li>
</ul><p>man: <code>ssh-keygen</code></p><p>You will soon have to manage your own <a href="https://intranet.hbtn.io/concepts/17">servers</a> hosted on remote <a href="https://youtu.be/iuqXFC_qIvA?t=46">data centers</a>. We need to set them up with your RSA public key so that you can access them via SSH.</p><p>Create a RSA key pair.</p><p>Requirements:</p><ul>
<li>Share your <strong>public key</strong> in your answer file <code>0-RSA_public_key.pub</code></li>
<li>Fill the <em>SSH public key</em> field of your <a href="https://intranet.hbtn.io/users/my_profile">intranet profile</a> with your public key</li>
<li><strong>Keep the private key to yourself in a secure location</strong>, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects</li>
<li>If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase</li>
</ul><p>SSH and RSA keys will be covered in depth in a later project.</p>



<h4 class="task">
    1. For Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p><p>Requirement:</p><ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
</ul>



<h4 class="task">
    2. While Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p><p>Requirements:</p><ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>



<h4 class="task">
    3. Until Holberton School loop
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p><p>Requirements:</p><ul>
<li>You must use the <code>until</code> loop (<code>for</code> and <code>while</code> are forbidden)</li>
</ul>



<h4 class="task">
    4. If 9, say Hi!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays <code>Holberton School</code> 10 times, but for the 9th iteration, displays <code>Holberton School</code> <em>and then</em> <code>Hi</code> on a new line.</p><p>Requirements:</p><ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code> statement</li>
</ul>



<h4 class="task">
    5. 4 bad luck, 8 is your chance
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that loops from 1 to 10 and:</p><ul>
<li>displays <code>bad luck</code> for the 4th loop iteration</li>
<li>displays <code>good luck</code> for the 8th loop iteration</li>
<li>displays <code>Holberton School</code> for the other iterations</li>
</ul><p>Requirements:</p><ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code>, <code>elif</code> and <code>else</code> statements</li>
</ul>



<h4 class="task">
    6. Superstitious numbers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays numbers from 1 to 20 and:</p><ul>
<li>displays <code>bad luck from China</code> for the 4th loop iteration</li>
<li>displays <code>bad luck from Japan</code> for the 9th loop iteration</li>
<li>displays <code>bad luck from Italy</code> for the 17th loop iteration</li>
</ul><p>Requirements:</p><ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>case</code> statement</li>
</ul>



<h4 class="task">
    7. Clock
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p><ul>
<li>display hours from 0 to 12</li>
<li>display minutes from 1 to 59</li>
</ul><p>Requirements:</p><ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul><p>Note that in this example, we only display the first 70 lines using the <code>head</code> command.</p>



<h4 class="task">
    8. For ls
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays:</p><ul>
<li>The content of the current directory</li>
<li>In a list format</li>
<li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
</ul><p>Requirements:</p><ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
<li>Do not display hidden files</li>
</ul>



<h4 class="task">
    9. To file, or not to file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that gives you information about the <code>holbertonschool</code> file.</p><p>Requirements:</p><ul>
<li>You must use <code>if</code> and, <code>else</code> (<code>case</code> is forbidden)</li>
<li>Your Bash script should check if the file exists and print:

<ul>
<li>if the file exists: <code>holbertonschool file exists</code></li>
<li>if the file does not exist: <code>holbertonschool file does not exist</code></li>
</ul></li>
<li>If the file exists, print:

<ul>
<li>if the file is empty: <code>holbertonschool file is empty</code></li>
<li>if the file is no empty: <code>holbertonschool file is not empty</code></li>
<li>if the file is a regular file: <code>holbertonschool is a regular file</code></li>
<li>if the file is not a regular file: (nothing)</li>
</ul></li>
</ul>



<h4 class="task">
    10. FizzBuzz
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that displays numbers from 1 to 100.</p><p>Requirements:</p><ul>
<li>Displays <code>FizzBuzz</code> when the number is a multiple of 3 and 5</li>
<li>Displays <code>Fizz</code> when the number is multiple of 3</li>
<li>Displays <code>Buzz</code> when the number is a multiple of 5</li>
<li>Otherwise, displays the number</li>
<li>In a list format</li>
</ul>

