export
AMPY_PORT:=/dev/tty.usbserial-537A0373131

.PHONY: put
put:
	ampy put main.py mazes.py
	# screen -S ttys003 -X quit

.PHONY: gen
gen:
	python3 convert.py > mazes.py

.PHONY: log
log:
	screen $(AMPY_PORT) 115200 -S M5Stack