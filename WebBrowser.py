import webbrowser

def main():
	userinput = input("Search by DuckDuckGo: ")
	if (userinput == "exit"):
		return 0
	userinputsplit = list(userinput)
	adress = "https://duckduckgo.com/?q="
	for ch in userinputsplit:
		match ch:
			case ' ':
				adress += "+"
			case '+':
				adress += "%2B"
			case '/':
				adress += "%2F"
			case '=':
				adress += "%3D"
			case _:
				adress += ch
	webbrowser.open(adress)

main()
