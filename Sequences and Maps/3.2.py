import sys

def get_odd_list():
	num = int(input())
	ods = []
	while num != -1:
		if num % 2 != 0:
			ods.append(num)
		num = int(input())
	return ods

def main():
	odds = get_odd_list(input())
	print(odds)

if __name__ == "__main__":
    main()