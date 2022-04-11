# Challenge 3

![1](1.png)

Load the file to IDA, we can see it tries to write byte to memory and then execute it

![2](2.png)

![3](3.png)

It is better to dynamic analysis this binary

Load it to x32dbg, set bp before the call and then run

![4](4.png)

Step into that call, the program again unpack itself by xoring bytes at `19fd34 + 1c` with `0x66`

![5](5.png)

So the chall is about file unpacking itself

Keep tracing until we cant and see the flag in memory

![6](6.png)


`such.5h311010101@flare-on.com`
