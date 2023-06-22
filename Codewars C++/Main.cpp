using namespace std;

#include<iostream>
#include<vector>
#include<algorithm>
#include <string>
#include <cctype>
#include <cstring>
#include <map>
#include <math.h>



int main()
{
	cout << findOdd({ 20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5 }) << endl << findOdd({ 0,1,0,1,0 });
	return 0;
}


// numbers less than x, that are divisible by 3 or 5, not counting twice
int solution(int number)
{
	int ans = 0;

	for (int i = 0; i < number; i++) {
		if ((i % 3 == 0 && i % 5 != 0) || i % 5 == 0) {
			ans += i;
		}
	}
	return ans;
}

//Complete the method/function so that it converts dash/underscore delimited words into camel casing.
string to_camel_case(string text) {
	string ans;
	bool cap = false;
	for (int i = 0; i < text.length(); i++) {
		if (text[i] == '_' || text[i] == '-') {
			cap = true;
			continue;
		}
		if (cap == true) {
			ans += toupper(text[i]);
			cap = false;
		}
		else {
			ans += text[i];
		}

	}
	return ans;
}

//Write a function that accepts an array of 10 integers (between 0 and 9), 
//that returns a string of those numbers in the form of a phone number. "(123) 456-7890"

string createPhoneNumber(const int arr[10]) {
	string ans = "(";
	for (int i = 0; i < 10; i++) {
		if (i == 3) {
			ans += ") ";
		}
		if (i == 6) {
			ans += "-";
		}

		ans += to_string(arr[i]);
	}
	return ans;
}

// Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements
//with the same value next to each other and preserving the original order of elements.

template <typename T> vector<T> uniqueInOrder(const vector<T>& iterable) {
	vector<T> ans;
	for (int i = 0; i < iterable.size(); i++) {
		ans.push_back(iterable[i]);
		while (i != iterable.size() - 1 && iterable[i + 1] == iterable[i]) {
			i++;
		}
	}
	return ans;
}

vector<char> uniqueInOrder(const string& iterable) {
	vector<char> ans;
	for (int i = 0; i < iterable.length(); i++) {
		ans.push_back(iterable[i]);
		while (iterable[i + 1] == iterable[i]) {
			i++;
		}
	}
	return ans;
}

//In a small town the population is p0 = 1000 at the beginning of a year.
//The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
//How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

class Arge
{
public:
	static int nbYear(int p0, double percent, int aug, int p) {
		int ans = 0;
		do {
			p0 *= (percent / 100) + 1;
			p0 += aug;
			ans += 1;
		} while (p0 < p);
		return ans;
	}
};

/*Greed is a dice game played with five six-sided dice. Your mission,
should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.
Three 1's => 1000 points
Three 6's =>  600 points
Three 5's =>  500 points
Three 4's =>  400 points
Three 3's =>  300 points
Three 2's =>  200 points
One   1 = > 100 points
One   5 = > 50 point*/

int greed(int number, int count) {
	if (count >= 3) {
		if (number == 1)
			return 1000 + (count % 3) * 100;
		if (number == 5)
			return 500 + (count % 3) * 50;
		return number * 100;
	}
	if (count < 3) {
		if (number == 1)
			return count * 100;
		if (number == 5)
			return count * 50;
		return 0;
	}
}

int score(const std::vector<int>& dice) {
	map<int, int> l;
	int ans = 0;
	for (int x : dice) {
		l[x] += 1;
	}
	for (const auto& kv : l) {
		int d = greed(kv.first, kv.second);
		ans += d;
	}
	return ans;
}

/*Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.*/

int findOdd(const vector<int>& numbers) {
	map<int, int> answ;
	for (int i = 0; i < numbers.size(); i++) {
		if (answ[numbers[i]] == 0)
			answ[numbers[i]] += 1;
		else
			answ[numbers[i]] -= 1;
	}
	for (const auto kv : answ) {
		if (kv.second == 1)
			return kv.first;
	}
}
