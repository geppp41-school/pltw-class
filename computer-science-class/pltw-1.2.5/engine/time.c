// Source - https://stackoverflow.com/a
// Posted by cmh, modified by community. See post 'Timeline' for change history
// Retrieved 2025-11-10, License - CC BY-SA 4.0

#include <stdio.h>
#include <sys/time.h>


// int main(void){
//     struct timeval val;
//     gettimeofday(&val, NULL);
    
//     printf("%f \n", val.tv_sec+(val.tv_usec/1000000.0));
// }
double getTimeMs(){
    struct timeval val;
    gettimeofday(&val, NULL);
    

    
    return (val.tv_sec+(val.tv_usec/1000000.0));
}
