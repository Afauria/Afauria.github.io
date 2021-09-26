---
layout: post
title: 排序算法
date: 2019-01-01
description: 排序算法笔记
categories: 算法
tags: 
- 算法
---

### 冒泡排序

```java
//冒泡排序
//比较相邻的元素。如果第一个比第二个大，就交换它们两个；
//对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
//针对所有的元素重复以上的步骤，除了最后一个；
//重复步骤1~3，直到排序完成。
private void bubbleSort(int[] arr) {
	int len = arr.length;
	for (int i = 0; i < len - 1; i++) {
		for (int j = 0; j < len - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) {        // 相邻元素两两对比
				int temp = arr[j + 1];        // 元素交换
				arr[j + 1] = arr[j];
				arr[j] = temp;
			}
		}
	}
}
```

### 选择排序

```java
//选择排序
//首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
// 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
// 以此类推，直到所有元素均排序完毕。
private void selectSort(int[] arr) {
	int len = arr.length;
	int minIndex, temp;
	for (int i = 0; i < len - 1; i++) {
		minIndex = i;
		for (int j = i + 1; j < len; j++) {
			if (arr[minIndex] > arr[j]) {
				minIndex = j;
			}
		}
        temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}
```

### 插入排序

```java
//插入排序
//从第一个元素开始，该元素可以认为已经被排序；
//取出下一个元素，在已经排序的元素序列中从后向前扫描；
//如果该元素（已排序）大于新元素，将该元素移到下一位置；
//重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
//将新元素插入到该位置后；
//重复步骤2~5。
private int[] insertSort(int[] arr) {
	int len = arr.length;
    int index, current;
    for (int i = 1; i < len - 1; i++) {
        index = i - 1;
        current = arr[i];
        while (index >= 0 && current < arr[index]) {
            arr[index + 1] = arr[index];
            index--;
        }
        arr[index + 1] = current;
    }
	return arr;
}
```

### 快速排序

```java
//快速排序,平均时间复杂度：O(NlogN)
//选择一个基准（第一个或最后一个）
//j从右往左（j--）找到小于基准的数a，i从左往右（i++）找到大于基准的数b，交换a、b
//j继续往左，i继续往右，不断交换
//直到i和j相等，将其与基准进行交换，此时基准（第i或第j个数）左边都小于基准，基准右边都大于基准
//左右分别进行快排
private void quickSort(int[] arr, int left, int right) {
    if (left > right) {
        return;
    }
    int pivot = arr[left];
    int i = left, j = right;
    while (i != j) {
        while (arr[j] >= pivot && i < j) {
            j--;
        }
        while (arr[i] <= pivot && i < j) {
            i++;
        }
        if (i < j) {
            int t = arr[i];
            arr[i] = arr[j];
            arr[j] = t;
        }
    }
    arr[left] = arr[i];
    arr[i] = pivot;
    quickSort(arr, left, i - 1);
    quickSort(arr, i + 1, right);
	}
}
```

**参考文章**

[十大经典排序算法（动图演示）](https://www.cnblogs.com/onepixel/p/7674659.html)

