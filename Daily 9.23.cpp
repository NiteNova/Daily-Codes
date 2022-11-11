#include <iostream>
using namespace std;

int main() {
    int room = 1;
    char choice - 'a';

    while (choice != 'q') { //game loop
        switch(room) {  
        

        case 1:
            cout <<"You're in room 1, you can go (s)outh)" << endl;
            cin >> choice;
            if choice(choice == 's' || choice = 'S')
                room = 2;
            else
                cout<<"Sorry, not an option"<< endl;
            break;
        case 2:
            cout <<"You're in room 2, you can go (s)outh, (n)orth, (w)est " << endl;
            cin >> choice;
            if choice(choice == 's' || choice = 'S')
                room = 4;
            elif choice(choice == 'w' || choice = 'W')
                room = 3;
            elif choice(choice == 'n' || choice = 'N')
                room = 1;
            else
                cout<<"Sorry, not an option"<< endl;
            break;
        case 3:
            cout <<"You're in room 3, you can go (e)ast)" << endl;
            cin >> choice;
            if choice(choice == 'e' || choice = 'E')
                room = 2;
            else
                cout<<"Sorry, not an option"<< endl;
            break;
        case 4:
            cout <<"You're in room 4, you can go (n)orth)" << endl;
            cin >> choice;
            if choice(choice == 'm' || choice = 'North')
                room = 2;
            else
                cout<<"Sorry, not an option"<< endl;
            break;




        } // end switch

    } //end game loop

} //end main