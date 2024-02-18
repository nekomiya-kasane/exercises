#pragma once

#ifndef MY_ARRAY_H
#define MY_ARRAY_H

struct Array {
	Array(const int* iArray, size_t iHeight, size_t iWidth) : arr(iArray), height(iHeight), width(iWidth) {}

	inline int operator[](std::pair<int, int> iLoc) {
		if ((iLoc.first < 0) || (iLoc.second < 0) || (iLoc.first >= height) || (iLoc.second >= width)) {
			return 0;
		}
		return arr[width * iLoc.first + iLoc.second];
	}

protected:
	const int* arr;
	size_t width, height;
};

#endif