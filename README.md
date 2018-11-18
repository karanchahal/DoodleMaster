# Doodle Master

The Doodle Master seeks to turn your UI mockups into real code. Currently this repository just serves to demonstrate a Proof Of Concept of Artificially Intelligent Design Tools. 

The demo supports the detection of 4 classes of UI components

1. TextViews
2. Headers
3. ImageViews
4. Buttons

This type of tool can be useful in a big organisation which adheres to a consistent design guide and has several reusable components on variety of platforms such as mobile and the web. For example a button on the Airbnb websote follows the same styling accross all platforms. This tool can simultaneously generate the same UI for Android and the Web.

## Demo

![alt text](/assets/new.gif)

## Technologies 

This demo uses a simple CNN for the classification of the doodles made. The software is able to localise the UI element through a combintion of geometric techniques and simple mouse/ finger position detction. Frameworks used are:

1. PyTorch - Deep Learning Model
2. React- UI 


This demo was inspired by AIrbnb's work on SKetching INterfaces. This demo was made while I was a frontend developer. I was inspored to make this as I saw a lot of developers spending time on coding the UI from the mockups, this time could be better spent in coding the functionality behing the UI. Doodle master  seeks to build a painless and natural way of prototyping interfaces. This tool can be used by designers and developers alike to showcase ideas quickly in the form of real code.


##### Note

This is not a prodution worthy piece of software,it is only meant for demo purposes. Please don't hesistate to contact me for more details on this project.