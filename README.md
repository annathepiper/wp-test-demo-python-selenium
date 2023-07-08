# Wordpress Test Demo With Python and Selenium

Project to demonstrate my automated testing skills in Python.

This suite of test cases runs Selenium-based test cases against a test Wordpress site. It's a port to Python of my project in the wp-test-demo-java-selenium repo.

## Prerequisites

As with the Java version of this project, I'm running these test cases against Docker containers that run a Wordpress test site, the MySQL database that powers it, and a Selenium grid. The Docker Compose yaml file I'm using to run these containers can be found in my misc-configs repo, along with an export of the test data I'm using for the Wordpress site.

The test data I'm using is a copy of one of my [live Wordpress sites](http://www.angelahighland.info), which has provided me the items to fill in for my WPTestLib helper class. (Which is, in turn, a port of the properties file from the Java version of this project.)

The main tool I'm using to run the suite is PyCharm, and the version of Python I'm working with is 3.10. I'm using Pytest as the test runner.

Overall, I'm setting up this suite in Python similarly to how I wrote similar test suites on my previous day job.

## Skills and tech I'm demonstrating here

* Use of a helper class to set test-specific strings like ID numbers, titles, and names
* Using Pytest and the Testdox plugin to run the test suite, and to annotate test methods
* Use of the @property decorator for a method
* Selenium webdriver click events in the Menu and Submenu test cases
* Use of action chains to do hover events over specific elements in the Submenu test cases
* Use of support classes to dictate page layout so I can shorten actual test cases
* Testing against a site running as a Docker container

## Pytest and Testdox

Earlier versions of this code used the Nose test runner. But Nose was old even in 2019, and so in the 2023 updates to this suite, I've done a bunch of changes to make the tests run in pytest instead. That was the test runner recommended to me when I put out a call for input on social media.

I'm using a plugin for pytest called [Testdox](https://pypi.org/project/pytest-testdox/), which does some formatting I like to the output and makes it a bit easier for me to read.

## Current testing status

This code has been successfully most recently run against PyCharm Community Edition 2023.1.3, on both Windows 10 and Ubuntu Linux 22.04.

## Reference links
* [Misc-configs repo](https://github.com/annathepiper/misc-configs) where I store my Docker Compose yml files
* [Java version of this project](https://github.com/annathepiper/wp-test-demo-java-selenium)
* [Nose](https://nose.readthedocs.io/en/latest/), the testing framework I'm using
* [PyCharm](https://www.jetbrains.com/pycharm/)
