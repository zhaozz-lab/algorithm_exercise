#include <stdio.h>
#include <memory.h>
#include <fstream>

#define C_TAG "From C"
#define PRINT_MSG_2SP(ARG0, ARG1) printf("%s - [%s] (%d) - [%s]:  %s: 0x%0p\n", C_TAG, __FILE__, __LINE__, __FUNCTION__, ARG0, ARG1)


using std::endl;

std::ofstream outFile;


class Detector {
    public:
        Detector();
        void process(int *pIn, int *pOut, int n);

    private:
        int m_var;
};


Detector::Detector() 
: m_var(0) {。
    outFile.open("addr_debug.txt");
    outFile << "m_var init address: " << &m_var << endl;
    PRINT_MSG_2SP("&m_var", &m_var);
}

void Detector::process(int *pIn, int *pOut, int n) {
    outFile << "m_var process address: " << &m_var << endl;
    outFile.close();
    PRINT_MSG_2SP("&m_var", &m_var);
}


#define SIM_EXPORT __declspec(dllexport)

#if defined(__cplusplus)
extern "C" {
#endif

    SIM_EXPORT Detector *DetectorNew() { return new Detector(); }
    SIM_EXPORT void DetectorProcess(Detector *pDet, int *pIn, int *pOut, int n) {
        pDet->process(pIn, pOut, n);
    }
    SIM_EXPORT void DetectorDelete(Detector *pDet) { delete pDet; }

#if defined(__cplusplus)
}
#endif