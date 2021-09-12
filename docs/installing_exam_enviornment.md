# Installing the Exam Enviornment

Tensorflow has explicit requirements for the exam (https://www.tensorflow.org/extras/cert/Setting_Up_TF_Developer_Certificate_Exam.pdf), basically they are:
- Use python 3.8
- Use tensorflow 2.5 (along with a specific pandas, numpy and scipy version) 
- Don't use anaconda to set up your virtual enviornment
- Use pycharm as the IDE.

I will be setting up the enviorment on my local system (linux mint) using the CPU (though the GPU installation looks fun and I may give it a go later on). So lets begin setting up the exam enviornment! 

## Setting up the virtual enviornment

I will be using pythons venv module to create the virtual enviornmennt. As the exam wants python 3.8 I will set up a python venv in 3.8.

~~~
mkdir venv
python3.8 -m venv venv
~~~

To activate the enviornment:

~~~
source venv/bin/activate
~~~

I then decided I wanted to change the the name of the virtual enviornment. To do this I changed the  bin/activate file to the name I wanted rename the virtual enviornment to be called.  

~~~
if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ] ; then
    _OLD_VIRTUAL_PS1="${PS1:-}"
    if [ "x(venv) " != x ] ; then
        PS1="(venv) ${PS1:-}"
~~~

Tensorflow has specific module requirements for the exam:
- tensorflow==2.5.0
- tensorflow-datasets==4.3.0
- Pillow==8.2.0
- pandas==1.2.4
- numpy==1.19.5
- scipy==1.7.0

To make it easier with the installation I have put them all in the requirements.txt. Annoyingly in the installation an error occured as the latest version of absl-py doesn't work with the version of tensorflow-metadata which tensorflow 2.5 needs. Rolling absl-py back to 0.12 fixes it (this is included in the requirements.txt file). Also you need to install wheel before installing the requirements.txt file or else loads of error messages about 'bdist_wheel' appear.

~~~
pip install wheel
pip install -r requirements.txt
~~~

You should now be all set with tensorflow 2.5

## Download Pycharm

This works on ubuntu based systems and I am building from source.

First download pycharm community (https://www.jetbrains.com/pycharm/download/#section=linux). I am using the community version (becuase I am not paying!!)

Next unzip the .tar.gz 

~~~
tar -xzf pycharm-community-2021.2.1.tar.gz
~~~

Then change to the /bin directory and make pycharm.sh executable 

~~~
chmod +x pycharm.sh
~~~

And vola pycharm is working!!

~~~
sh pycharm.sh
~~~

As an added extra I added sh pycharm.sh to my .bashrc file as an alias so I can just type in pycharm to run.
