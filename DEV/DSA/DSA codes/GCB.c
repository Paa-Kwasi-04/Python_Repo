// Created by User on 9/14/2023.
// get their bank accounts
// get the amounts in the account
// cross-check is they are the ones redrawing for the bank
// tell them their balance at the end of the program
#include "stdio.h"
#define N 30
#include "stdlib.h"
#include "conio.h"

typedef struct ATM
{
    char name[N];
    int pin;
    float amount;
} ATM;

struct node
{
    struct node *prev;
    ATM atm;
    struct node *next;
};
int choice, ans, x;
struct node *head = NULL, *new_node, *temp, *pretemp, *ptr;

struct node *search(int pin, struct node *y)
{
    temp = y;
    while (temp->atm->pin != pin)
    {
        temp = temp->next;
    }

    return temp;
}
struct node *create_account(struct node *y)
{
    do
    {
        new_node = (struct node *)malloc(sizeof(struct node));
        printf("Enter your Full name: ");
        scanf("%s", &new_node->atm->name);
        getch();
        printf("Enter a four digit pin number: ");
        scanf("%d", &new_node->atm->pin);
        getch();
        printf("Enter initial deposit amount: ");
        scanf("%f", &new_node->atm->amount);

        if (y == NULL)
        {
            y = temp = new_node;
            new_node->prev = NULL;
            new_node->next = NULL;
        }
        else
        {
            temp->next = new_node;
            new_node->prev = temp;
            new_node->next = NULL;
            temp = new_node;
        }
        getch();
        printf("Create another bank account: ");
        scanf("%d", &choice);
    } while (choice != 0);

    return y;
}
struct node *delete_account(struct node *y)
{
    temp = y;
    int pin;
    printf("Enter Account to be deleted: ");
    scanf("%d", &pin);

    while (temp->atm->pin != pin)
    {
        pretemp = temp;
        temp = temp->next;
    }
    pretemp->next = temp->next;
    temp->next->prev = pretemp;
    free(temp);

    return y;
}
struct node *deposit(struct node *y)
{
    int pin;
    float amount;
    printf("Enter your pin number: ");
    scanf("%d", &pin);
    ptr = search(pin, y);

    getch();
    printf("Enter amount to be deposited: ");
    scanf("%f", &amount);

    ptr->atm->amount += amount;

    return y;
}
struct node *withdrawal(struct node *y)
{
    int pin;
    float amount;
    printf("Enter your pin number: ");
    scanf("%d", &pin);
    ptr = search(pin, y);

    getch();
    printf("Enter amount to be withdrawn: ");
    scanf("%f", &amount);

    ptr->atm->amount -= amount;

    return y;
}
int check_balance(struct node *y)
{
    int pin;
    float amount;
    printf("Enter your pin number: ");
    scanf("%d", &pin);
    ptr = search(pin, y);

    return ptr->atm->amount;
}

int main()
{

    do
    {
        printf("Welcome To GCB Bank PLC Limited\n");

        printf("\n\n----ATM Services----\n"
               "\n1. Create bank account"
               "\n2. Deposit Cash"
               "\n3. Withdraw Money"
               "\n4. Check Balance"
               "\n5. Delete Account"
               "\n6. Exit");

        printf("\n\n");
        printf("Which of the Services do You require: ");
        scanf("%d", &ans);

        switch (ans)
        {
        case 1:
            head = create_account(head);
            printf("Accounts have been created");
            break;
        case 2:
            head = deposit(head);
            printf("Amount has been credited");
            break;
        case 3:
            head = withdrawal(head);
            printf("Amount has been debited");
            break;
        case 4:
            x = check_balance(head);
            printf("Your balance is: %d", x);
            break;
        case 5:
            head = delete_account(head);
            printf("Account has  deleted");
            break;
        default:
            printf("invalid response\nTry again");
            break;
        }

    } while (ans != 6);
    return 0;
}
