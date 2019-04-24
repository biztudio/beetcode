动态规划
---

问题的性质：求出f(n)，只需要知道几个更小的f(c)。我们将求解f(c)称作求解f(n)的“子问题”。
这就是DP（动态规划，dynamic programming）.
将一个根问题拆成几个子问题，分别求解这些子问题，即可推断出根问题的解。

一言以蔽之：大事化小，小事化了。
简单来说就是：递归可解+缓存重复分支，防止了不必要的递归。

* 思考动态规划的第一点----最优子结构: 
  > 子问题最优时，母问题通过优化选择后一定最优的情况叫做“最优子结构”
* 思考动态规划的第二点----子问题重叠：
  > 母问题与子问题本质上是同一个问题的情况称为“子问题重叠”。然而问题中出现的不同点往往就是被子问题之间传递的参数
* 思考动态规划的第三点----边界：
  > 子问题在一定时候就不再需要提出子子问题的情况叫做边界，没有边界就会出现死循环。
* 思考动态规划的第四点----子问题独立：
  > 一个母问题在对子问题选择时，当前被选择的子问题两两互不影响的情况叫做“子问题独立”。
* 思考动态规划的第五点----做备忘录：
  > 可以把问题的解置于一个变量中，如果再次遇到这个问题就直接从变量中获得答案，因此每一个问题仅会计算一遍，如果不做备忘的话，动态规划就没有任何优势可言了
  * 思考动态规划的第六点----时间分析：
  > 

参考资料:
* [什么是动态规划？动态规划的意义是什么？](https://www.zhihu.com/question/23995189)
* [动态规划初步·各种子序列问题](https://pks-loving.blog.luogu.org/junior-dynamic-programming-dong-tai-gui-hua-chu-bu-ge-zhong-zi-xu-lie)
* [通过金矿模型介绍动态规划](http://www.cnblogs.com/sdjl/articles/1274312.html)
* [漫画说算法--动态规划算法](https://blog.csdn.net/baidu_37107022/article/details/73189125)