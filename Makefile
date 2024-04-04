export
AMPY_PORT:=/dev/tty.usbserial-537A0373131

.PHONY: run
run:
	ampy put main.py

.PHONY: gen
gen:
	python3 convert.py > mazes.py

.PHONY: log
	screen $(AMPY_PORT) 115200