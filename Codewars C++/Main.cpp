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


/*A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.*/

class Bouncingball
{
public:
    static int bouncingBall(double h, double bounce, double window){
		if (h <= 0 || bounce >= 1 || bounce <= 0 || window >= h){
			return -1;
		}
		int ans = 0;
		do{
			ans++;
			h *= bounce;
			if (h > window){
				ans++;
			}
			
		}while (h > window);
		return ans;
	}
};


/*Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].*/

vector<int> deleteNth(vector<int> arr, int n)
{
	vector <int> ans;
	map<int, int> l;
	for (int i = 0; i<arr.size(); i++){
		if (l[arr[i]] < n){
			ans.push_back(arr[i]);
		}
		l[arr[i]] += 1;
	}
  	return ans;
}


/*Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.*/

int val(char c){
	switch(c){
		case 'I':
			return 1;
			break;
		case 'V':
			return 5;
			break;
		case 'X':
			return 10;
			break;
		case 'L':
			return 50;
			break;
		case 'C':
			return 100;
			break;
		case 'D':
			return 500;
			break;
		case 'M':
			return 1000;
			break;
	}
}

int solution(string roman) {
	int ans = 0;
	for (int i = 0; i < roman.length(); i++){
		if (i == roman.length() - 1){
			return ans + val(roman[i]);
		}
		if (val(roman[i+1]) > val(roman[i])){
			ans += val(roman[i+1])-val(roman[i]);
			i++;
			continue;
		}
		ans += val(roman[i]);
	}
  	return ans;
}


/*Write a function that takes an integer as input, 
and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.*/
string s = "";

unsigned int countBits(unsigned long long n){
	unsigned int ans = 0;
	while(n){
		ans += n & 1;
		n >>= 1;
	}
	return ans;
}


/*Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).*/

pair<size_t, size_t> two_sum(const vector<int>& numbers, int target) {
    for (int i = 0; i< numbers.size(); i++){
		for (int j=i+1; j < numbers.size(); j++){
			if(numbers[i] + numbers[j] == target)
				return {i,j};
		}
	}
}


/*The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.*/

map<char, unsigned> count(const string& string) {
    map <char, unsigned> ans;
	for (const char& c : string){
		ans[c]++;
	}
	return ans;
}


/*A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or more characters. 
The 1st character of a code is a capital letter which defines the book category.
In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) 
which indicates the quantity of books of this code in stock.
For the lists L and M of example you have to return the string:
(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 
114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.
vector<string> s = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"};
vector<string> c = {"A", "B", "C", "W"};
*/

class StockList
{
public:
  static string stockSummary(vector<string> &lstOfArt, vector<string> &categories){
		if (lstOfArt.size() == 0 || categories.size() == 0){
			return "";
		}
		map<char, int> vals;
		string ans = "";
		for (auto s : lstOfArt){
			vals[s[0]] += stoi(s.substr(s.find(" ")));
		}
		for (auto c : categories){
			ans += "(" + c + " : " + to_string(vals[c[0]]) + ") - ";
		}
		return ans.substr(0, ans.size()-3);
  	}
};


/*The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. 
It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 
Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares*/

typedef unsigned long long ull;
class SumFct
{
 	public:
  	static ull perimeter(int n){
		if (n == 0)
			return 0;
		n++;
		ull a = 0, b = 0, ans = 1, curr = 1;
		for (ull i = 1; i < n; i++){
			a = b;
			b = curr;
			curr = a+b;
			ans += curr;
		}
		return 4 * ans;
	}
};


/*Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.*/

typedef long long ll;
int persistence(ll n){
	int ans = 0;
	int len = to_string(n).length();
	ll curr = 1;
	while (len > 1){
		for (int i = 0; i < len; i++){
			curr *= to_string(n)[i] - '0';
		}
		ans ++;
		n = curr;
		len = to_string(curr).length();
		curr = 1;
	}
	return ans;
}


/*Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. 
A tower block is represented with "*" character.
For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ", 
  "*****"
]*/

vector<string> towerBuilder(unsigned nFloors) {
  	int lastFloor = nFloors * 2 - 1;
	string floor = "";
	vector<string> ans;
	for (int i = 1; i < nFloors+1; i++){
		floor += string((lastFloor - (i * 2 - 1))/2, ' ');
		floor += string(i * 2 - 1, '*');
		floor += string((lastFloor - (i * 2 - 1))/2, ' ');
		ans.push_back(floor);
		floor = "";
	}
	return ans;	
}


/*Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.*/

bool validate(string s){
	int len = s.length();
	if (len == 2){
		if (s == ":)" || s == ";)" || s == ":D" || s == ";D"){
			return true;
		}
	}
	if (len == 3){
		if ((s[0] == ':' || s[0] == ';') && (s[1] == '-' || s[1] == '~') && (s[2] == 'D' || s[2] == ')'))
			return true;
	}
	return false;
}

int countSmileys(vector<string> arr)
{
	int ans = 0;
	if (arr.empty()){
		return ans;
	}
 	for (string s : arr){
		if(validate(s))
			ans++;
	}
	return ans;
}


//Same task as before but done easier and more compact using Regex

#include <regex>

int countSmileys(vector<string> arr){
	int ans = 0;
	regex smileys("[:|;](-|~)?[)|D]");
	for (auto &s : arr){
		if(regex_match(s, smileys))
			ans++;
	}
	return ans;
}


/*Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]*/

vector<int> snail(const vector<vector<int>> &snail_map) {
	if (snail_map.empty() || snail_map[0].empty())
		return {};
  	vector<int> ans;
	int x = 0;
	int n = snail_map.size();
	while (x != n){
		for(int i = x; i <= n-1; i++){
			ans.push_back(snail_map[x][i]);
			if(pow(snail_map.size(),2) == ans.size()){
				return ans;
			}
		}
		for(int i = x+1; i <= n-1; i++){
			ans.push_back(snail_map[i][n-1]);
		}
		for(int i = n-2; i >= x; i--){
			ans.push_back(snail_map[n-1][i]);
		}
		for(int i = n-2; i >= x+1; i--){
			ans.push_back(snail_map[i][x]);
		}
		x++;
		n--;
	}
	return ans;
}


/*For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
Test examples:
"EBG13 rknzcyr." -> "ROT13 example."
"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"*/

string rot13(const string& str) {
	string ans = "";
	for (int i = 0; i<str.length();i++){
		if(isalpha(str[i])){
			if(isupper(str[i])){
				ans += str[i] + 13 > 'Z' ? 'A' + (str[i] + 12)  % 'Z' : str[i] + 13;
			}
			else{
				ans += str[i] + 13 > 'z' ? 'a' + (str[i] + 12)  % 'z' : str[i] + 13;
			}
			
		}
		else{
			ans += str[i];
		}
	}
  	return ans;
}


