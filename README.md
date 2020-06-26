# taskseq

Make taskwarrior tasks sequential easily

## Installation

	pip3 install taskseq

## Usage

like this:

	taskseq 1,2,3--4,5--6--7

In  this example, task 4 and 5 will both depend on 1, 2 and 3.
task 6 will depend on 4 and 5
task 7 will depend on 6

You can think of it like this:

	,  <=> "and"
	-- <=> "(which) must be completed before"

so the sequence

	10,7,8--4,15--2

means

	10 and 7 and 8 must be completed before 4 and 15
	which must be completed before 2
