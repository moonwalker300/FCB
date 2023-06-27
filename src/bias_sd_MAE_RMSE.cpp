#include <cstdio>
#include <cstdlib>
#include <fstream>
//#define generate
using namespace std;
#define CN 50
#define abs(x) ((x) > 0 ? (x) : (-(x)))
void readNumber(float& f, ifstream& in) {
	f = 0;
	char ch;
	while (true) {
		in.get(ch); 
		if (ch == ':')
			break;
	}
	float fh = 1;
	while (true) {
		in.get(ch);
		if (ch == '-')
			fh = -1;
		if ((ch >= '0') && (ch <= '9'))
			break;
	}
	f = ch - '0';
	float jz = 1;
	bool inte = true;
	while (true) {
		in.get(ch);
		if ((ch >= '0') && (ch <= '9')) {
			if (inte)
				f = f * 10 + ch - '0';
			else {
				jz /= 10;
				f += jz * (ch - '0');
			}	
		} else if (ch == '.')
			inte = false;
		else
			break;
	}
	f *= fh;
}

float Var(float* a) {
	float sum2 = 0, sum = 0;
	for (int i = 0; i < CN; i++) {
		sum2 += a[i] * a[i];
		sum += a[i];
	}
	sum2 /= CN;
	sum /= CN;
	sum = sum * sum;
	return sum2 - sum;
}

float Ave(float* a) {
	float sum = 0;
	for (int i = 0; i < CN; i++) 
		sum += a[i];
	
	sum /= CN;
	return sum;
}
float Mae(float *a, float gdt) {
	float sum = 0;
	for (int i = 0; i < CN; i++)
		sum += abs(a[i] - gdt);
	sum /= CN;
	return sum;
}

float Rmse(float *a, float gdt) {
	float sum = 0;
	for (int i = 0; i < CN; i++)
		sum += (a[i] - gdt) * (a[i] - gdt);
	sum /= CN;
	return sqrt(sum);
}

int main() {
	char filename[CN];
    ifstream in_gd("GroundTruth.gdt");
	float gd;
	in_gd >> gd;
	float newMethod[CN];
	for (int i = 0; i < CN; i++) {
		sprintf_s(filename, "Exp.%d", i); //Repeat Experiment File
		printf("%d\n", i);
		ifstream in(filename);
		readNumber(newMethod[i], in);
	}
	printf("balancing rmse:%f\n", Rmse(newMethod, gd));
	printf("balancing mae:%f\n", Mae(newMethod, gd));
	printf("balancing bias:%f\n", abs(Ave(newMethod) - gd));
	printf("balancing sd:%f\n", sqrt(Var(newMethod)));
	return 0;
}