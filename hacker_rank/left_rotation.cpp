#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);


void left_rotate( vector<int>& a, int rotation_number ){
    
    int counter = rotation_number;

    int length = a.size() ;


    while( counter > 0 ){
        
        int key = a[length - 1];
        int next_key = key;
        for( int i = length; i > -1; i-- ){
            int index = ( ( i - 1 )%length );
            next_key = a[index-1];
            a[index - 1] = key;
            key = next_key;
        }
        
        counter--;
    }

}


int main()
{
    string nd_temp;
    getline(cin, nd_temp);

    vector<string> nd = split_string(nd_temp);

    int n = stoi(nd[0]);

    int d = stoi(nd[1]);

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split_string(a_temp_temp);

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }
    
    left_rotate( a, d );

    std::cout<<"seg\n";


    for( std::vector<int>::iterator it = a.begin(); it != a.end(); it++ ){
        std::cout<<*(it) << " ";
    }
    std::cout<<endl;
    // std::vector<int>::iterator it = a.begin();
    // for( auto it = a.begin(); it != a.end(); it++ ){
    //     std::cout<<*(it) << " ";
    // }
    //std::cout<<std::endl;
    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
