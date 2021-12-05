SOLUTION_TARGET := Group37A4.tgz

SOLUTION_FILES := $(wildcard *.py)
SOLUTION_FILES += README.txt

.PHONY: all clean

all: solution

solution:
	tar -cf $(SOLUTION_TARGET) $(SOLUTION_FILES)

clean:
	-rm -f $(SOLUTION_TARGET)
