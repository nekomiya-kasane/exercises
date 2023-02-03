#ifndef C_VECTOR_H
#define C_VECTOR_H

typedef double (*transformer_double)(double);
typedef long (*transformer_long)(long);

typedef enum { DOUBLE, LONG } VecType;

typedef struct {
	VecType type;
	union {
		double* ddata;
		long* ldata;
	};
	long size;
} vector;

vector* new_vector(VecType iType, int iSize);
void free_vector(vector** iVec);

void print_vector(vector* iVec);

int set(vector* iVec, long iInd, double iData);
//int set(vector* iVec, long iInd, long iData);

double get_double(vector* iVec, long iInd);
long get_long(vector* iVec, long iInd);

double min_double(vector* iVec);
long min_long(vector* iVec);

int transform(vector* iSrc, vector* iDest, transformer_double iFunc);
//int transform(vector* iSrc, vector* iDest, transformer_long iFunc);

int fill_vector(vector* iVec, double iStart, double iEnd, double iStep);



#endif // C_VECTOR_H