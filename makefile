TEXSRC = traffic_aware_topology.tex
BIBSRC = reference.bib
FIGS = 

FILES := $(shell wget -q -O traffic_aware_topology.tex https://script.google.com/macros/s/AKfycbx9H3rjAoYCj63akwpVa4KvbZw9et_AQNrwTXxcszJ__yHfY6w/exec)

ALLSRC = $(TEXSRC) $(BIBSRC) $(FIGS) 

all: traffic_aware_topology.pdf

traffic_aware_topology.pdf: traffic_aware_topology.ps
	ps2pdf14 traffic_aware_topology.ps
	open traffic_aware_topology.pdf

traffic_aware_topology.ps: traffic_aware_topology.dvi
	dvips -t letter -e 0 -o traffic_aware_topology.ps traffic_aware_topology.dvi

traffic_aware_topology.dvi: $(ALLSRC) traffic_aware_topology.bbl
	pdflatex traffic_aware_topology
	pdflatex traffic_aware_topology

traffic_aware_topology.aux: $(ALLSRC)
	latex traffic_aware_topology

traffic_aware_topology.bbl: $(ALLSRC) traffic_aware_topology.aux
	bibtex traffic_aware_topology

clean:	
	rm -f traffic_aware_topology.aux traffic_aware_topology.log traffic_aware_topology.bbl


