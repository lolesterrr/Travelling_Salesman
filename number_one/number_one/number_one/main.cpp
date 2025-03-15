#include <iostream>
#include <iomanip> // For std::setw
using namespace std;

int main() {
	
	//Letters A to G Represent cities with the respective First letters
    string cities[7] = {"A", "B", "C", "D", "E", "F", "G"};
	
	
    // Define the adjacency matrix
    int graph[7][7] = {
        {0, 12, 10, 0, 9, 0, 12},
        {12, 0, 8, 12, 0, 0, 0},
        {10, 8, 0, 11, 3, 0, 0},
        {0, 12, 11, 0, 11, 10, 0},
        {9, 0, 3, 11, 0, 6, 7},
        {0, 0, 0, 10, 6, 0, 9},
        {12, 0, 0, 0, 7, 9, 0}
    };

    // Print matrix
    cout << "***********************ADJACENCY MATRIX**************************" << endl;
    cout << "   Atlanta   Boston   Chicago   Dallas    El-Paso  FortWorth  Gary" << endl;
    for (int i = 0; i < 7; i++) {
        cout << left << setw(8) << cities[i] << " ";
        for (int j = 0; j < 7; j++) {
            cout << setw(8) << graph[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
