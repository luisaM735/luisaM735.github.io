/*Luisa Martinez
  Loan Calculator
  Assignment 2
  9/23/23*/

#include<iostream>
#include<cmath>
#include<cstdlib>
#include <iomanip>

using namespace std;


double monthly_interest(double apr);
double amortization_calc(double p, double r, int n);
void interest_balance_calculation(double& p, double r,int n, double& interest, double& principal_payment, double m);
void  total_pay_and_interest(double p, double r, int n, double& total_pay, double& total_interest, double& apr);
void user_input(double& p, double& apr, int& n);
void table_output(double& p, double& interest, double& principal_payment, double m);
void sum_output(double& total_pay, double& total_interest, double m, int n);

int main(){
    int n;
    double apr,interest,principal_payment, total_pay=0, total_interest, p;

    user_input(p, apr, n);
    double r = monthly_interest(apr);
    double m =amortization_calc(p, r, n);


    for(int i=1;i<=n;i++){
        interest_balance_calculation(p,r,n,interest, principal_payment,m);
        table_output(p,interest, principal_payment,m);
        p -= principal_payment;
        total_pay_and_interest(p,r,n,total_pay,total_interest, apr);
    }
    sum_output(total_pay, total_interest, m,n);

    return 0;

}

//An input function which prompts and fills the input with values for P, APR, and n(call by reference function)
void user_input(double& p, double& apr, int& n){
    cout<< "What is the principal loan amount?:$";
    cin>> p;
    cout<< "P = $"<< p<< endl;

    cout<<"What is the annual percentage rate?: ";
    cin>> apr;
    cout<<"APR = "<< apr << "%" << endl;

    cout<< "What is the number of loan payments?: ";
    cin>> n;
    cout<< "n = "<< n<< endl;
};


//A function that calculates and returns monthly interest rate (r) using the APR as input argument.
double monthly_interest(double apr){
    double r = pow((1+(apr/100)),(1.0/12)) - 1;
    return r;
};

//A function that calculates and returns amortization, M using inputs of P, r, and n.
double amortization_calc(double p, double r, int n){
    double m = p*(r*pow(1+r,n))/(pow(1+r,n)-1);
    return m;
};

//A function that calculates the interest and principal balance for every month(call-by reference function)
void interest_balance_calculation(double& p, double r, int n, double& interest, double& principal_payment, double m){
        interest = p*r;
        principal_payment = m - interest;

};
//function that keeps track of total payment and total interest accumulated. This can be(call-by-reference function)
void  total_pay_and_interest(double p, double r, int n, double& total_pay, double& total_interest, double& apr){
    total_pay =0.0;
    total_interest = 0.0;
    double principal_payment, interest,m;

    for(int i=1;i<=n;i++){
            interest_balance_calculation(p,r,n,interest,principal_payment,m);
            total_pay += m;
            total_interest += interest;
        }

    };


//output function which displays tabular information(call-by-reference)
void table_output(double& p, double& interest, double& principal_payment, double m){
    cout << "Beginning Balance: $" << setw(8) << right <<fixed<<setprecision(2)<< p << " | ";
    cout << "Interest: $" << setw(8) << right<<fixed<<setprecision(2) << interest << " | ";
    cout << "Principal Payment: $" << setw(8) << right<<fixed<<setprecision(2) << principal_payment << " | ";
    cout << "Ending Balance: $" << setw(10) << right <<fixed<<setprecision(2)<< p - principal_payment << endl;
};

//output function which displays the summary of payments at the end(call-by-reference function)
void sum_output(double& total_pay, double& total_interest, double m, int n){
        cout<< "Payment every month: $"<< fixed<<setprecision(2)<<m<<endl;
        cout<< "Total payments: $"<<fixed<< setprecision(2)<<total_pay<<endl;
        cout<< "Total interest: $"<<fixed<< setprecision(2)<<total_interest<<endl;
};

