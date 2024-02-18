#include <iostream>
#include <string>

using namespace std;

struct node{
    node* child[10]{nullptr};
    bool isWord = false;
    unsigned int cnt = 0;
};

bool insert(string& word, node* root){
    node* cur = root;
    for(char c : word) {
        cur->cnt++;
        node* child = cur->child[c - '0'];
        if(child == nullptr)
            cur->child[c - '0'] = new node();
        cur =  cur->child[c - '0'];
        if(cur->isWord)
            return false;
    }
    cur->isWord = true;
    if(cur->cnt)
        return false;
    cur->cnt++;
    return true;
}

int main() {
    unsigned int n,q;
    string tmp;

    cin >> n;

    while(n--) {
        node* root = new node;
        cin >> q;
        bool res = true;
        while(q--){
            cin >> tmp;
            bool add_num = insert(tmp, root);
            if(!add_num) {
                res = false;
            }
        }
        if(res)
            cout << "YES\n";
        else
            cout << "NO\n";
    }
    return 0;
}