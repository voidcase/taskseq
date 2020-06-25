# taskseq

(WARNING: This package is pre-release and does not promise to work the same way in further releases until 1.0.0)

Make taskwarrior tasks sequential easily

like this:

	taskseq 1,2,3--4,5--6--7

In  this example, task 4 and 5 will both depend on 1, 2 and 3.
task 6 will depend on 4 and 5
task 7 will depend on 6
