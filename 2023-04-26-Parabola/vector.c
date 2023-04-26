#include <stdio.h>
#include <math.h>
#include <malloc.h>

#include "vector.h"

vector* new_vector(VecType iType, int iSize) {
	vector* res = (vector*)malloc(sizeof(vector));
	res->type = iType;
	res->ddata = NULL;
	res->size = iSize;

	if (!iSize)
		return res;

	if (iType == DOUBLE) {
		res->ddata = (double*)malloc(sizeof(double) * iSize);
		for (long i = 0; i < iSize; ++i) {
			res->ddata[i] = 0;
		}
	}
	else if (iType == LONG) {
		res->ldata = (long*)malloc(sizeof(long) * iSize);
		for (long i = 0; i < iSize; ++i) {
			res->ldata[i] = 0;
		}
	}
	return res;
}

void free_vector(vector** iVec) {
	if (!iVec) 
		return;

	vector* vec = *iVec;

	switch (vec->type)
	{
	case DOUBLE: if (vec->ddata) free(vec->ddata); break;
	case LONG: if (vec->ldata) free(vec->ldata); break;
	}

	free(vec);
	*iVec = NULL;
}

void print_vector(vector* iVec) {
	for (long i = 0; i < iVec->size; ++i) {
		if (iVec->type == DOUBLE) {
			printf("%.12e\n", get_double(iVec, i));
		}
		else {
			printf("%ld\n", get_long(iVec, i));
		}
	}
}

int set(vector* iVec, long iInd, double iData) {
#ifdef _DEBUG
	if ((iVec->type != DOUBLE) || (iVec->size <= iInd)) {
		return 1;
	}
#endif
	iVec->ddata[iInd] = iData;
	return 0;
}

//int set(vector* iVec, long iInd, long iData) {
//#ifdef _DEBUG
//	if ((iVec->type != LONG) || (iVec->size <= iInd)) {
//		return 1;
//	}
//#endif
//	iVec->ldata[iInd] = iData;
//	return 0;
//}

double get_double(vector* iVec, long iInd) {
#ifdef _DEBUG
	if (iVec->size <= iInd) {
		printf("Invalid input.");
		return 0;
	}
#endif
	return iVec->type == DOUBLE ? iVec->ddata[iInd] : (double)(iVec->ldata[iInd]);
}

long get_long(vector* iVec, long iInd) {
#ifdef _DEBUG
	if (iVec->size <= iInd) {
		printf("Invalid input.");
		return 0;
	}
#endif
	return iVec->type == DOUBLE ? (long)iVec->ddata[iInd] : iVec->ldata[iInd];
}

double min_double(vector* iVec) {
#ifdef _DEBUG
	if (iVec->type != DOUBLE) {
		printf("Invalid input.");
		return 0;
	}
#endif
	if (!iVec->size)
		return 0;

	double ele = iVec->ddata[0];
	for (long i = 1; i < iVec->size; ++i) {
		if (iVec->ddata[i] < ele) {
			ele = iVec->ddata[i];
		}
	}

	return ele;
}

long min_long(vector* iVec) {
#ifdef _DEBUG
	if (iVec->type != LONG) {
		printf("Invalid input.");
		return 0;
	}
#endif
	if (!iVec->size)
		return 0;

	long ele = iVec->ldata[0];
	for (long i = 1; i < iVec->size; ++i) {
		if (iVec->ldata[i] < ele) {
			ele = iVec->ldata[i];
		}
	}

	return ele;
}

double max_double(vector* iVec) {
#ifdef _DEBUG
	if (iVec->type != DOUBLE) {
		printf("Invalid input.");
		return 0;
	}
#endif
	if (!iVec->size)
		return 0;

	double ele = iVec->ddata[0];
	for (long i = 1; i < iVec->size; ++i) {
		if (iVec->ddata[i] > ele) {
			ele = iVec->ddata[i];
		}
	}

	return ele;
}

long max_long(vector* iVec) {
#ifdef _DEBUG
	if (iVec->type != LONG) {
		printf("Invalid input.");
		return 0;
	}
#endif
	if (!iVec->size)
		return 0;

	long ele = iVec->ldata[0];
	for (long i = 1; i < iVec->size; ++i) {
		if (iVec->ldata[i] > ele) {
			ele = iVec->ldata[i];
		}
	}

	return ele;
}

int transform(vector* iSrc, vector* iDest, transformer_double iFunc) {
	if (!iSrc || !iDest
		|| (iSrc->type != iDest->type)
		|| (iSrc->type != DOUBLE)
		|| !iSrc->ddata) {
		printf("Invalid Vector.\n");
		return 1;
	}

	if (iDest->ddata) {
		free(iDest->ddata);
	}

	iDest->ddata = (double*)malloc(sizeof(double) * iSrc->size);
	for (long i = 0; i < iSrc->size; ++i) {
		iDest->ddata[i] = iFunc(iSrc->ddata[i]);
	}

	return 0;
}

//int transform(vector* iSrc, vector* iDest, transformer_long iFunc) {
//	if (!iSrc || !iDest
//		|| (iSrc->type != iDest->type)
//		|| (iSrc->type != LONG)
//		|| !iSrc->ldata) {
//		printf("Invalid Vector.\n");
//		return 1;
//	}
//
//	if (iDest->ldata) {
//		free(iDest->ldata);
//	}
//
//	iDest->ldata = (double*)malloc(sizeof(double) * iSrc->size);
//	for (long i = 0; i < iSrc->size; ++i) {
//		iDest->ldata[i] = iFunc(iSrc->ldata[i]);
//	}
//
//	return 0;
//}

int fill_vector(vector* iVec, double iStart, double iEnd, double iStep) {
	if (iVec->type != DOUBLE)
		return 1;

	long n = (long)round((iEnd - iStart) / iStep) + 1;
	if (iVec->size != n) {
		iVec->ddata = (double*)realloc(iVec->ddata, sizeof(double) * n);
		iVec->size = n;
	}

	long counter = 0;
	for (double i = iStart; i <= iEnd + 1e-12; i = i + iStep) {
		iVec->ddata[counter] = i;
		++counter;
	}
	return 0;
}
