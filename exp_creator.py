def evaluate_exp(expi):
	exp = list(expi)
	#A terrible expression evaluator

	#first evaluate Joins
	count = len(exp)
	i = 0
	while i < count:
		if exp[i] == "J":
			exp[i-1] = exp[i-1] + exp[i+1]
			exp.pop(i)
			exp.pop(i)
			count = count -2
		else: 
			i = i + 1

	#then evaluate Multipliers
	count = len(exp)
	i = 0
	while i < count:
		if exp[i] == "P":
			exp[i-1] = str(int(exp[i-1]) * int(exp[i+1]))
			exp.pop(i)
			exp.pop(i)
			count = count -2
		else:
			i = i + 1

	#then evalute Additions
	count = len(exp)
	i = 0
	while i < count:
		if exp[i] == "A":
			exp[i-1] = str(int(exp[i-1]) + int(exp[i+1]))
			exp.pop(i)
			exp.pop(i)
			count = count -2
		else:
			i = i + 1

	return exp


@viz
def rec_exp_creator(strd, index, k, opl, result, outl):
	if index == len(strd) - 1:
		result.append(strd[index])
		eval_l = evaluate_exp(result)
		if int(eval_l[0]) == k:
			out = "".join(result)
			out = out.replace("J", "")
			out = out.replace("A", "+")
			out = out.replace("P", "*")
			outl.append(out+"="+eval_l[0])
		return
	else:
		for o in opl:
			ol = list(result)
			ol.append(strd[index])
			ol.append(o)
			rec_exp_creator(strd, index+1, k, opl, ol, outl)


@viz
def expression_creator(strd, k):
	outl = list()
	rec_exp_creator(strd , 0, k, ["J", "P", "A"], list(), outl)
	print(outl)

expression_creator("222", 24)
callgraph.render("expression_creator_backtrack.png")


