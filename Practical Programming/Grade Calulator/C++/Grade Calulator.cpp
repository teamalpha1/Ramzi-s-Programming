// Grade Calulator.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int main()
{
	int grade;

	cout << "Hello teacher!" << endl;
	this_thread::sleep_for(2s);

	cout << "Please input the student's grade: ";
	cin >> grade;
	cout << endl;

	if (grade >= 0 && grade <= 59) {
		cout << "Your Grade is F, from a mark of " << grade << endl;
		this_thread::sleep_for(2s);
		system("PAUSE");
	}

	else if (grade >= 60 && grade <= 69) {
		cout << "Your Grade is D, from a mark of " << grade << endl;
		this_thread::sleep_for(2s);
		system("PAUSE");
	}

	else if (grade >= 70 && grade <= 79) {
		cout << "Your Grade is C, from a mark of " << grade << endl;
		this_thread::sleep_for(2s);
		system("PAUSE");
	}

	else if (grade >= 80 && grade <= 89) {
		cout << "Your Grade is B, from a mark of " << grade << endl;
		this_thread::sleep_for(2s);
		system("PAUSE");
	}

	else if (grade >= 90 && grade <= 100) {
		if (grade == 100) {
			cout << "You got a perfect score of a 100!" << endl;
			system("PAUSE");
		}
		else {
			cout << "Your Grade is A, from a mark of " << grade << endl;
			this_thread::sleep_for(2s);
			system("PAUSE");
		}
	}

    return 0;
}