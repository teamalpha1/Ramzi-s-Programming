// Macintosh Plus Thoughts.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

int main()
{
	ifstream file;
	file.open("thoughts.csv");
	string line;
	vector <string> thoughts;
	string choice;
	string uselessVar;

	while (file.good()) {
		getline(file, line, '\n');
		thoughts.push_back(line);
	}

	while (true) {
		system("cls");
		int thing = int(int(time(NULL) + rand()*rand()/3) + int(M_PI)/M_E);
		srand(thing);
		int randomIndex = rand() % (thoughts.size()) - 1;
		cout << "Do you want to think some more?" << endl;
		cin >> choice;

		if (choice == "y") {
			cout << thoughts[randomIndex] << endl;
			PlaySound(TEXT("music.wav"), NULL, SND_FILENAME | SND_ASYNC);
			std::this_thread::sleep_for(std::chrono::milliseconds(13000));
		}
	}
	return 0;
}