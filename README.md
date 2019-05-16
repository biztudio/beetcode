# beetcode

[![Build Status](https://dev.azure.com/biztudioCI/beetcode/_apis/build/status/biztudio.beetcode?branchName=master)](https://dev.azure.com/biztudioCI/beetcode/_build/latest?definitionId=2&branchName=master)

My Alg practice on [My Leetcode](https://leetcode-cn.com/biztudio/). ( language: javascript / python / SQL )

* 考虑一题多解及最优解；
* 用 Python 和 ES6 来实现，用 [behave](http://behave.github.io/behave.example/) 和 [jest](https://jestjs.io/zh-Hans/) 进行 BDD / TDD 验证;
* 用 [DocToc](https://github.com/thlorenz/doctoc) 进行 markdown 文档的整理
* 使用 [Azure DevOps Pipeline](https://dev.azure.com/biztudioCI/beetcode/_build) 进行持续集成测试

环境：
* macOS / Linux
  * Python (3.7.1) 
    * python**3** -m venv beetcode.venv
    * source ./beetcode.venv/bin/activate
    * pip**3** install --upgrade pip
    * pip**3** install -r requirements.txt
* Windows
  * Python (3.7.1) 
    * python -m venv beetcode.venv
    * .\beetcode.venv\Scripts\activate.bat
    * python -m pip install --upgrade pip
    * pip install -r requirements.txt
  * Anaconda
    * conda create -n beetcode.venv python=3.7.1