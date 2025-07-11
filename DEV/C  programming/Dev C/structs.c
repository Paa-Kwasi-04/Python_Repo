#include <stdio.h>

// Structures are C types that can hold multiple data types
typedef struct Player { /* typedef keyword makes the Player struct a data type
 * Thus, we do not need to always call struct Player*/
    char name[16];
    float health;
    float location_x;
    float location_y;
}Player;

typedef struct Student{
    char name[16];
    int roll_no;
    int c_prog;
    int emerging_tech;
}Student;

void loseHealth(Player *pObject){
    pObject -> health -= 0.3f;
}

void gainHealth(Player *pObject){
    pObject -> health += 0.15f;
}

void updateLocation(Player *pObject, float x, float y){
    pObject -> location_x = x;
    pObject -> location_y = y;
}

int main() {
    // A possible application of structures in keeping students name's and scores
    Student st1 = {"John", 155, 100, 96};
    Student st2 = {"Jon",  154, 100, 96};
    Student st3 = {"Jo",   153, 100, 96};
    Student st4 = {"Jack", 152, 100, 96};

    Student myStudents[4] = {st1, st2, st3, st4};
    for (int i=0;i<4;i++){
        printf("%s %d %d %d \n", myStudents[i].name,myStudents[i].roll_no,myStudents[i].c_prog,myStudents[i].emerging_tech);
    }

    Player Player1 = {"Wesley", 1.0f, 0.0f, 0.0f};
    printf("You have created: %s", Player1.name);
    loseHealth(&Player1);
    printf("\n%s's health: %.2f", Player1.name, Player1.health);
    updateLocation(&Player1, 1.0f, 0.5f);
    printf("\n%s's location: (%.2f, %.2f)", Player1.name, Player1.location_x, Player1.location_y);
    return 0;
}











