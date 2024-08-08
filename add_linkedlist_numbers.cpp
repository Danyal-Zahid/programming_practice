
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     long long int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(long long int x) : val(x), next(nullptr) {}
 *     ListNode(long long int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Leetcode: https://leetcode.com/problems/add-two-numbers/
class Solution {
private:
    long long int convertToNumber(ListNode* l){
        ListNode* curr = l;
        long long int number = 0;
        long long int multiplier = 1;
        while(curr != nullptr){
            number = number + curr->val * multiplier;
            multiplier = multiplier * 10;
            curr = curr->next;
        }
        return number;
    }
    ListNode* convertToList(long long int number){
        ListNode* result = nullptr;
        if (number == 0) {
            return (new ListNode(number, nullptr));
        }
        while(number != 0){
            long long int currentValue = number % 10;
            number = floor(number / 10);
            ListNode* temp = new ListNode(currentValue, nullptr);
            if(result != nullptr){
                temp->next = result;
                result = temp;
            } 
            else {
                result = temp;
            }
        }
        return result;
    }
    ListNode* reverseList(ListNode* lst){
        ListNode* curr = lst;
        ListNode* prev = nullptr;
        while(curr != nullptr) {
            ListNode* tnext = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tnext;
        }
        return prev;
    }
    string addLists(ListNode* l1, ListNode* l2) {
        string result = "";
        int carry = 0;
        while(l1 != nullptr || l2 != nullptr) {
            int l1v = 0;
            int l2v = 0;
            if(l1 != nullptr) {
                l1v = l1->val;
                l1 = l1->next;
            }
            if(l2 != nullptr) {
                l2v = l2->val;
                l2 = l2->next;
            }
            int temp = carry + l1v + l2v;
            if (temp > 9) {
                carry = floor(temp/10);
                temp = temp%10;
            } else {
                carry = 0;
            }
            result = result + to_string(temp);
        }
        if (carry != 0) {
            result = result + to_string(carry);
        }
        return result;
    }

    ListNode* constructListFromString(string str) {
        ListNode* res = nullptr;
        ListNode* head = nullptr;
        int i = 0;
        while (i < str.length()) {
            int c = str[i] - '0';
            ListNode* temp = new ListNode(c, nullptr);
            if (res == nullptr) {
                res = temp;
                head = res;
            }
            else {
                res->next = temp;
                res = temp;
            }
            i += 1;
        }
        return head;
    }
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // long long int num1 = this->convertToNumber(l1);
        // long long int num2 = this->convertToNumber(l2);
        // ListNode* res = this->convertToList(num1+num2);
        // return this->reverseList(res);
        return this->constructListFromString(this->addLists(l1, l2));;
    }
};