#define _GNU_SOURCE

#include <time.h>
#include <stdio.h>
#include <sched.h>
#include <pthread.h>
#include <stdlib.h>


cpu_set_t mask;
CPU_ZERO(&mask);
CPU_SET(3, &mask);
if (sched_setaffinity(0, sizeof(mask), &mask) < 0) {
    printf("set_Aff?")
}

printf("Hello")