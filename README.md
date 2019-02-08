# wp-test-demo-python
Project to demonstrate my automated testing skills in Python.

This suite of test cases runs Selenium-based test cases against a test Wordpress site. It's a port to Python of my project in the wp-test-demo-java-selenium repo.

## Prerequisites
As with the Java version of this project, I'm running these test cases against Docker containers that run a Wordpress test site, the MySQL database that powers it, and a Selenium grid. The Docker Compose yaml file I'm using to run these containers can be found in my misc-configs repo, along with an export of the test data I'm using for the Wordpress site.

The test data I'm using is a copy of one of my [live Wordpress sites](http://www.angelahighland.info), which has provided me the items to fill in for my WPTestLib helper class. (Which is, in turn, a port of the properties file from the Java version of this project.)

The main tool I'm using to run the suite is PyCharm, and the version of Python I'm working with is 3.7. I'm using Nosetests as the test runner, as that's what I used in my prior experience on my last day job, and PyCharm supports it.

Overall, I'm setting up this suite in Python similarly to how I wrote similar test suites on my previous day job.

## Skills and tech I'm demonstrating here
* Use of a helper class to set test-specific strings like ID numbers, titles, and names
* Using Nose functionality to run the test suite, and to annotate test methods
* Testing against a site running as a Docker container

## Why Nose?
I'm aware that the original version of Nose is in maintenance mode, and its docs do encourage people to use Nose2 instead. For the time being, though, I'm using Nose as that's what I'm most immediately familiar with. Time permitting, I'll be updating this suite to use Nose2.

## Reference links
* [Misc-configs repo](https://github.com/annathepiper/misc-configs) where I store my Docker Compose yml files
* [Java version of this project](https://github.com/annathepiper/wp-test-demo-java-selenium)
* [Nose](https://nose.readthedocs.io/en/latest/), the testing framework I'm using
* [PyCharm](https://www.jetbrains.com/pycharm/)
