#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 定义木棒结构体
struct Stick {
    int length;
    int weight;
    int index;
};

// 比较函数，用于对木棒按照长度从小到大排序
bool compareSticks(Stick a, Stick b) {
    return a.length < b.length;
}

int main() {
    int n;
    cin >> n;

    vector<Stick> sticks(n);

    // 输入木棒的长度和重量，并初始化索引
    for (int i = 0; i < n; ++i) {
        cin >> sticks[i].length >> sticks[i].weight;
        sticks[i].index = i + 1;
    }

    // 按照长度从小到大排序木棒
    sort(sticks.begin(), sticks.end(), compareSticks);

    // 动态规划计算最少准备时间
    vector<int> dp(n);
    for (int i = 0; i < n; ++i) {
        dp[i] = 1;
        for (int j = 0; j < i; ++j) {
            if (sticks[j].weight <= sticks[i].weight) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }

    // 找到最大的最少准备时间
    int maxTime = 0;
    int maxIndex = 0;
    for (int i = 0; i < n; ++i) {
        if (dp[i] > maxTime) {
            maxTime = dp[i];
            maxIndex = i;
        }
    }

    // 输出加工顺序
    vector<int> result;
    for (int i = maxIndex; i >= 0; --i) {
        if (dp[i] == maxTime) {
            result.push_back(sticks[i].index);
            --maxTime;
        }
    }

    // 输出结果
    cout << "sequence：";
    for (int i = result.size() - 1; i >= 0; --i) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}