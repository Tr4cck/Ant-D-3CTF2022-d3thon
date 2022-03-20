这道题目从设计到完成的整个过程比较匆忙，题目也本身有很多设计的不合理的地方，导致虚拟机内部信息泄露过于严重，大大降低了本题的难度，希望师傅们谅解。

The whole process from design to completion of this challenge is rather hurried, and the challenge itself has a lot of unreasonable design, resulting in too much information leakage inside the virtual machine, which greatly reduces the difficulty of this topic... Hope you all understand...

题目的核心部分是一个 *Python3.10.2* 编写的简易虚拟机，并进行了简单的变量名称混淆，最后使用 *Cython0.29.28* 编译出 so。由于没有对 so 的 import 做任何限制，并且 bcode.lbc 中的代码一定会被逐句解释，于是**一种可能的解法**就是将库 import 进去，逐条语句测试功能，可以非常快速地测出每一条语句的作用：

The core of the problem is a simple virtual machine written in *Python 3.10.2*, with simple variable name obfuscation, and finally a so compiled using *Cython 0.29.28*. Since there are no restrictions on the import of the so, and the code in bcode.lbc must be interpreted sentence by sentence, **one possible solution** is to import the library import in and test the function statement by statement, which can very quickly measure the effect of each statement:

当然一开始是想让各位师傅去对 so 文件做一点静态分析（测题的时候想到或许可以通过检测 python 解释器的进程从而实现简单的反调试，但是也来不及写了），整个代码比较冗长，但是仔细看看会发现大部分都是边界检查、版本信息检查、异常处理分支等等，而这部分对逆向分析的关系不太大：

Of course, at first I wanted you to do a little static analysis of the so file (during the test it occurred to me that I might be able to do some simple anti-debugging by detecting the python interpreter process, but it was too late to write it), and the code is rather long, but a closer look reveals that most of it is about bounds checking, version checking, exception handling branches, etc., which are less relevant to reverse analysis.

```cpp
if ( !v6 )
{
  v1113 = 0LL;
  v71 = 0LL;
  v10 = 0LL;
  v5 = 0LL;
  v1110 = 0LL;
  v72 = 0LL;
  v45 = 0LL;
  v39 = v1124;
  v1114 = 0LL;
  v46 = 0LL;
  v37 = 0LL;
  v32 = 0LL;
  v1112 = 0LL;
  v73 = 1627;
  v1108 = 0LL;
  v1100 = 0LL;
  v1078 = 0LL;
  v1105 = 0LL;
  v1115 = 0LL;
  v1116 = 0LL;
  v945 = 0LL;
  v1117 = 0LL;
  LODWORD(v1118) = 7;
  goto LABEL_311;
}
```

开始我们需要找到全局字符串表，从而定位到主要逻辑 `_pyx_pymod_exec_byte_analizer`：

To start we need to find the global string table so we can locate the main logic `_pyx_pymod_exec_byte_analizer`.

可以看出这里是 `import re`：

You can see here `import re`.

这里是 `Variables = {}` 等等：

Here is `Variables = {}` and so on.

后面步骤大致相同，会比较麻烦，多打一些注释，做一些重命名可以提高一丢丢效率 XD

The latter steps are more or less the same, it can be a bit tricky, typing more comments and doing some renaming can improve efficiency a little XD