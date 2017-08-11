ANACONDA3  = /opt/conda
CPP        = gcc
CFLAGS     = -c
SRCS       = calc.cpp
TARGET     = _calc
CXXSRCS    = calc_wrap.cxx
PYTHON_INCLUDE    = -I$(ANACONDA3)/include/python3.5m
PYTHON_LIB = -L$(ANACONDA3)/lib -lpython3.5m
LIBS       =
INTERFACE  = $(SRCS:.cpp=.i)
SWIG       = swig
SWIGOPT    = -c++ -python 
SO		   = .so
CCSHARED   = -fPIC
CXXSHARED  = g++ -shared
OBJS       = $(SRCS:.cpp=.o) $(CXXSRCS:.cxx=.o)

all: $(SRCS)
	$(SWIG) $(SWIGOPT) $(INTERFACE)
	$(CPP) $(CCSHARED) $(CFLAGS) $(ICXXSRCS) $(SRCS) $(CXXSRCS) $(PYTHON_INCLUDE) 
	$(CXXSHARED) $(OBJS) -o $(TARGET)$(SO) $(PYTHON_INCLUDE) $(PYTHON_LIB)

test:
	g++ -lgtest -pthread calc.cpp test.cpp -o test

clean:
	rm -f *_wrap* *.o *~ *$(SO) mypython *.pyc .~* core
