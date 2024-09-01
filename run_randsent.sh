grammar="grammar.gr"
start_symbol="ROOT"
num_sentences=1
max_expansions=450

python3 randsent.py -g $grammar -s $start_symbol -n $num_sentences -M $max_expansions -t