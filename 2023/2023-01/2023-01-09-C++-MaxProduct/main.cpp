#include <iostream>
#include <vector>
#include <algorithm>

#include "array.h"

#include "test.h"

int main()
{
	size_t maxVal = 0;

	const auto dim = 5 /* window size */;

	size_t index = 0;
	for (const int* mat : { 
		test_arr_0, test_arr_1, test_arr_2, test_arr_3, test_arr_4, 
		test_arr_5, test_arr_6, test_arr_7, test_arr_8, test_arr_9, 
		test_arr_10 
		}) {
		
		auto w = width[index];
		auto h = height[index];

		if ((w < 5) && (h < 5)) {
			std::cout << "Data " << index << " error: width & height all less than 5." << std::endl;
			++index;
			continue;
		}

		Array arr(reinterpret_cast<const int*>(mat), h, w);

		size_t max_prod = 0;

		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				size_t row = 1, col = 1, ltrb = 1, lbrt = 1;
				for (int k = 0; k < 5; ++k) {
					row *= arr[{i, j + k}];
					col *= arr[{i + k, j}];
					ltrb *= arr[{i + k, j + k}];
					lbrt *= arr[{i + 4 - k, j + k}];
				}
				max_prod = std::max({ max_prod, row, col, ltrb, lbrt });
			}
		}

		std::cout << "Max product of test data " << index << " is: " << max_prod << std::endl;

		++index;
	}

	return 0;
}
