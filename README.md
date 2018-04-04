# SysOpsSshExercise | Python version 2.7
Creates a simple process in Python that logs onto a remote machine using ssh (granted they already have a authorized key), 
gathers basic information, and changes the SSH Authorized Key file for each given ip in inputFile.

processing might take a while because of test Ips that cannot ssh,
it is however, instantaneous when ips that can ssh are given,
also the test servers that were used include my own virtual machine and rlogin.cs.vt.edu

Possibly need to change permissions on authorized_key_exercise.pub to 400 or 600 before running this script,
as this was tested using real dummy keys

to run this script: python SysOpsScript.py < inputTestFile

to run test cases: python -m unittest test_SysOpsScript < inputTestFile
