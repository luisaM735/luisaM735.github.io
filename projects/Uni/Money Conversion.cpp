/*Coin Dispenser Machine
  Luisa Martinez*/

//AMERICAN COIN SYSTEM

#include <iostream>
#include <iomanip> //for setprecision
#include <math.h> //for rounding
#include <limits> //for numeric_limits
using namespace std;

int choice;
const int QUARTER = 25, DIME = 10, NICKEL = 5, PENNY = 1;
//For Program 1
int amt_in_cents, quarters, dimes, nickels, pennies, change_left;
double dollar_amt;
//For program 2
int q, d, n, p;
double coin_to_dollar;


int main(){

    while(choice != 3){
        cout<< "What type of conversion are you doing?\n 1. Dollar Amount to Coins\n 2. Coin Amount to dollars\n 3. Quit\n";
        cin>> choice;

        //Program 1
        if(choice == 1){
            cout<< "What's the dollar amount of coin change that you need?\n$";
            cin>> dollar_amt;

            while (!(cin >> dollar_amt) || dollar_amt <= 0 || dollar_amt >= 100) {
            cin.clear();  // Clear error flags
            cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Ignore the invalid input
            cout << "Please try again and enter a positive number less than 100.\n";
            exit(1);
            }

            if((dollar_amt<100)&& (dollar_amt>0)&& (cin>> dollar_amt)){
                cout<<"Value in dollars: $" <<dollar_amt << fixed<< setprecision(2)<<"\n";

                //Multiplied by 100.05 because it kept rounding down. I found that this number worked by trial and error.
                amt_in_cents = dollar_amt*100.05 ;
                cout<< "Value in cents: " << amt_in_cents <<"\n";

                //Math to convert dollar amount to coin change
                quarters = amt_in_cents/QUARTER;
                change_left = amt_in_cents%QUARTER;

                dimes = change_left/DIME;
                change_left = change_left%DIME;

                nickels = change_left/NICKEL;
                change_left = change_left%NICKEL;

                pennies = change_left/PENNY;
                cout<< "\nQuarter: "<<quarters<< "\n" << "Dime: " <<dimes<< "\n" << "Nickel: " <<nickels<<"\n" << "Penny: " << pennies<< "\n\n";
            }

        }

        //Program 2
        else if(choice == 2){
            //Website CodeSpeedy showed me how to format and use all the cin functions to verify that the users input is valid
            //!cin checks that the input is an integer
            //cin.peek looks for a new line character, and if it's not found then the input is invalid
            //cin.ignore removes unwanted characters before the next input
            cout << "How many quarters do you have?\n";
            while (!(cin >> q) || q < 0 || cin.peek() != '\n') {
                cout << "Please try again and type a positive integer\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

            cout << "How many dimes do you have?\n";
            while (!(cin >> d) || d < 0 || cin.peek() != '\n') {
                cout << "Please try again and type a positive integer\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

            cout << "How many nickels do you have?\n";
            while (!(cin >> n) || n < 0 || cin.peek() != '\n') {
                cout << "Please try again and type a positive integer\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

            cout << "How many pennies do you have?\n";
            while (!(cin >> p) || p < 0 || cin.peek() != '\n') {
                cout << "Please try again and type a positive integer\n";
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                }

            // Calculate the total value of the coins in dollars
            coin_to_dollar = round(q * QUARTER + d * DIME + n * NICKEL + p * PENNY) / 100.0;
            cout << "The coins are worth: $" << fixed << setprecision(2) << coin_to_dollar << "\n\n";
            }

        else{
            while((choice < 1) || (choice > 3) || (!(cin>>choice))){
            //if choice is not 1 or 2
            cout<< "Your options are 1, 2, or 3. Please try again.\n";
            cin.clear();  // Clear error flags
            cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Ignore the invalid input
        }
    }
    return 0;
}
