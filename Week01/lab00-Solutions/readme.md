# Introdution

This lab explains how to use your own computer to complete assignments for CS 61A and introduces some of the basics of Python.
本实验介绍了如何使用自己的计算机完成 CS 61A 的作业，并介绍了 Python 的一些基础知识。

# Set up

* Install a terminal - Windows 子系统模拟 Ubuntu

* Install Python3 - 3.12

* Install a text editor - VS code

# Using terminal

* home directory - prompt 提示符 `~ $`

![image-20241022194959187](C:\Users\22044\AppData\Roaming\Typora\typora-user-images\image-20241022194959187.png)

* display the full path - 主目录 - `echo "$HOME"`

![image-20241022200147709](C:\Users\22044\AppData\Roaming\Typora\typora-user-images\image-20241022200147709.png)

* path

	   **c**ommand **l**ine **i**nterface or CLI - 命令行界面
	
	   **g**raphics **u**ser **i**nterface or GUI - 图形用户界面

# Organizing files

* `ls` - **l**i**s**ts all the files and folders in the current directory

  ps：`__pycache__` 是模块的缓存文件，储存编译过的机器码方便下次调用

* `cd <path to directory>` - **c**hange **d**irectory

  cd /mnt/c/Users/ - home directory - 非当前目录

  	22044 - Users Name

  cd Desktop - desktop directory - 当前目录

* `cd ..` - the parent directory

* `cd ~` - home directory

* `mkdir <directory name>`  -  **m**a**k**es a new **dir**ectory

* `mv <source path> <destination path>` - move

# Assignment

- `lab00.py`: The template file you'll be adding your code to
  `lab00.py`：要将代码添加到的模板文件
- `ok`: A program used to test and submit assignments
  `ok`：用于测试和提交作业的程序
- `lab00.ok`: A configuration file for `ok`
  `lab00.ok`：`ok` 的配置文件

# .ok 系统的配置

让我们详细拆解这个配置文件：

1. **`name`**：作业名称，表明这是 "Lab 0"。
2. **`endpoint`**：表示与服务器端相关的路径，可能用于提交作业。
3. **`src`**：这是源文件的列表，表示这个 Lab 需要加载哪些文件进行测试。比如 `lab00.py` 和 `parsons_probs/ilove61a.py`。`lab_.py` 应该是和 `lab00.py` 类似的作业文件。
4. **`tests`**：该字段定义了如何测试不同的文件。对于 `lab*.py` 文件，使用 `doctest`，而 `tests/*.py` 文件则使用 `ok_test`，这意味着这些文件的测试方式不同。
5. **`default_tests`**：默认测试的名称，比如 `twenty_twenty_two`、`python-basics` 和 `ilove61a`。这些测试是 OK 系统在运行时的默认测试集合。
6. **`protocols`**：这些协议指的是与作业相关的操作，比如：
   - `restore`：恢复默认文件状态。
   - `file_contents`：检查文件内容。
   - `analytics`：分析作业状态。
   - `unlock`：解锁测试问题。
   - `grading`：与评分相关的操作。
   - `backup`：将作业备份到服务器。
7. **`parsons`**：该字段定义了与 Parsons 问题（特定类型的编程练习）相关的信息。在这个例子中，`ilove61a` 是一个必需的 Parsons 问题。
