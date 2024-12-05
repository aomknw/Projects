#include <iostream>
#include<stdio.h>
#include<conio.h>
#include <fstream>
using namespace std;

class Food {
    public :
    string name,table;
    char answer = 'Y';
    int number1,number2,order_Piz,order_SS,amount_Piz,amount_SS,change_money1,
    change_money2,change1,change2;
    float hawaiian = 199 ,sea_food = 219 , pepperroni = 199, deluxe = 199 ;
    float spaghetti_cabonara = 99, spaghetti_becon = 89,spaghetti_seafood = 129 ;
    float hotdog = 35, french_fries = 49,sandwich = 25;
    public :
    void Pizza();
    void Spaghetti();
    void Starter();
};
void Food::Pizza() {
    cout << "Name : ";
    cin >> name;
    cout << "Table No. : ";
    cin >> table;
    while (answer =='y' or  answer =='Y') {
        cout << "-------PIZZA-------" << endl;
        cout << "[1] hawaiian   199 ฿ "<< endl;
        cout << "[2] Seafood    219 ฿ "<< endl;
        cout << "[3] Pepperroni 199 ฿ "<< endl;
        cout << "[4] deluxe     199 ฿ "<< endl;
        cout << "[5] Exit "<< endl << endl;
        cout << "What number did you pick : ";   
        cin >> number1;
        switch(number1) {
            case 1 :
            cout << "How many : ";
            cin >> order_Piz ;
            hawaiian *= order_Piz;
            amount_Piz += hawaiian;
            break;
            
            case 2 :
            cout << "How many : ";
            cin >> order_Piz ;
            sea_food *= order_Piz;
            amount_Piz += sea_food;
            break;
            
            case 3 :
            cout << "How many : ";
            cin >> order_Piz ;
            pepperroni *= order_Piz ;
            amount_Piz += pepperroni;
            break;
            
            case 4 :
            cout << "How many : ";
            cin >> order_Piz ;
            deluxe *= order_Piz;
            amount_Piz += deluxe;
            break;
            
            case 5 :
                if (number1 == 5);
                exit(1);
        }
        cout << "Total : " << amount_Piz << " ฿"<< endl <<endl ;
        cout << "You Want Buy again ? [ yes = y or no = n ] : ";
        cin >> answer ;
    }
    cout << endl << "Totality = " << amount_Piz << endl ;
    while(amount_Piz > 0 ) {
            cout << "Please enter the amount : " ;
            cin >> change_money1 ;
            if (change_money1 < amount_Piz ) {
                cout << "Money not enought. Please Enter again "<< endl;
            }
            
            else if (change_money1 >= amount_Piz) {
                change1 = change_money1 - amount_Piz ; 
                break; 
            }
    }
    cout << "Food change = " << change1 << " ฿" << endl;
};

void Food::Spaghetti() {
    cout << "Name : ";
    cin >> name;
    cout << "Table No. : ";
    cin >> table;
    while (answer =='y' or  answer =='Y') {
        cout << "------- SPAGHETTI -------" << endl;
        cout << "[1] Spaghetti Cabonara  99 ฿ "<< endl;
        cout << "[2] Spaghetti Becon     89 ฿ "<< endl;
        cout << "[3] Spaghetti Seafood  129 ฿ "<< endl << endl;
        cout << "-------- STARTER --------" << endl;
        cout << "[4] Hotdog              35 ฿ "<< endl;
        cout << "[5] Frenchfries         49 ฿ "<< endl;
        cout << "[6] Sandwich            25 ฿ "<< endl;
        cout << "[7] Exit "<< endl << endl;
        cout << "What number did you pick : ";   
        cin >> number2;
        switch(number2) {
            case 1 :
            cout << "How many : ";
            cin >> order_SS ;
            spaghetti_cabonara *= order_SS;
            amount_SS += spaghetti_cabonara;
            break;
            
            case 2 :
            cout << "How many : ";
            cin >> order_SS ;
            spaghetti_becon *= order_SS;
            amount_SS += spaghetti_becon;
            break;
            
            case 3 :
            cout << "How many : ";
            cin >> order_SS ;
            spaghetti_seafood *= order_SS;
            amount_SS += spaghetti_seafood;
            break;
            
            case 4 :
            cout << "How many : ";
            cin >> order_SS ;
            hotdog *= order_SS;
            amount_SS += hotdog;
            break;
            
            case 5 :
            cout << "How many : ";
            cin >> order_SS ;
            french_fries *= order_SS;
            amount_SS += french_fries;
            break;
            
            case 6 :
            cout << "How many : ";
            cin >> order_SS ;
            sandwich *= order_SS;
            amount_SS += sandwich;
            break;
            
            case 7 :
                if (number1 == 5);
                exit(1);
        }
        cout << "Total : " << amount_SS << " ฿"<< endl <<endl ;
        cout << "You Want Buy again ? [ yes = y or no = n ] : ";
        cin >> answer ;
    }
    cout << endl << "Totality = " << amount_SS << endl ;
    while(amount_SS > 0 ) {
            cout << "Please enter the amount : " ;
            cin >> change_money2 ;
            if (change_money2 < amount_SS) {
                cout << "Money not enought. Please Enter again "<< endl;
            }
            
            else if (change_money2 >= amount_SS) {
                change2 = change_money2 - amount_SS ; 
                break; 
            }
    }
    cout << "Food change = " << change2 << " ฿" << endl;
};

class Sweets {
    public :
    string name,table;
    char answer = 'Y' ;
    int number,order_SW,amount_SW,change_money,change;
    float Pancake = 79, French_toasts = 109, Banoffee_pie = 59, Croissant = 59, Cupcake_vanilla = 65;
    
    Sweets(float show_Amount) {
        amount_SW = show_Amount;
    }
    Sweets(float show_Amount,int show_Number) {
        amount_SW = show_Amount;
        number = show_Number;
    }
    void show_total(){
        string name,table;
        char answer = 'Y' ;
        int show_Number,order_SW,change_moneychange;
        float show_Amount,Pancake = 79, French_toasts = 109, Banoffee_pie = 59, Croissant = 59, Cupcake_vanilla = 65;
        
        cout << "Name : ";
        cin >> name;
        cout << "Table No. : ";
        cin >> table;
        while ( answer =='y' or answer =='Y') {
            cout << "--------- SWEETS ---------" << endl;
            cout << "[1] Pancake          79 ฿ "<< endl;
            cout << "[2] French Toasts   109 ฿ "<< endl;
            cout << "[3] Banoffee Pie     59 ฿ "<< endl;
            cout << "[4] Croissant        59 ฿ "<< endl;
            cout << "[5] Cupcake Vanilla  65 ฿ "<< endl;
            cout << "[6] Exit "<< endl << endl;
            cout << "What number did you pick : ";   
            cin >> number;
            switch(number) {
                case 1 :
                cout << "How many : ";
                cin >> order_SW ;
                Pancake *= order_SW;
                amount_SW += Pancake;
                break;
                
                case 2 :
                cout << "How many : ";
                cin >> order_SW ;
                French_toasts *= order_SW;
                amount_SW += French_toasts;
                break;
                
                case 3 :
                cout << "How many : ";
                cin >> order_SW ;
                Banoffee_pie *= order_SW;
                amount_SW += Banoffee_pie;
                break;
                
                case 4 :
                cout << "How many : ";
                cin >> order_SW ;
                Croissant *= order_SW;
                amount_SW += Croissant;
                break;
                
                case 5 :
                cout << "How many : ";
                cin >> order_SW ;
                Cupcake_vanilla *= order_SW;
                amount_SW += Cupcake_vanilla;
                break;
                
                case 6 :
                    if (number == 6);
                    exit(1);
            }
            cout << "Total : " << amount_SW << " ฿"<< endl <<endl ;
        cout << "You Want Buy again ? [ yes = y or no = n ] : ";
        cin >> answer ;
        }
        cout << endl << "Totality = " << amount_SW << endl ;
        while(amount_SW > 0 ) {
            cout << "Please enter the amount : " ;
            cin >> change_money ;
            if (change_money < amount_SW) {
                cout << "Money not enought. Please Enter again "<< endl;
            }
                
            else if (change_money >= amount_SW) {
                change = change_money - amount_SW ; 
                break; 
            }
        }
        cout << "Food change = " << change << " ฿" << endl;
    };
};

class Feedback {
    public :
    string name;
    void show_name(){
        cout <<"Name : ";
        cin >> name ;
    };
};

class Good : public Feedback {
    public:
    string text ;
    void show_Good() {
        ifstream f;  
        f.open("good.txt");
        string line;
        while(getline(f,line)) {
            cout << line << endl;
        }
    f.close(); 
    };
};

class Bad : public Feedback {
    public:
    string text ;
    void show_Bad() {
        ifstream f;  
        f.open("bad.txt");
        string line;
        while(getline(f,line)) {
            cout << line << endl;
        }
    f.close(); 
    };
};
    
int main() {
    int answer_main;
    char main_as;
    
    Food f1;
    float show_Amount;
    int show_Number;
    Sweets s1(show_Amount);
    Sweets s2(show_Amount,show_Number);
    Good g1;
    Bad b2;
    do {
        
        cout << endl << "------- 'WELCOME TO THE FOOD SHOP' -------" << endl << endl;
        cout << "=========== MENU ======== " << endl;
        cout << " [1] Pizza " << endl;
        cout << " [2] Spaghetti & Starter" << endl;
        cout << " [3] Sweets " << endl ;
        cout << " [4] Feedback " <<endl ;
        cout << " [5] Exit" << endl<<endl;
        cout << "Select number 1/2/3/4/5 : " ;
        cin >> answer_main;
        switch(answer_main) {
            case 1:
            cout << endl ;
            f1.Pizza();
            break;
            
            case 2:
            cout << endl ;
            f1.Spaghetti();
            break;
            
            case 3 :
            cout << endl ;
            s1.show_total();
            break;
            
            case 4 :
            cout << endl ;
            int select;
            char ans;
            do {
                cout <<"[1] REVIEW " << endl;
                cout <<"[2] FEEDBACK " << endl;
                cout <<"Select Number : ";
                cin >> select;
                switch(select)
                {
                    case 1 :
                    cout << endl ;
                    g1.show_Good();
                    break;
                    case 2 : 
                    cout << endl ;
                    b2.show_Bad();
                    break;
                }
                cout << endl << "Back to select Again [ yes = y or no = n ] : ";
                cin >> ans ;
                cout << endl ;
            }
            while(ans =='y' || ans =='Y') ;
            break;
            
            case 5:
            if (answer_main == 5) {
                exit(1);
                }
            
            default:
                cout <<"\t\tThis is not exsit so try again!" << endl;
        }
        cout <<"Back to Menu [ yes = y or no = n ] : ";
        cin >> main_as ;
        if(main_as =='n' or main_as =='N') {
        }
    }
    while(main_as =='y' or main_as =='Y') ;
}
