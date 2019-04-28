# beetcode

[![Build Status](https://travis-ci.org/biztudio/beetcode.svg?branch=master)](https://travis-ci.org/biztudio/beetcode)
[![Build Status](https://travis-ci.org/biztudio/beetcode.svg?branch=pb115)](https://travis-ci.org/biztudio/beetcode)

My Alg practice on [Leetcode](https://leetcode-cn.com). ( language: javascript / python / SQL )

* 考虑一题多解及最优解；
* 用 Python 和 ES6 来实现，用 [behave](http://behave.github.io/behave.example/) 和 [jest](https://jestjs.io/zh-Hans/) 进行 TDD 验证;
* 用 [DocToc](https://github.com/thlorenz/doctoc) 进行 markdown 文档的整理
* 使用 Travis CI 进行持续集成测试

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