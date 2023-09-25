# **MusicGroup**

## **Hyperiondev Software Engineering Bootcamp

### **Level 2, Task 23: Capstone Project - Django** 
### **Level 3, Task 10: Capstone Project I - Consolidation**

#### __*Table of Contents*__
1. Project Description
2. Installation
3. Usage
4. Credits/References 

#### __*1. Project Description*__
This project is a product of two seperate Hyperiondev capstone tasks. 

For the first task (level 2, task 23) we had to create a website for a made-up popband using django, html, CSS and Bootstrap. The website had to have at least three webpages and one database-driven component, as well as a user login and authentication system. The purpose of this task was to give us a space to combine all that we had learnt in level 2 (database handling, Django, html, CSS and bootstrap) to create a proper working website. I made a website for the fictional web-core Earth, Wind and Fire cover band, called Earth, Wind and Angelfire - shoutout to my friend Kali who came up with the concept for the band! My website has about ten pages. They are as follows:
* a homepage
* a login page
* a logout/farewell page
* a registration page
* a merchandise page
* a page displaying a list of blog posts
* a page that displays the details of an individual blog post
* a page displaying a list of polls for users to vote in
* a page displaying the details of the selected poll and a list of possible choices
* a page showing the results of a poll

My templates for these webpages are quite chaotic because I didnt create a single CSS file to call on when styling all of these pages - which I know is something I should have done to make the whole project look neater and the actual process of building it easier. The styling is also not the best, I wish that I had added more images to make it look prettier, and the design of the merchandise is also not my best work but I didnt want to waste too much time getting lost styling t-shirts and pins. 

Overall the website works, the only problem is that when a user is logged in, the logout button/link that is meant to sit on the header of the webpages doesnt appear on the homepage, merchpage and the various blog pages - you have to navigate to the polls webpage in order to log out.

For the second project (level 3, task 10) we were asked to add software documentation using Sphinx, a gitignore file, a requirements text file and a Dockerfile using Git. We had to create a local repository and copy our django project to it, and the add a gitignore.txt and requirements.txt to the root directory of the project. Then we had to create two branches and add documentation using Sphinx on one, and a Dockerfile on the other, and then merge them back together with the master branch. Finally we had to push our repository containing our project to GitHub and add a README.md file.

#### __*2. Installation*__
In order to install and work on this project locally you will need the following:

* Internet connection
* Python, you can download it [here](https://www.python.org/downloads/)
* Django, this has been included in the requirements.txt document
* A code editor, such as [Visual Studio Code](https://code.visualstudio.com/download)
* Bootstrap, find it [here](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
* Docker desktop, create a Docker account and download the app [here](https://www.docker.com/products/docker-desktop/)
* Git, get it [here](https://git-scm.com/downloads)
* sphinx, installation instructions [here](https://www.sphinx-doc.org/en/master/usage/installation.html#windows-other-method)
* sphinx-rtd-theme, installation instructions [here](https://pypi.org/project/sphinx-rtd-theme/)

You can pull down the app from Docker Hub, the image is bookah/musicgroup-app. Please ensure that the django secrect key is added to settings.py. To rebuild and run the image, enter the following commands into the command prompt:
* **docker build -t musicgroup-app** 

* **docker run -d -p 8000:8000 musicgroup-app**

Enter the following into your browser:
* **http://localhost:8000/musicgroup-app** 

#### __*3. Usage*__
This project was created in order to test my understanding of the django framework, html, CSS and Bootstrap. It is not meant to act as a real website or merchant page for a real band. 

The following images show what the website looks like when deployed:

![The home-page of the website](<Screenshot (25).png>)

![The blog section of the website](<Screenshot (26).png>)

![The polls section of the website](<Screenshot (27).png>)

![The login page](<Screenshot (28).png>)

![The registration page](<Screenshot (29).png>)

![The merchandise page](<Screenshot (30).png>)

![The merchandise page](<Screenshot (31).png>)

![The merchandise page](<Screenshot (32).png>)

![The logout page](<Screenshot (35).png>)

#### __*4. Credits/References*__
I had a lot of help from my mom throughout the creation of this project, she especially  helped me with the registration method in views.py, with my Dockerfile and with this README file. 

I also had a lot of help from a lot of websites for various features of the website. Some of these sites aren't directly credited in the code of this project because I didnt want to clutter up the code with comments, so I'll put all the links to these websites here, where they can be found in one place and not scattered throughout the project:

* here are the websites that helped me create and style the merchandise page of this website:
  
  * for the creatation of the t-shirts and buttons:
    * [customink.com](https://www.customink.com/) 

  * from frontendfreecode.com: 
    * [how to switch one image with another one](http://frontendfreecode.com/change-image-on-hover-with-bootstrap)

  * from getbootstrap.com:
    * [install bootsrap](https://getbootstrap.com/docs/3.4/getting-started/-->)
    * [text wrapping](https://getbootstrap.com/docs/5.0/utilities/text/-->)

  * from w3schhols.com
    * [image styling](https://www.w3schools.com/css/css3_images.asp)
    * [button styling](https://www.w3schools.com/css/css3_buttons.asp)

  * from stackoverflow.com for column alignment
    * [link 1](https://stackoverflow.com/questions/74779593/how-can-i-right-align-column-with-text-and-input)
    * [link 2](https://stackoverflow.com/questions/48482944/how-to-fit-an-image-inside-a-bootstrap-3)


* here are the websites that help me with the blog feature:

  * [djangocentral.com](https://djangocentral.com/building-a-blog-application-with-django/-->) 
  * [geeksforgeeks.org](https://www.geeksforgeeks.org/detailview-class-based-views-django/-->)
  * [reddit.com](https://www.reddit.com/r/django/comments/3fdeap/tuple_object_has_no_attribute_default_manager/) 
  * [scaler.com](https://www.scaler.com/topics/django/resetting-db-in-django/ -->)


* here are the websites that helped me with the poll feature:

  * [medium.com](https://medium.com/analytics-vidhya/building-a-simple-poll-system-in-django-part-i-a0bfb4fc3699)
  * [geeksforgeeks.org](https://www.geeksforgeeks.org/voting-system-project-using-django-framework/)  

* here are the websites that helped me with the authorisation system

  * [coderbook.com](https://coderbook.com/@marcus/how-to-restrict-access-with-django-permissions/)
  * [the django project forum](https://forum.djangoproject.com/t/logout-function/2710)
  * [ordinarycoders.com](https://ordinarycoders.com/blog/article/django-user-register-login-logout)
  * [stackoverflow.com](https://stackoverflow.com/questions/69099712/how-to-restrict-pages-in-django-if-login-requiredlogin-url-login-does-no) 

* here are the websites that helped me with the styling of my webpages:

  * font:
    * [source of font](https://www.1001fonts.com/pixel-fonts.html) 
    * [how to use custom font](https://www.wikihow.com/Upload-Your-Own-Fonts-to-HTML-Using-CSS)

  * images:
    * the cloud image used as the background image for all the webpages is one I took myself  
    * [pixelated guitar](https://pixabay.com/illustrations/pixel-mine-art-guitar-music-1562563/) 
    * [neon angel wings](https://unsplash.com/s/photos/angel)
     
  * navigation bar:
    * [how to align items to the right](https://www.geeksforgeeks.org/how-to-align-navbar-items-to-the-right-in-bootstrap-4/)
    * [how to make the nav bar transparent](https://mdbootstrap.com/how-to/bootstrap/navbar-transparent/)
    * [hubspot](https://blog.hubspot.com/website/bootstrap-navbar)
