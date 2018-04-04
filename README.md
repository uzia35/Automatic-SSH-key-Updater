# SysOpsSshExercise | Python version 2.7
Creates a simple process in Python that logs onto a remote machine using ssh (granted they already have a authorized key), 
gathers basic information, and changes the SSH Authorized Key file for each given ip in inputFile.

processing might take a while because of test Ips that cannot ssh,
it is however, instantaneous when actual Ips are given,
also the test servers that were used include my own virtual machine and rlogin.cs.vt.edu

to run this script: python SysOpsScript.py < inputTestFile

test cases: python -m unittest test_SysOpsScript < inputTestFile
