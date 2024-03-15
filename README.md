Deploying your Python application to Android

Since many years Android has held the top position as the most used OS with about 38% of the OS user share in 2023. Currently 3 major languages – C++, Java, Kotlin are used for application development on Android. Although Python has the capabilities of enabling Android deployment, Python was never considered as an adequate language for Android development. But, with the introduction of “PEP 738: Adding Android as a supported platform”, and the increasing popularity of frameworks like PySide6, Kivy, and Beeware which enable GUI development with Python for Android devices, it is time for Python package developers to consider Android as a potential platform.

This talk gives an introduction to each of the GUI development toolkits – Kivy, Beeware (Toga) and PySide6 by demonstrating how to create a simple Contact List application. We later delve into the pros and cons of each of these frameworks, so that Python application developers can decide which framework suits their requirements better.

Python can be used to create native applications for Android. However, although Python is the most popular programming language, it is not the first choice to create an Android application. This talk gives an overview of developing Android application with Python by comparing the 3 most popular frameworks for GUI development with Python that support Android as a platform – PySide6, Kivy and Beeware. This comparison is demonstrated with a simple Contact List application with the ability to add, edit and delete contacts.

The overall structure of the talk will be almost the following:

Why is Android a relevant platform for Python application developers? (6 minutes)
In this section, we establish why Android is the most popular OS being sued currently. Although Python has had the support to run applications natively in Android, even dating back to 2011, the development of Android applications with Python is not so popular. We will further highlight one of the major concerns of using Python for Android develpoment and how PEP 738 can help simplify this.

Current status of Android app development with Python (2 minutes)
In this section, we give a brief introduction to some of the Python based toolkits that support Android as a platform – Kivy, Beeware and PySide6.

Contact List application with Kivy (3 minutes)
In this section, we look at how the overall Python code for the contact list application looks like using Kivy and the steps to create the final distributable (.apk).

Contact List application with PySide6 (5 minutes)
The deployment of PySide6 application to Android uses the same build tool as Kivy, called python-for-android. python-for-android now also supports a Qt backend along with SDL2 that Kivy uses thus enabling the deployment of PySide6 application. In this section, we look at how the overall Python code for the contact list application looks like using PySide6 and the steps to create the final distributable (.apk).

Contact List application with Toga (3 minutes)
In this section, we look at how the overall Python code for the contact list application looks like using Beeware’s toga and the steps to create the final distributable (.apk).

Pros and Cons of each framework (6 minutes)
Since the exact same application was created using each of the 3 frameworks, we do a comparison by looking at the pros and cons of each framework.

Conclusion and Questions (5 minutes)
Questions from the audience.