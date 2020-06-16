#include<stdio.h>
 #include<math.h>
// PRINTS ALL LEAP YEARS WITHIN USER SPECIFIED RANGE
int main(){
int start;
int end;
printf("Enter start year:");
scanf("%d", &start);
// asks for user input for start
printf("Enter end year:");
scanf("%d", &end);
// asks for user input for end
int temp=start-((start/4)*4);
// check if starting year is a leap year
int leap=(start/4)*4;
if (temp==0){
printf("%d", leap);
}leap=leap+4;
// print every four years until less than or equal to end range
while (leap<=end){
printf("%d", leap);
leap=leap+4;
}return 0;
}