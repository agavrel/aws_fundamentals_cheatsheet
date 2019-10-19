PD = pandoc

PDFLAGS = --from markdown-yaml_metadata_block --latex-engine=xelatex -V geometry:margin=1in -V CJKmainfont="Noto Serif CJK JP"

Aws_Fundamentals.pdf: README.md
	python md_creator.py
	$(PD) $(PDFLAGS) README.md -o $@
