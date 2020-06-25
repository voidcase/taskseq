next:
	task rc:test/config next

reset:
	rm -rf test/taskstore && cp -rf test/prototype_taskstore test/taskstore

run:
	python3 taskseq.py --config ./test/config 1,2,3--4--5,6,7--8--9,10
